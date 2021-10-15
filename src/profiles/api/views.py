from rest_framework.generics import RetrieveAPIView

from .serializers import ProfileSerializer
from ..models import Profile


class ProfileAPIView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
