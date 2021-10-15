from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.ProfileAPIView.as_view(), name="profile-detail")
]
