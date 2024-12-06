from django.db import models
from apps.users.models import User

class Property(models.Model):
    STATUS_CHOICES = (
        ('occupied', '已入住'),
        ('vacant', '空置'),
    )
    
    building = models.CharField(max_length=50, verbose_name='楼栋号')
    unit = models.CharField(max_length=50, verbose_name='单元号')
    room = models.CharField(max_length=50, verbose_name='房间号')
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='面积(平方米)')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='业主')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='vacant', verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '房产信息'
        verbose_name_plural = verbose_name
        unique_together = ('building', 'unit', 'room')

    def __str__(self):
        return f"{self.building}-{self.unit}-{self.room}"
