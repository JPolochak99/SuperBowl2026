from bs4 import BeautifulSoup

# Read the HTML file
with open("templates/index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first table
table = soup.find('table')

if table:
    # If a table is found, extract rows
    rows = table.find_all('tr')  # Find all rows in the table

    # Iterate through rows
    for row in rows:
        cells = row.find_all(['th', 'td'])  # Find all cells in the row
        row_data = [cell.text.strip() for cell in cells]  # Extract and clean cell data
        print(row_data)  # Print the row data
else:
    print("No table found in index.html")