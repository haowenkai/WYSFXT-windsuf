from django.db import models
from apps.properties.models import Property

class ChargeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='费用类别名称')
    description = models.TextField(blank=True, verbose_name='描述')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    unit = models.CharField(max_length=20, verbose_name='计费单位')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '收费类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ChargeRecord(models.Model):
    STATUS_CHOICES = (
        ('pending', '待缴费'),
        ('paid', '已缴费'),
        ('overdue', '已逾期'),
    )
    
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='房产')
    category = models.ForeignKey(ChargeCategory, on_delete=models.CASCADE, verbose_name='费用类别')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='金额')
    billing_date = models.DateField(verbose_name='账单日期')
    due_date = models.DateField(verbose_name='截止日期')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='状态')
    payment_date = models.DateField(null=True, blank=True, verbose_name='缴费日期')
    remark = models.TextField(blank=True, verbose_name='备注')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '收费记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.property} - {self.category} - {self.billing_date}"
