from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("data/house_g.pdf")

styles = getSampleStyleSheet()

content = [
    Paragraph("House G has 7 bedrooms and 5 bathrooms.", styles["Normal"]),
    Paragraph("House G has 1 swimming pool.", styles["Normal"]),
    Paragraph("House G has 3 parking spaces.", styles["Normal"]),
    Paragraph("Garden area is 1200 square feet.", styles["Normal"]),
]

pdf.build(content)

print("PDF created successfully!")