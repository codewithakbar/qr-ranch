import os
import uuid
import qrcode
import base64

from io import BytesIO
from PIL import Image

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage


from home.serializers import MaktablarSerializer
from .models import Maktablar



class MaktablarQRCodeAPIView(viewsets.ModelViewSet):
    queryset = Maktablar.objects.all()
    serializer_class = MaktablarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



def home_page(request):

    return render(request, "home.html")