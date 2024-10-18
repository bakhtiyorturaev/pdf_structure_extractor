from rest_framework import serializers
from .models import UploadedPDF

class PDFUploadedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedPDF
        fields = ['id', 'file', 'uploaded_at']

