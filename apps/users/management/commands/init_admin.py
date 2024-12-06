from django.core.management.base import BaseCommand
from apps.users.models import User

class Command(BaseCommand):
    help = '创建初始管理员用户'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                role='admin'
            )
            self.stdout.write(self.style.SUCCESS('成功创建管理员用户'))
        else:
            self.stdout.write(self.style.WARNING('管理员用户已存在'))
