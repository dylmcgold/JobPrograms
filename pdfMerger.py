from pypdf import PdfMerger
from cvRegex import x
import os


pdfs = ['your_resume_here.pdf', 'xvar.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

directory_path = "CoverLetters"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

merger.write(f"{directory_path}/{x} Res_CV - Your Name Here.pdf")
merger.close()
os.remove("xvar.pdf")