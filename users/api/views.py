import jwt
from django.http import response
from users.models import Todo, User
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from users.api.serializers import UserSerializer, LoginSerializer, TodoSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


def roles(user):
    if user.is_superuser:
        return "Admin"
    else:
        return "User"


class RegisterView(GenericAPIView):
    """
    post:
    Register/Create User
    """

    serializer_class = UserSerializer

    @swagger_auto_schema(tags=["Authentication API"])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    """
    post:
    Login User with JWT Token response
    """

    serializer_class = LoginSerializer

    @swagger_auto_schema(tags=["Authentication API"], responses={200: "JWT Token"})
    def post(self, request):
        data = request.data
        email = data.get("email", "")
        password = data.get("password", "")
        user = auth.authenticate(email=email, password=password)
        if user:
            auth_token = jwt.encode(
                {
                    "first_name": str(user.first_name),
                    "last_name": str(user.last_name),
                    "email": str(user.email),
                    "is_active": str(user.is_active),
                    "role": roles(user),
                },
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            data = {"token": auth_token}
            return Response(data)

        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


########################Todo CRUD Operations############################


class TodoList(APIView):
    """
    get:
    Todo Items Lists as JSON response.
    """

    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(tags=["Todo Item API"], responses={200: TodoSerializer})
    def get(self, request, format=None):
        todo = Todo.objects.all()
        data = TodoSerializer(todo, many=True).data
        return Response(data)


class TodoCreate(APIView):
    """
    post:
    Creates a Todo Item and show it as JSON response.
    Only Admin can access this API.
    """

    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(tags=["Todo Item API"], request_body=TodoSerializer)
    def post(self, request, format=None):
        if request.user.is_superuser is not True:
            content = {"status": "Unauthorized.User is not Admin"}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            create = serializer.create(validated_data)
            data = self.serializer_class(create).data
            return Response(data, status=status.HTTP_201_CREATED)


class TodoRetrieve(APIView):
    """
    get:
    Retrieves specific Todo Item as JSON response.
    Only Admin can access this API.
    """

    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(tags=["Todo Item API"], responses={200: TodoSerializer})
    def get(self, request, pk, format=None):
        if request.user.is_staff is not True:
            content = {"status": "Unauthorized..User is not Admin"}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                todo = Todo.objects.get(id=pk)
                data = TodoSerializer(todo).data
                return Response(data)
            except Todo.DoesNotExist:
                content = {"status": f"Not Found Todo No.-{pk}"}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdate(APIView):
    """
    put:
    Updates specific Todo Item and show it as JSON response.
    Only Admin can access this API.
    """

    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(tags=["Todo Item API"], responses={200: TodoSerializer})
    def put(self, request, pk, format=None):
        if request.user.is_staff is not True:
            content = {"status": "Unauthorized.User is not Admin"}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                todo = Todo.objects.get(id=pk)
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                validated_data = serializer.validated_data
                update = serializer.update(todo, validated_data)
                data = self.serializer_class(update).data
                return Response(data)
            except Todo.DoesNotExist:
                content = {"status": f"Not Found Todo No.-{pk}"}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)


class TodoDelete(APIView):
    """
    delete:
    Deletes specific Todo Item.
    Only Admin can access this API.
    """

    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        tags=["Todo Item API"], responses={200: "Deleted Todo No.-{id}"}
    )
    def delete(self, request, pk, format=None):
        if request.user.is_staff is not True:
            content = {"status": "Unauthorized.User is not Admin"}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            try:
                todo = Todo.objects.get(id=pk)
                todo.delete()
                content = {"status": f"Deleted Todo No.-{pk} "}
                return Response(content)
            except Todo.DoesNotExist:
                content = {"status": f"Not Found Todo No.-{pk}"}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
