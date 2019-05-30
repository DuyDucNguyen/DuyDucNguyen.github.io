# Reduce PDF size
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -sOutputFile=output.pdf input.pdf


# Options
#setting = '/screen' Quality level settings lowest resolution and lowest file size, but fine for viewing on a screen; 
#"/ebook," a mid-point in resolution and file size; 
#"/printer" and 
#"/prepress," high-quality settings used for printing PDFs.

# How to use: paste the comment in Terminal
