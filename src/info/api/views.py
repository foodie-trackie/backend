from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from info.models import Item, User
from .serializers import ItemSerializer, UserSerializer


class UserItemListView(ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Item.objects.filter(user_id=user_id)


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
