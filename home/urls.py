from django.urls import path
from .views import MaktablarQRCodeAPIView

urlpatterns = [
    path('maktablar/<slug:slug>/', MaktablarQRCodeAPIView.as_view(), name='maktablar_qr_code'),
]
