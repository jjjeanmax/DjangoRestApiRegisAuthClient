from django.urls import path, include
from . import views
from .views import (
    ClientListView,
    EditClientView,
    DetailClientView,
    DeleteClientView,
    info,
)

urlpatterns = [
    path('', views.info, name='info'),

    path('list/', ClientListView.as_view(), name='all client'),
    path('<id>/detail/', DetailClientView.as_view(), name='detail'),
    path('<id>/edit/', EditClientView.as_view(), name='edit'),
    path('<id>/delete/', DeleteClientView.as_view(), name='delete'),
]
