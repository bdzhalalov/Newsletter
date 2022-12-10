from django.urls import path
from .views import NewsletterList, oauth

urlpatterns = [
    path('newsletter/', NewsletterList.as_view()),
    path('auth/', oauth),
]