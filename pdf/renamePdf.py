from PyPDF2 import PdfFileReader
import os
import stat

allpdfs = []
for filename in os.listdir('./'):
    tmp = filename.split('.')
    if filename.split('.')[-1] == 'pdf':
        allpdfs.append(filename)

for pdffile in allpdfs:
    os.chmod(pdffile, 0o444)
    fp = open(pdffile, "rb")
    pdf = PdfFileReader(fp, strict = False, overwriteWarnings = False)
    count = pdf.getNumPages()
    fp.close()
    filename = str(count) + ' ' + pdffile
    os.rename(pdffile, filename)

