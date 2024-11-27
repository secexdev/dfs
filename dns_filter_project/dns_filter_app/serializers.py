from rest_framework import serializers
from .models import Blocklist, DNSLog
from django.contrib.auth.models import User

# Blocklist Serializer
class BlocklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocklist
        fields = ['id', 'domain', 'category', 'blocked']

# DNS Log Serializer
class DNSLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSLog
        fields = ['id', 'domain', 'timestamp', 'action_taken', 'user']
