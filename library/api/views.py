from library.api.mixins import CustomListModelMixin
from rest_framework.generics import GenericAPIView


class CustomListAPIView(CustomListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
