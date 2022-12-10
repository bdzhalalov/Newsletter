from django.urls import path
from .views import NewsletterList

urlpatterns = [
    path('newsletter/', NewsletterList.as_view())
]