from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Snack
from .permissions import IsReviewerOrReadOnly
from .serializers import SnackSerializer


class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsReviewerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
