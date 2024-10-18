# PDF Structure Extractor

PDF Structure Extractor is a project designed to extract information from PDF files using Python and Django. This project allows for the extraction of chapters, sections, and subsections from PDF files.

#Requirements

- Python 3.x
- Django 3.x or 4.x
- Django REST Framework
- PyPDF2
- PyCryptodome (if working with encrypted PDF files is necessary)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bakhtiyorturaev/pdf_structure_extractor.git
   cd pdf_structure_extractor




2. Create and activate a virtual environment:

python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows


3. Install the required packages:
 pip install -r requirements.txt

4. Running the Project:
 python manage.py runserver

5. Example:
 curl -X POST -F 'file=@/path/to/your/file.pdf' http://localhost:8000/api/upload/

