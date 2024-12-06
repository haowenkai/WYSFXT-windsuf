from django.urls import path
from . import views

app_name = 'charges'

urlpatterns = [
    # 收费类别管理
    path('categories/', views.ChargeCategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.ChargeCategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/', views.ChargeCategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.ChargeCategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.ChargeCategoryDeleteView.as_view(), name='category_delete'),
    
    # 收费记录管理
    path('records/', views.ChargeRecordListView.as_view(), name='record_list'),
    path('records/create/', views.ChargeRecordCreateView.as_view(), name='record_create'),
    path('records/<int:pk>/', views.ChargeRecordDetailView.as_view(), name='record_detail'),
    path('records/<int:pk>/update/', views.ChargeRecordUpdateView.as_view(), name='record_update'),
    path('records/<int:pk>/delete/', views.ChargeRecordDeleteView.as_view(), name='record_delete'),
]
