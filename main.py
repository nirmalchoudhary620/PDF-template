from fpdf import FPDF
import pandas as pd

# Initialize a PDF object with Portrait orientation, millimeter units, and A4 size
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Turn off automatic page breaks to control layout manually
pdf.set_auto_page_break(auto=False, margin=0)

# Load topic data from a CSV file (must contain 'Topic' and 'Pages' columns)
df = pd.read_csv("topics.csv")

# Loop through each topic in the DataFrame
for index, row in df.iterrows():
    # Add the first page for the current topic
    pdf.add_page()

    # Set font for the topic title (Times, Bold, size 30)
    pdf.set_font(family="Times", style="B", size=30)
    pdf.set_text_color(0, 0, 0)  # Black text

    # Write the topic title at the top-left corner and move to the next line
    pdf.cell(w=0, h=18, txt=row["Topic"], align="L", ln=1)

    # Draw horizontal lines across the page to simulate writing lines
    for y in range(25, 285, 10):  # Start from Y=25 to Y=275 with 10mm spacing
        pdf.line(10, y, 200, y)   # Line from left (x=10) to right (x=200)

    # Set Y-position for the footer line (just above page bottom)
    footer_y = 285

    # Draw a horizontal line above the footer text
    pdf.line(10, footer_y, 200, footer_y)

    # Move the cursor to the footer position
    pdf.set_y(footer_y)

    # Set font and color for the footer (Times Italic, grey color)
    pdf.set_font(family="Times", style="I", size=15)
    pdf.set_text_color(100, 100, 100)

    # Write the topic name in the footer, aligned to the right
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Add additional pages if the topic spans more than one page
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Draw writing lines on the additional page
        for y in range(25, 285, 10):
            pdf.line(10, y, 200, y)

        # Footer setup for the additional page
        footer_y = 285
        pdf.line(10, footer_y, 200, footer_y)
        pdf.set_y(footer_y)
        pdf.set_font(family="Times", style="I", size=15)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Generate and save the final PDF file
pdf.output("output.pdf")
