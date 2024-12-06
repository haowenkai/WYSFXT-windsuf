from rest_framework import serializers
from .models import Property
from apps.users.serializers import UserSerializer

class PropertySerializer(serializers.ModelSerializer):
    owner_detail = UserSerializer(source='owner', read_only=True)
    
    class Meta:
        model = Property
        fields = [
            'id', 'building', 'unit', 'room', 'area', 
            'owner', 'owner_detail', 'status', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        # 验证房产信息的唯一性
        building = data.get('building')
        unit = data.get('unit')
        room = data.get('room')
        
        # 在更新时排除当前实例
        instance = self.instance
        if instance:
            exists = Property.objects.exclude(pk=instance.pk).filter(
                building=building,
                unit=unit,
                room=room
            ).exists()
        else:
            exists = Property.objects.filter(
                building=building,
                unit=unit,
                room=room
            ).exists()
            
        if exists:
            raise serializers.ValidationError("该房产已存在")
        return data
