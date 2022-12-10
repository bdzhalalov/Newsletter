from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Client
from .serializers import ClientSerializer


class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'


@permission_classes((IsAuthenticated,))
class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = PagePagination

