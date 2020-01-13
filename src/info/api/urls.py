from django.urls import path

from .views import ItemListView, ItemDetailView, UserListView, UserDetailView

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('items/<pk>', ItemDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<pk>', UserDetailView.as_view())
]
