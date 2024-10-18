
from django.urls import path

from .views import PDFUploadView, PDFStructureExtractorView


urlpatterns = [
    path('upload/', PDFUploadView.as_view(), name='upload_pdf'),
    path('extract/<int:pdf_id>/', PDFStructureExtractorView.as_view(), name='extract_structure_pdf')

]