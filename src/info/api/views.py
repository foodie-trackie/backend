from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from info.models import Item
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .serializers import ItemSerializer, UserSerializer
import json


class UserItemListView(ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Item.objects.filter(owner=owner)


class ItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def signup_view(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    if request.method == 'POST':
        form = SignUpForm(data)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return HttpResponse(form.errors.as_json(), status=400)


def login_view(request):
    data = json.loads(request.body.decode('utf-8'))
    if request.method == 'POST':
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        userData = UserSerializer(user).data
        if user is not None:
            login(request, user)
            return HttpResponse(json.dumps({'id': userData['id'], 'username': userData['username'], 'email': userData['email']}), status=200)
        return HttpResponse(status=404)
