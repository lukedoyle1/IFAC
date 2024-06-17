# Import packages
import os
import PyPDF2

def pdf_to_text(pdf_path, output_txt):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Write the extracted text to a text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

def process_directory(pdf_dir, output_dir):
    # List all files in the directory
    files = os.listdir(pdf_dir)
    # Filter out PDF files
    pdf_files = [f for f in files if f.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        # Construct full file path
        pdf_path = os.path.join(pdf_dir, pdf_file)
        # Create output file name by replacing '.pdf' with '_txt.txt'
        output_txt_name = os.path.splitext(pdf_file)[0] + '_txt.txt'
        output_txt_path = os.path.join(output_dir, output_txt_name)

        # Process the PDF file
        pdf_to_text(pdf_path, output_txt_path)
        print(f'Processed: {pdf_file}')

# Example usage
pdf_dir = r"C:\Users\LukeDoyle\OneDrive - Irish Fiscal Advisory Council\Project\SPU\PDF"  # Replace with your PDF directory path
output_dir = r"C:\Users\LukeDoyle\OneDrive - Irish Fiscal Adv
isory Council\Project\SPU\txt"  

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process all PDF files in the directory
process_directory(pdf_dir, output_dir)

print('Run completed')






















# def pdf_to_text(pdf_path, output_txt):
#     # Open the PDF file in read-binary mode
#     with open(pdf_path, 'rb') as pdf_file:
#         # Create a PdfReader object instead of PdfFileReader
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Initialize an empty string to store the text
#         text = ''

#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             text += page.extract_text()

#     # Write the extracted text to a text file
#     with open(output_txt, 'w', encoding='utf-8') as txt_file:
#         txt_file.write(text)
        
# pdf_path = r"C:\Users\LukeDoyle\OneDrive - Irish Fiscal Advisory Council\Project\SPU\PDF\SPU 2023.pdf"  # Replace with your PDF file path
# output_txt = r"C:\Users\LukeDoyle\OneDrive - Irish Fiscal Advisory Council\Project\SPU\txt\output.txt"  # Replace with your desired output text file path



# pdf_to_text(pdf_path, output_txt)

# print('Run')
