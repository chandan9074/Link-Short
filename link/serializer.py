from rest_framework import serializers
from .models import Url

class URLSerializer(serializers.ModelSerializer):
    class Meta:

        model = Url
        fields = '__all__'
        extra_kwargs = {'short_link': {'required': False}, 'user_profile': {'required': False}, 'title': {'required': False}}


class EditURLSerializer(serializers.ModelSerializer):
    class Meta:

        model = Url
        fields = '__all__'
        extra_kwargs = {'given_link': {'required': False}, 'user_profile': {'required': False}, 'title': {'required': False}}



class RenderPublicURLSerializer(serializers.ModelSerializer):
    class Meta:

        model = Url
        fields = '__all__'
        extra_kwargs = {'given_link': {'required': False}, 'user_profile': {'required': False}, 'title': {'required': False}}


class UrlListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Url
        fields = '__all__'