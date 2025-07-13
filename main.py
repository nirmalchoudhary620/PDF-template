from fpdf import FPDF
import pandas as pd

# Create a PDF object with Portrait orientation, millimeter units, and A4 paper size
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Disable automatic page breaks to manually control layout
pdf.set_auto_page_break(auto=False, margin=0)

# Read data from a CSV file, which should contain "Topic" and "Pages" columns
df = pd.read_csv("topics.csv")

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Add the first page for the current topic
    pdf.add_page()

    # Set font for the topic title (Times Bold, size 24)
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)  # Set text color to black

    # Write the topic title at the top-left and move to the next line
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Draw a horizontal line below the title (Y = 21 mm)
    pdf.line(10, 21, 200, 21)

    # Define Y-position for the footer (a bit above the bottom of the page)
    footer_y = 285

    # Draw a line just above the footer text
    pdf.line(10, footer_y, 200, footer_y)

    # Position the cursor to footer Y-position
    pdf.set_y(footer_y)

    # Set footer font (Times Italic, size 15) and grey color
    pdf.set_font(family="Times", style="I", size=15)
    pdf.set_text_color(100, 100, 100)

    # Display the topic name in the footer, aligned to the right
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Create additional blank pages for the topic (if more than 1 page)
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Repeat footer setup on each additional page
        footer_y = 285
        pdf.line(10, footer_y, 200, footer_y)
        pdf.set_y(footer_y)
        pdf.set_font(family="Times", style="I", size=15)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Export the final PDF to a file named "output.pdf"
pdf.output("output.pdf")
