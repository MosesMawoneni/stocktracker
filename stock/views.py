from rest_framework.viewsets import ModelViewSet
from .models import Issue, Item, StorePersonnelProfile, Worker
from .serializers import (
    IssuesSerializer,
    ItemShowAllSerializer,
    PersonnelSerializer,
    WorkerSerializer,
)


class ItemViewSet(ModelViewSet):
    serializer_class = ItemShowAllSerializer
    queryset = Item.objects.all()


class WorkerViewSet(ModelViewSet):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class IssueViewSet(ModelViewSet):
    serializer_class = IssuesSerializer
    queryset = Issue.objects.all()


class PersonnelViewSet(ModelViewSet):
    serializer_class = PersonnelSerializer
    queryset = StorePersonnelProfile.objects.all()
