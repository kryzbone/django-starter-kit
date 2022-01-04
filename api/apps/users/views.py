from djoser import views as djoser_views
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    search_fields = ("email", "username")
    ordering_fields = ("created_at", "username", "email")
    lookup_field = "uuid"

    ordering = ("created_at",)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(data=serializer.data, status=HTTP_200_OK)


class CustomRegistrationViewSet(djoser_views.UserViewSet):
    loopup_fields = "uuid"
