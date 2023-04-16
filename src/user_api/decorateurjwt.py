import jwt
import json
from django.http import JsonResponse

import environ
env = environ.Env()
environ.Env.read_env()

def jwt_required(func):
    def wrapper(request, *args, **kwargs):
        token = request.META.get('HTTP_JWT')

        if not token:
            return JsonResponse({'error': 'JWT token not found'}, status=401)

        try:
            jwt.decode(token,env('SECRET_KEY'),algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            print("jwt.ExpiredSignatureError")
            return JsonResponse({'error': 'JWT token has expired'}, status=401)
        except (jwt.InvalidTokenError, IndexError):
            print("jwt.InvalidTokenError, IndexError")
            return JsonResponse({'error': 'Invalid JWT token'}, status=401)
        
        print("return wrapper")
        return func(request, *args, **kwargs)
    
    print("return wrapper")
    return wrapper