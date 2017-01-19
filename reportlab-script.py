import glob
from reportlab.pdfgen import canvas

# Collect all the maps 
map_images = glob.glob("map_imgs\\*.png")

# Generate PDF file
c = canvas.Canvas("filename.pdf")

for m in map_images:
	c.drawImage(m, 10, 10)
	c.showPage()

c.save()
print 'Done! Check your working directory for the generated pdf file.'

