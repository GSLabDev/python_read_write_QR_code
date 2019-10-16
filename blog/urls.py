from . import views
from django.urls import path

urlpatterns = [
    path('', views.CodeList.as_view(), name='home'),
    # path('<pk:pk>/', views.CodeDetail.as_view(), name='code_detail'),
    path('code/<int:pk>/', views.CodeDetail.as_view(), name='code_detail'),
    path('code/new/', views.code_new, name='code_new'),
    path('code/<int:pk>/edit/', views.code_edit, name='code_edit'),
    path('code/<int:pk>/decode_qr/', views.decode_qr, name='decode_qr'),
]
