import PyPDF2
from urllib.parse import unquote
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .funcsions import extract_func
from .models import UploadedPDF
from .serializers import PDFUploadedSerializer

class PDFUploadView(APIView):
    def post(self, request, format=None):
        serializer = PDFUploadedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'id': serializer.instance.id,
                'file': unquote(serializer.instance.file.url),
                'uploaded_at': serializer.instance.uploaded_at.strftime('%Y-%m-%d %H:%M:%S'),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PDFStructureExtractorView(APIView):
    def get(self, request, pdf_id, format=None):
        pdf_instance = get_object_or_404(UploadedPDF, id=pdf_id)
        pdf_path = pdf_instance.file.path

        # extract_structure funksiyasini chaqirish
        structure = extract_func(pdf_path)

        return Response({
            'id': pdf_instance.id,
            'file': unquote(pdf_instance.file.url),
            'uploaded_at': pdf_instance.uploaded_at.isoformat(),
            'structure': structure
        }, status=status.HTTP_200_OK)