from rest_framework import serializers
from info.models import Item
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'number', 'production_date', 'shelf_life', 'expiration_date', 'owner')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password')  # To makesure passwords are not displayed

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        print(validated_data)
        user.set_password(validated_data['password'])  # To generate a hash for the password
        user.save()
        return user
