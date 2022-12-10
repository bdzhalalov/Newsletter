from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .models import Newsletter, Message
from .serializers import NewsletterSerializer, MessageSerializer


class PagePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'


@permission_classes((IsAuthenticated,))
class NewsletterList(ListCreateAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.prefetch_related('filter__tag')


def oauth(request):
    return render(request, 'oauth.html')

