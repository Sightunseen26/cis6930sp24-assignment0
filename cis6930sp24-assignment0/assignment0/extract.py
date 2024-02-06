import re
import PyPDF2

def extractincidents(incident_data):
    incidents = []

    with open(incident_data, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Use regular expression to extract relevant information from each line
            pattern = re.compile(r'(\d{1,2}/\d{1,2}/\d{4}) (\d{1,2}:\d{2}) (\S+) (\S+.*) (\S+.*) (\S+)')
            matches = pattern.findall(page_text)

            for match in matches:
                date, time, incident_number, location, nature, incident_ori = match
                incidents.append((f'{date} {time}', incident_number, location, nature, incident_ori))

    return incidents
