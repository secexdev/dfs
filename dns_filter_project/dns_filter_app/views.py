from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Blocklist, DNSLog
from .serializers import BlocklistSerializer, DNSLogSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

# Blocklist Viewset
class BlocklistViewSet(viewsets.ModelViewSet):
    queryset = Blocklist.objects.all()
    serializer_class = BlocklistSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def toggle_block(self, request):
        domain = request.data.get('domain')
        try:
            block = Blocklist.objects.get(domain=domain)
            block.blocked = not block.blocked
            block.save()
            return Response({'status': 'domain block status updated'})
        except Blocklist.DoesNotExist:
            return Response({'error': 'Domain not found'}, status=400)

# DNS Log Viewset
class DNSLogViewSet(viewsets.ModelViewSet):
    queryset = DNSLog.objects.all()
    serializer_class = DNSLogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # This assumes the user is logged in
        serializer.save(user=self.request.user)
