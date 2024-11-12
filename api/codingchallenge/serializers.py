from rest_framework import serializers

from codingchallenge.models import Event


class EventRaceDataSerializer(serializers.Serializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())

    def to_representation(self, instance):
        event = instance
        if isinstance(instance, dict):
            event = instance["event"]

        data = []
        return {"id": event.pk, "name": event.name, "data": data}
