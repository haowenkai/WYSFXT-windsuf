from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('summary/', views.PaymentSummaryView.as_view(), name='payment_summary'),
    path('property-stats/', views.PropertyStatsView.as_view(), name='property_stats'),
    path('charge-stats/', views.ChargeStatsView.as_view(), name='charge_stats'),
    path('export/excel/', views.ExportExcelView.as_view(), name='export_excel'),
    path('comprehensive/', views.ComprehensiveReportView.as_view(), name='comprehensive_report'),
]
