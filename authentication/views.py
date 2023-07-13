import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from authentication.tasks import test_task
from .serializer import RegisterSerializer
from .models import User
from http import HTTPStatus as STATUS
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# Create your views here.
class Register(CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.create(user_data)
            response = {
                'status': 'success',
                'statusCode': 201,
                'message': 'User created successfully'
            }
            return Response(response, status=STATUS.CREATED)

        except Exception as e:
            print(str(e))
            return Response(str(e), status=STATUS.BAD_REQUEST)
        
    def get(self, request):
        test_task.delay()
        # test_task()

        return Response('From Create View', status=STATUS.OK)
        
    

class Login(APIView):
    def post(self, request):
        user_data = request.data
        user = User.objects.get(user_id=user_data.get('user_id'))
        token = user.get_tokens()
        response = {
            'status': 'success',
            'statusCode': 200,
            'data': token
        }
        return Response(response, status=STATUS.OK)
    
    def get(self, request):
        return Response('GET From APIView', status=STATUS.OK)
    
    def put(self, request):
        return Response('PUT from APIview', status=STATUS.OK)
    
    def delete(self, request):
        return Response('DELETE from APIview', status=STATUS.OK)
    
    def patch(self, request):
        return Response('PATCH from APIview', status=STATUS.OK)


class Generic(GenericAPIView):
    def post(self, request):
        return Response('POST From GenericView', status=STATUS.OK)
    
    def get(self, request):
        print(request.META)
        print(request.META.get('SERVER_SOFTWARE'))
        return Response('GET From GenericView', status=STATUS.OK)
    
    def put(self, request):
        return Response('PUT from Genericview', status=STATUS.OK)
    
    def delete(self, request):
        return Response('DELETE from Genericview', status=STATUS.OK)
    
    def patch(self, request):
        return Response('PATCH from Genericview', status=STATUS.OK)
    