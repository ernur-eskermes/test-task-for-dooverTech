from rest_framework import serializers

from ..models import User, Client, UserAddress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }


class ClientCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = (
            'id',
            'user',
            'phone',
            'avatar'
        )

    def create(self, validated_data):
        user_data = validated_data['user']
        user = User.objects.create(
            username=user_data['username'],
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
        )
        user.set_password(user_data['password'])
        user.save()

        client = Client.objects.create(
            user=user,
            avatar=validated_data['avatar'],
            phone=validated_data['phone']
        )
        return client


class ClientDetailSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'avatar',
            'phone',
            'bonus',
        )
        extra_kwargs = {
            'bonus': {"read_only": True}
        }

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name


class ClientUpdateSerializer(ClientDetailSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = (
            'id',
            'user',
            'avatar',
            'bonus',
            'phone',
        )
        extra_kwargs = {
            'bonus': {"read_only": True}
        }

    def update(self, instance, validated_data):
        for key, value in validated_data.pop('user').items():
            setattr(instance.user, key, value)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.user.save()
        instance.save()
        return instance


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = (
            'id',
            'street',
            'city',
            'state',
            'zipcode',
        )
