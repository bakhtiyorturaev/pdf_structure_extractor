# extract_structure.py

import PyPDF2

def extract_func(pdf_path):
    structure = {}
    current_chapter = None
    current_section = None

    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num].extract_text()
            if not page:  # Agar sahifadan matn olinmasa davom eting
                continue

            lines = page.split("\n")
            for line in lines:
                line = line.strip()

                # Boblarni aniqlash
                if line.startswith("Глава") or line.startswith("Chapter"):
                    chapter_number = line.split()[1]  # Bob raqamini olish
                    current_chapter = chapter_number
                    structure[current_chapter] = {"title": line, "sections": {}}

                # Kichik bo'limlarni aniqlash
                elif current_chapter and line:
                    # Raqamlarni to'g'ri aniqlash
                    if line and line[0].isdigit() and line[1] == '.':
                        section_number = line.split()[0].strip('»').strip()
                        current_section = section_number
                        structure[current_chapter]["sections"][current_section] = {
                            "title": line,
                            "subsections": {}
                        }
                    elif current_section:
                        # Kichik bo'limlar
                        if current_section in structure[current_chapter]["sections"]:
                            subsection_number = f"{current_section}.{len(structure[current_chapter]['sections'][current_section]['subsections']) + 1}"
                            structure[current_chapter]["sections"][current_section]["subsections"][subsection_number] = {
                                "title": line
                            }
                        else:
                            print(f"Warning: current_section '{current_section}' not found in structure.")

    return structure
