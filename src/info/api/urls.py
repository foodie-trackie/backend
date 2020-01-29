from django.urls import path

from .views import UserItemListView, UserListCreateView, ItemDetailView, ItemCreateView, UserDetailView, signup_view, login_view

urlpatterns = [
    path('users/<owner>/items/', UserItemListView.as_view()),
    path('items/<int:pk>', ItemDetailView.as_view()),
    path('items/', ItemCreateView.as_view()),
    path('users/', UserListCreateView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('signup/', signup_view),
    path('login/', login_view)
]
