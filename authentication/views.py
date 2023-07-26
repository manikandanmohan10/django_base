import logging
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from authentication.tasks import test_task
from .serializer import LibrarySerializer, RegisterSerializer, BookSerializer, UserProfileSerializer
from .models import Library, User, Book, UserProfile
from http import HTTPStatus as STATUS
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.db.models import Q

logger = logging.getLogger(__name__)
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


class DeleteUser(APIView):
    def delete(self, request):
        try:
            user_id = request.query_params.get('id')
            if not user_id:
                return Response('User not found', status=STATUS.NOT_FOUND)    
            
            user = User.objects.get(user_id=user_id)
            if not user:
                return Response('User not found', status=STATUS.NOT_FOUND)    

            user.delete()
            return Response('User deleted successfully', status=STATUS.OK)
            
        except Exception as e:
            return Response(str(e), status=STATUS.BAD_REQUEST)


class Generic(GenericAPIView):
    def post(self, request):
        return Response('POST From GenericView', status=STATUS.OK)
    
    def get(self, request):
        # print(request.META)
        # print(request.META.get('SERVER_SOFTWARE'))
        # return Response('GET From GenericView ---', status=STATUS.OK)
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        return HttpResponse('GET From GenericView', status=STATUS.OK)
    
    def put(self, request):
        return Response('PUT from Genericview', status=STATUS.OK)
    
    def delete(self, request):
        return Response('DELETE from Genericview', status=STATUS.OK)
    
    def patch(self, request):
        return Response('PATCH from Genericview', status=STATUS.OK)
    

class BookAPI(APIView):
    serializer_class = BookSerializer
    def post(self, request):
        try:
            book_data = request.data
            serializer = self.serializer_class(data=book_data)
            serializer.is_valid(raise_exception=True)
            book = Book.objects.create(
                book_name = book_data.get('book_name', ''),
                publish_date = book_data.get('publish_date', ''),
                book_owner_id = book_data.get('book_owner', '')
            )
            book.save()
            response_data = {
                'status': 'success',
                'statusCode': 201,
                'data': book_data
            }
            return Response(response_data, status=STATUS.CREATED)

        except Exception as e:
            print(str(e))
            return Response(str(e), status=STATUS.BAD_REQUEST)


class UserProfileAPI(APIView):
    serializer_class = UserProfileSerializer
    def post(self, request):
        try:
            user_data = request.data
            serializer = self.serializer_class(data=user_data)
            serializer.is_valid(raise_exception=True)
            data = UserProfile.objects.create(
                user_role=user_data.get('user_role'),
                user_department=user_data.get('user_department'),
                employee=user_data.get('employee')
            )
            data.save()
            response_data = {
                'status': 'success',
                'statusCode': 201,
                'data': serializer.data
            }
            return Response(response_data, status=STATUS.CREATED)
        except Exception as e:
            return Response(str(e), status=STATUS.BAD_GATEWAY)
        

class LibraryAPI(APIView):
    serializer_class = LibrarySerializer
    def post(self, request):
        try:
            user_data = request.data
            serializer = self.serializer_class(data=user_data)
            serializer.is_valid(raise_exception=True)
            data = Library.objects.create(
                library_name=user_data.get('library_name') 
            )
            data.save()
            response_data = {
                'status': 'success',
                'statusCode': 201,
                'data': serializer.data
            }
            return Response(response_data, status=STATUS.CREATED)
        except Exception as e:
            return Response(str(e), status=STATUS.BAD_GATEWAY)
        

class LibrarySubscriptionAPI(APIView):
    def post(self, request):
        user_data = request.data
        user = User.objects.get(user_id=user_data.get('user_id'))
        library = Library.objects.get(library_name=user_data.get('library_name'))
        if user and library:
            library.members.add(user)   
            library.save()

        return Response('Success', status=STATUS.OK)