from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
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
    data = json.loads(request.body.decode('utf-8'))
    print(json.loads(request.body.decode('utf-8')))
    if request.method == 'POST':
        form = SignUpForm(data)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return HttpResponse(form.errors.as_json(), status=400)

