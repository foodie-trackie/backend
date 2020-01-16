from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from info.models import Item
from django.contrib.auth.models import User
from .serializers import ItemSerializer, UserSerializer


class UserItemListView(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Item.objects.filter(owner=owner)


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
