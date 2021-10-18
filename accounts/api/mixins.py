import sys
import traceback

from django.http import HttpResponseForbidden
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class OnlyClientMixin(APIView):
    """Проверяет, относятся ли получаемые или
    отправляемые данные к текущему юзеру """

    def get(self, request, *args, **kwargs):
        try:
            if self.request.user.is_superuser:
                return super().get(request, *args, **kwargs)
            if not self.request.user.is_authenticated or \
                    kwargs.get('client_id') and \
                    str(self.request.user.client.pk) != kwargs['client_id']:
                return HttpResponseForbidden()
            return super().get(request, *args, **kwargs)
        except BaseException as e:
            print(e, '\n', traceback.extract_tb(sys.exc_info()[2]))
            if e.__class__ == serializers.ValidationError:
                raise e
            return Response(str(e))

    def post(self, request, *args, **kwargs):
        try:
            has_access = self.has_access(request)
            if not has_access[0]:
                return has_access[1]
            return super().post(request, *args, **kwargs)
        except BaseException as e:
            print(e, '\n', traceback.extract_tb(sys.exc_info()[2]))
            if e.__class__ == serializers.ValidationError:
                raise e
            return Response(str(e))

    def put(self, request, *args, **kwargs):
        try:
            has_access = self.has_access(request)
            if not has_access[0]:
                return has_access[1]
            return super().put(request, *args, **kwargs)
        except BaseException as e:
            print(e, '\n', traceback.extract_tb(sys.exc_info()[2]))
            if e.__class__ == serializers.ValidationError:
                raise e
            return Response(str(e))

    def patch(self, request, *args, **kwargs):
        try:
            has_access = self.has_access(request)
            if not has_access[0]:
                return has_access[1]
            return super().patch(request, *args, **kwargs)
        except BaseException as e:
            print(e, '\n', traceback.extract_tb(sys.exc_info()[2]))
            if e.__class__ == serializers.ValidationError:
                raise e
            return Response(str(e))

    def has_access(self, request):
        if self.request.user.is_superuser:
            return True, None
        data = self.request.data
        if not self.request.user.is_authenticated or \
                data.get('client_id') and \
                str(self.request.user.client.pk) != data['client_id']:
            return False, HttpResponseForbidden()
        return True, None
