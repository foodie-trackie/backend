from rest_framework import serializers
from info.models import Item
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'number', 'production_date', 'shelf_life', 'expiration_date', 'owner')


class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'items']
