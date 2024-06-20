from sec_edgar_downloader import Downloader
import os
from docx import Document
import PyPDF2

# Provide a name and email for identification (can be placeholders)
name = "John Doe"
email = "john.doe@example.com"

# Initialize the downloader with the provided name and email
downloader = Downloader(name, email)

# Define the ticker symbol or company name for the filings you want to search for
ticker = "AAPL"

# Search for 10-K filings for the specified ticker symbol and download them to a directory
downloaded_filings_dir = downloader.get("10-K", ticker, download_details=False)

# List the files in the downloaded directory
downloaded_files = os.listdir(downloaded_filings_dir)

# Loop through each downloaded file
for file_name in downloaded_files:
    file_path = os.path.join(downloaded_filings_dir, file_name)

    # Parse the filing based on its file type
    _, extension = os.path.splitext(file_name)
    if extension == ".docx":
        # Parse Word document (docx)
        doc = Document(file_path)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    elif extension == ".pdf":
        # Parse PDF document
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            text = "\n".join(
                reader.getPage(page_num).extractText()
                for page_num in range(reader.numPages)
            )
    else:
        # Handle other file types
        # You may need to use other libraries or techniques based on the file type
        text = "Unable to parse filing of type {}".format(extension)

    # Convert to Markdown format
    markdown_filename = os.path.splitext(file_name)[0] + ".md"
    with open(os.path.join("markdown", markdown_filename), "w") as md_file:
        md_file.write(f"## {file_name}\n\n")
        md_file.write(text)

    # Print Markdown file path
    print(f"Markdown file saved: {os.path.join('markdown', markdown_filename)}")
