from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from info.models import Item
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .serializers import ItemSerializer, UserSerializer


class UserItemListView(ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Item.objects.filter(owner=owner)


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET', 'POST'])
def signup_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # user = authenticate(username=username, password=password)
    # login(request, user, backend='django.contrib.auth.backends.ModelBackend')


# class CreateUserView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
