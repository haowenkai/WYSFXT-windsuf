from rest_framework import serializers
from .models import PaymentSummary
from apps.charges.models import ChargeRecord
from apps.properties.models import Property

class PaymentSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSummary
        fields = [
            'id', 'date', 'total_amount', 'paid_amount',
            'pending_amount', 'overdue_amount', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

class PropertyStatsSerializer(serializers.Serializer):
    total_properties = serializers.IntegerField()
    occupied_count = serializers.IntegerField()
    vacant_count = serializers.IntegerField()
    occupation_rate = serializers.FloatField()

    def to_representation(self, instance):
        total = Property.objects.count()
        occupied = Property.objects.filter(status='occupied').count()
        vacant = Property.objects.filter(status='vacant').count()
        rate = (occupied / total * 100) if total > 0 else 0
        
        return {
            'total_properties': total,
            'occupied_count': occupied,
            'vacant_count': vacant,
            'occupation_rate': round(rate, 2)
        }

class ChargeStatsSerializer(serializers.Serializer):
    total_charges = serializers.DecimalField(max_digits=12, decimal_places=2)
    paid_charges = serializers.DecimalField(max_digits=12, decimal_places=2)
    pending_charges = serializers.DecimalField(max_digits=12, decimal_places=2)
    overdue_charges = serializers.DecimalField(max_digits=12, decimal_places=2)
    collection_rate = serializers.FloatField()

    def to_representation(self, instance):
        total = ChargeRecord.objects.aggregate(
            total=models.Sum('amount'))['total'] or 0
        paid = ChargeRecord.objects.filter(
            status='paid').aggregate(
            paid=models.Sum('amount'))['paid'] or 0
        pending = ChargeRecord.objects.filter(
            status='pending').aggregate(
            pending=models.Sum('amount'))['pending'] or 0
        overdue = ChargeRecord.objects.filter(
            status='overdue').aggregate(
            overdue=models.Sum('amount'))['overdue'] or 0
        
        rate = (paid / total * 100) if total > 0 else 0
        
        return {
            'total_charges': total,
            'paid_charges': paid,
            'pending_charges': pending,
            'overdue_charges': overdue,
            'collection_rate': round(rate, 2)
        }

class ComprehensiveReportSerializer(serializers.Serializer):
    property_stats = PropertyStatsSerializer()
    charge_stats = ChargeStatsSerializer()
    latest_payment = PaymentSummarySerializer()

    def to_representation(self, instance):
        # 获取最新的支付摘要
        latest_payment = PaymentSummary.objects.order_by('-date').first()
        
        return {
            'property_stats': PropertyStatsSerializer().to_representation(None),
            'charge_stats': ChargeStatsSerializer().to_representation(None),
            'latest_payment': PaymentSummarySerializer(latest_payment).data if latest_payment else None
        }
