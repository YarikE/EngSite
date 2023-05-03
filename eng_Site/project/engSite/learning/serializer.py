from rest_framework import serializers
from .models import BdWords


class WordsAPIserializer(serializers.ModelSerializer):
    class Meta:
        model = BdWords
        fields = ['word', 'trl_word']
