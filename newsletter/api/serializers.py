from rest_framework.serializers import ModelSerializer

from .models import Newsletter, Message


class NewsletterSerializer(ModelSerializer):

    class Meta:
        model = Newsletter
        fields = '__all__'


class MessageSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = '_all__'
