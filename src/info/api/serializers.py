from rest_framework import serializers

from info .models import Item, User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'number', 'production_date', 'shelf_life', 'expiration_date', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')
