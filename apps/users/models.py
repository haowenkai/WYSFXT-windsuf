from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', '管理员'),
        ('owner', '业主'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='owner', verbose_name='角色')
    phone = models.CharField(max_length=11, blank=True, verbose_name='联系电话')
    address = models.CharField(max_length=200, blank=True, verbose_name='联系地址')
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.username
