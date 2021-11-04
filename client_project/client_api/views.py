from django.shortcuts import render
from client_api.models import Client
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)

from .serializers import (
    ClientListSerializer,
    ClientRegisterSerializer,
    ClientUpdateSerializer,
    ClientDetailSerializer,
    ClientDeleteSerializer,

)


class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer


class EditClientView(UpdateAPIView):
    lookup_field = 'id'
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientUpdateSerializer


class DetailClientView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientDetailSerializer


class DeleteClientView(DestroyAPIView):
    lookup_field = 'id'
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientDeleteSerializer


def info(request):
    return render(request, template_name='client_api/info.html', context=None)
