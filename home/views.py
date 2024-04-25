import os
import uuid
import qrcode
import base64

from io import BytesIO
from PIL import Image

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage


from home.serializers import MaktablarSerializer
from .models import Maktablar



class MaktablarQRCodeAPIView(APIView):
    def get(self, request, slug):
        maktab = get_object_or_404(Maktablar, slug=slug)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data("https://youtube.com/")
        # qr.add_data(request.build_absolute_uri())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format='PNG')
        
        buffer.seek(0)
        
        # Fayl nomini generatsiya qilish
        filename = f"qr-{maktab.slug}.png"
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        
        # Agar avvalgi versiya mavjud bo'lsa, o'chiramiz
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # Faylni saqlash
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filepath = fs.save(filename, buffer)
        image_url = fs.url(filepath)
        
        serializer = MaktablarSerializer(maktab)
        # Javobda rasmlar uchun URL-ni qo'shamiz
        return Response({'maktab': serializer.data, 'qr_image_url': image_url}, status=status.HTTP_200_OK)