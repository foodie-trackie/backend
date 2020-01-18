from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
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


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    print(username)

    user = authenticate(username=username, password=password)
    login(request, user)


# class CreateUserView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
