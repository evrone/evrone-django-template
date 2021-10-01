from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.serializers import HealthSerializer


class HealthView(GenericAPIView):
    """
    PUBLIC METHOD.

    DESCRIPTION: Health check view.
    """

    serializer_class = HealthSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"})
