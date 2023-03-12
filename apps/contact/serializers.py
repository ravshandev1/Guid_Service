from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'contact_link', 'city', 'city_name', 'check_in_time', 'language_name',
                  'check_out_time', 'language', 'created_at']

    created_at = serializers.DateTimeField(read_only=True)
    city_name = serializers.CharField(read_only=True, source='city.name')
    language_name = serializers.CharField(read_only=True, source='language.name')
