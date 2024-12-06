from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChargeCategory, ChargeRecord
from .serializers import ChargeCategorySerializer, ChargeRecordSerializer

# 收费类别视图
class ChargeCategoryListView(generics.ListAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ChargeCategoryCreateView(generics.CreateAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    permission_classes = [permissions.IsAdminUser]

class ChargeCategoryDetailView(generics.RetrieveAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ChargeCategoryUpdateView(generics.UpdateAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    permission_classes = [permissions.IsAdminUser]

class ChargeCategoryDeleteView(generics.DestroyAPIView):
    queryset = ChargeCategory.objects.all()
    serializer_class = ChargeCategorySerializer
    permission_classes = [permissions.IsAdminUser]

# 收费记录视图
class ChargeRecordListView(generics.ListAPIView):
    serializer_class = ChargeRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = ChargeRecord.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(property__owner=self.request.user)
        return queryset

class ChargeRecordCreateView(generics.CreateAPIView):
    queryset = ChargeRecord.objects.all()
    serializer_class = ChargeRecordSerializer
    permission_classes = [permissions.IsAdminUser]

class ChargeRecordDetailView(generics.RetrieveAPIView):
    serializer_class = ChargeRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = ChargeRecord.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(property__owner=self.request.user)
        return queryset

class ChargeRecordUpdateView(generics.UpdateAPIView):
    queryset = ChargeRecord.objects.all()
    serializer_class = ChargeRecordSerializer
    permission_classes = [permissions.IsAdminUser]

class ChargeRecordDeleteView(generics.DestroyAPIView):
    queryset = ChargeRecord.objects.all()
    serializer_class = ChargeRecordSerializer
    permission_classes = [permissions.IsAdminUser]
