from django.urls import path

from .views import UserItemListView, UserListCreateView, UserDetailView, signup_view, login_view

urlpatterns = [
    path('items/<owner>', UserItemListView.as_view()),
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('signup/', signup_view),
    path('login/', login_view)
]
