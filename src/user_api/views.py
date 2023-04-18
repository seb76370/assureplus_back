from pprint import pprint
from rest_framework.views import APIView

from rest_framework.exceptions import AuthenticationFailed
from user_api.models import Users
from .serializers import UsersReadSerializers, UsersResetPasswordSerializers, UsersSerializers
from rest_framework.response import Response
import jwt, datetime

import environ
env = environ.Env()
environ.Env.read_env()


class registerView(APIView):
    def post(self, request):
        serializer = UsersSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class loginView(APIView):
    def post(self, request):
        response =Response()
        # headers = request.META

        email = request.data.get('email')
        password = request.data.get('password')
        user = Users.objects.filter(email=email).first()

        if user is None:                                
            response.data = {
                'message': 'user unknow',
            }

            return response
        
        if not user.check_password(password):                             
            response.data = {
                'message': 'Login/password fail',
            }

            return response
        

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,env('SECRET_KEY'),algorithm='HS256')

        response =Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
                            
        response.data = {
            'message': 'success',
            'jwt': token
        }

        return response
    
class userView(APIView):

    def post(self, request):
        isconnected = True
        token = request.data.get('jwt')
        if not jwt:
            raise AuthenticationFailed({"status_code":502,"message":"User not conected"})
        
        try:
            payload = jwt.decode(token,env('SECRET_KEY'),algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            isconnected = False
        
        if isconnected:
            user = Users.objects.filter(id=payload['id']).first()
            serializer = UsersReadSerializers(user)

            return Response(serializer.data)
        else:
            print("raiseeeee")
            raise AuthenticationFailed({"status_code":502,"message":"Erreur JWT"})
    
class resetView(APIView):

    def post(self, request):
        token = request.data.get('jwt')
        newPassword:str = request.data.get('password')
        if not jwt:
            raise AuthenticationFailed('Unauthenticated')
        try:
            token = jwt.decode(token,env('SECRET_KEY'),algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        serializer = UsersResetPasswordSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = Users.objects.filter(id=token['id']).first()
        user.set_password(newPassword)
        user.save()

        response = Response()
        response.data = {
            'message': 'success'
        }
        return response
    
class logoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
