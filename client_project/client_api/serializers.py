from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer
from client_api.models import Client


class ClientRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    photo = serializers.ImageField(use_url='images', required=False)
    adress = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    username = serializers.CharField(required=True, write_only=True)

    class Meta:

        model = Client
        fields = ['first_name', 'last_name', 'adress', 'photo']

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError("A user is already registered with this e-mail address.")
        return email

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'photo': self.validated_data.get('photo'),
            'adress': self.validated_data.get('adress'),
            'first_name': self.validated_data.get('first_name'),
            'last_name': self.validated_data.get('last_name'),

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.photo = self.cleaned_data.get('photo')
        user.adress = self.cleaned_data.get('adress')
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()

        return user


# get all user
class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'adress',
            'photo',
        ]


# edit user
class ClientUpdateSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'adress',
            'photo',

        ]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'adress',
            'photo',
        ]


class ClientDeleteSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'adress',
            'photo',
        ]
