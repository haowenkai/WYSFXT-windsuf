from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from .models import PaymentSummary
from .serializers import PaymentSummarySerializer, PropertyStatsSerializer, ChargeStatsSerializer, ComprehensiveReportSerializer
from apps.charges.models import ChargeRecord
from apps.properties.models import Property

class PaymentSummaryView(generics.ListCreateAPIView):
    queryset = PaymentSummary.objects.all()
    serializer_class = PaymentSummarySerializer
    permission_classes = [permissions.IsAdminUser]

class PropertyStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = PropertyStatsSerializer({})
        return Response(serializer.data)

class ChargeStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = ChargeStatsSerializer({})
        return Response(serializer.data)

class ComprehensiveReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = ComprehensiveReportSerializer({})
        return Response(serializer.data)

class ExportExcelView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        import pandas as pd
        from django.http import HttpResponse
        from io import BytesIO
        
        # 创建一个Excel写入器
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        
        # 导出收费记录
        charge_records = ChargeRecord.objects.all().values(
            'property__building', 'property__unit', 'property__room',
            'category__name', 'amount', 'status', 'billing_date', 'due_date'
        )
        df_charges = pd.DataFrame(charge_records)
        df_charges.to_excel(writer, sheet_name='收费记录', index=False)
        
        # 导出房产信息
        properties = Property.objects.all().values(
            'building', 'unit', 'room', 'area', 'status',
            'owner__username', 'owner__phone'
        )
        df_properties = pd.DataFrame(properties)
        df_properties.to_excel(writer, sheet_name='房产信息', index=False)
        
        # 保存Excel文件
        writer.close()
        output.seek(0)
        
        # 返回Excel文件
        response = HttpResponse(
            output.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=property_report.xlsx'
        return response
