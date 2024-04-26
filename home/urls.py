from django.urls import path, include
from .views import MaktablarQRCodeAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'maktablar', MaktablarQRCodeAPIView)

urlpatterns = [
    path('', include(router.urls)),
]