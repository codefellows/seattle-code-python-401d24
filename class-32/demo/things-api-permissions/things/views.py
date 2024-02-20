from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Thing
from .serializers import ThingSerializer
from .permissions import IsOwnerOrReadOnly

class ThingList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    queryset = Thing.objects.all()

    #serializing
    serializer_class = ThingSerializer

# The ThingDetail needs the same things
class ThingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = (IsOwnerOrReadOnly,)
