from rest_framework import serializers
from .models import ChargeCategory, ChargeRecord
from apps.properties.serializers import PropertySerializer

class ChargeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargeCategory
        fields = [
            'id', 'name', 'description', 'unit_price', 
            'unit', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_unit_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("单价必须大于0")
        return value

class ChargeRecordSerializer(serializers.ModelSerializer):
    property_detail = PropertySerializer(source='property', read_only=True)
    category_detail = ChargeCategorySerializer(source='category', read_only=True)
    
    class Meta:
        model = ChargeRecord
        fields = [
            'id', 'property', 'property_detail',
            'category', 'category_detail',
            'amount', 'billing_date', 'due_date',
            'status', 'payment_date', 'remark',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        # 验证账单日期和截止日期
        if data['billing_date'] > data['due_date']:
            raise serializers.ValidationError("账单日期不能晚于截止日期")
        
        # 验证支付日期（如果有）
        payment_date = data.get('payment_date')
        if payment_date and payment_date < data['billing_date']:
            raise serializers.ValidationError("支付日期不能早于账单日期")
            
        return data

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("金额必须大于0")
        return value
