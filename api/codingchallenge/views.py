from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response

from codingchallenge.models import Event
from codingchallenge.serializers import EventRaceDataSerializer


class EventRaceDataViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Event.objects.all()
    serializer_class = EventRaceDataSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, pk=None):
        retrieve_serializer = self.get_serializer_class()
        s = retrieve_serializer(
            data={"event": pk},
            context={"request": request},
        )
        if s.is_valid():
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
