from django.urls import path

from .views import UserItemListView, ItemDetailView, UserListView, UserDetailView

urlpatterns = [
    path('items/<owner>', UserItemListView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]
