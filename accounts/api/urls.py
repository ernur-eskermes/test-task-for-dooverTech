from django.urls import path

from . import views

urlpatterns = [
    path(
        'create/',
        views.ClientCreateAPIView.as_view(),
        name='client_create_api'
    ),
    path(
        '<int:client_id>/',
        views.ClientDetailAPIView.as_view(),
        name='client_detail_api'
    ),
    path(
        '<int:client_id>/address/',
        views.UserAddressCreateAPIView.as_view(),
        name='address_create_api'
    ),
    path(
        '<int:client_id>/products/',
        views.ClientProductAPIView.as_view(),
        name='client_detail_api'
    ),
    path(
        '<int:client_id>/',
        views.ClientDetailAPIView.as_view(),
        name='client_detail_api'
    ),
    path(
        '<int:client_id>/delete/',
        views.ClientDeleteAPIView.as_view(),
        name='client_delete_api'
    ),
    path(
        '<int:client_id>/update/',
        views.ClientUpdateAPIView.as_view(),
        name='client_update_api'
    ),
]
