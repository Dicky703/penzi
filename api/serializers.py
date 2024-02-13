from rest_framework import serializers
from .models import Message, Users

class PenziMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'message_from', 'message_to', 'message_content', 'timestamp']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'age', 'gender', 'county', 'town', 'level_of_education',
                  'profession', 'marital_status', 'religion', 'ethnicity', 
                  'description', 'myself', 'msisdn', 'registration_time']