from django.db import models
from apps.charges.models import ChargeRecord

class PaymentSummary(models.Model):
    date = models.DateField(verbose_name='统计日期')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='总金额')
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='已缴金额')
    pending_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='待缴金额')
    overdue_amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='逾期金额')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '收费统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"收费统计 - {self.date}"
