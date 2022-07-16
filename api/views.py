from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsersListSerializer
from .models import BotUsers


class RegisterLoginUsers(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            serializer = UsersListSerializer(BotUsers.objects.get(user_id=request.query_params.get("user_id"))).data
            content = {
                'user': str(request.user),
                'data': serializer,
                "status_code": 200
            }
            return Response(content)
        except:
            content = {
                'user': str(request.user),
                "status_code": 404
            }
            return Response(content, status=404)

    def post(self, request):
        serializer = UsersListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {"data": serializer.data, "status_code": 201}
            return Response(content)
        else:
            content = {"data": serializer.errors, "status_code": 400}
            return Response(content)

    def put(self, request):
        try:
            is_deleted = request.data.get("is_deleted")
            new_data = UsersListSerializer(BotUsers.objects.get(user_id=request.data.get("user_id"))).data
            new_data["is_deleted"] = is_deleted
            serializer = UsersListSerializer(BotUsers.objects.get(user_id=request.data.get("user_id")), data=new_data)
            if serializer.is_valid():
                serializer.save()
                content = {
                    'user': str(request.user),
                    'data': serializer.data,
                    "status_code": 200
                }
                return Response(content)
            else:
                content = {"data": serializer.errors, "status_code": 400}
                return Response(content)
        except:
            content = {
                'user': str(request.user),
                "status_code": 404
            }
            return Response(content, status=404)


class UsersList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            serializer = UsersListSerializer(BotUsers.objects.all(), many=True).data
            content = {
                'user': str(request.user),
                'data': serializer,
                "status_code": 200
            }
            return Response(content)
        except:
            content = {
                'user': str(request.user),
                "status_code": 404
            }
            return Response(content, status=404)

    def post(self, request):
        try:
            is_deleted = request.data.get("is_deleted")
            users = BotUsers.objects.all()
            for user in users:
                new_data = UsersListSerializer(BotUsers.objects.get(user_id=user.user_id)).data
                new_data["is_deleted"] = is_deleted
                serializer = UsersListSerializer(BotUsers.objects.get(user_id=user.user_id), data=new_data)
                if serializer.is_valid():
                    serializer.save()
            content = {
                'user': str(request.user),
                'data': "Changes Applied",
                "status_code": 200
            }
            return Response(content)

        except Exception as e:
            print(e)
            content = {
                'user': str(request.user),
                "status_code": 404
            }
            return Response(content, status=404)
