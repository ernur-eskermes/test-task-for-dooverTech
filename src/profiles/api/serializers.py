from rest_framework import serializers

from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'avatar'
        )

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email
