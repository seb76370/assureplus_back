import jwt
import json
from django.http import JsonResponse

import environ
env = environ.Env()
environ.Env.read_env()

def jwt_required(func):
    def wrapper(request, *args, **kwargs):
        body = json.loads(request.body)
        token = body.get('jwt', '')

        if not token:
            return JsonResponse({'error': 'JWT token not found'}, status=401)

        try:
            jwt.decode(token,env('SECRET_KEY'),algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'JWT token has expired'}, status=401)
        except (jwt.InvalidTokenError, IndexError):
            return JsonResponse({'error': 'Invalid JWT token'}, status=401)
        return func(request, *args, **kwargs)
    
    return wrapper