from bs4 import BeautifulSoup
import pandas as pd

def find_target_cell(html_data, nfcNum, afcNum):
    soup = BeautifulSoup(html_data, 'html.parser')

    nfcNum = str(nfcNum)
    afcNum = str(afcNum)

    # Find the table
    table = soup.find('table')
   
    row_index = None
    col_index = None
    target_cell_value = None

    
    if table:
        # Find column index (header row)
        header_row = table.find('tr')
        if header_row:
            cells = header_row.find_all(['th', 'td'])
            for idx, cell in enumerate(cells):
                if cell.text.strip() == nfcNum:
                    col_index = idx
                    break


        # Find row index (data rows)
        rows = table.find_all('tr')[1:]  # Skip header
        for row_idx, row in enumerate(rows):
            cells = row.find_all(['td', 'th'])
            for idx, cell in enumerate(cells):
                if cell.text.strip() == afcNum:
                    row_index = row_idx
                    break


        # Get the target cell
        if row_index is not None and col_index is not None:
            target_cell = rows[row_index].find_all('td')[col_index]
            target_cell_value = target_cell.text.strip()


    return target_cell_value

def above_cell(html_data, nfcNum, afcNum):
    soup = BeautifulSoup(html_data, 'html.parser')

    nfcNum = str(nfcNum)
    afcNum = str(afcNum)

    # Find the table
    table = soup.find('table')

    row_index = None
    col_index = None
    above_cell_value = None

    if table:
        # Find column index (header row)
        header_row = table.find('tr')
        if header_row:
            cells = header_row.find_all(['th', 'td'])
            for idx, cell in enumerate(cells):
                if cell.text.strip() == nfcNum:
                    col_index = idx
                    break

        # Find row index (data rows)
        rows = table.find_all('tr')[1:]  # Skip header row
        total_rows = len(rows)

        for row_idx, row in enumerate(rows):
            cells = row.find_all(['td', 'th'])
            for idx, cell in enumerate(cells):
                if cell.text.strip() == afcNum:
                    row_index = row_idx
                    break

        # If row_index is found, get the cell above it
        if row_index is not None and col_index is not None:
            prev_row_index = (row_index - 1) % total_rows  # Wrap to last row if at top
            target_cell = rows[prev_row_index].find_all('td')[col_index]
            above_cell_value = target_cell.text.strip()

    return above_cell_value

from bs4 import BeautifulSoup

def below_cell(html_data, nfcNum, afcNum):
    soup = BeautifulSoup(html_data, 'html.parser')

    nfcNum = str(nfcNum)
    afcNum = str(afcNum)

    # Find the table
    table = soup.find('table')
   
    row_index = None
    col_index = None
    below_cell_value = None

    if table:
        # Find column index (header row)
        header_row = table.find('tr')
        if header_row:
            cells = header_row.find_all(['th', 'td'])
            for idx, cell in enumerate(cells):
                if cell.text.strip() == nfcNum:
                    col_index = idx
                    break

        # Find row index (data rows)
        rows = table.find_all('tr')[1:]  # Skip header row
        total_rows = len(rows)

        for row_idx, row in enumerate(rows):
            cells = row.find_all(['td', 'th'])
            for idx, cell in enumerate(cells):
                if cell.text.strip() == afcNum:
                    row_index = row_idx
                    break

        # If row_index is found, get the cell below it
        if row_index is not None and col_index is not None:
            next_row_index = (row_index + 1) % total_rows  # Wrap around to top
            target_cell = rows[next_row_index].find_all('td')[col_index]
            below_cell_value = target_cell.text.strip()

    return below_cell_value


def q1_scores():
    info = pd.read_excel("boxesTest.xlsx", sheet_name="Sheet2")

    nfcQ1_normal = info.iloc[0,1]
    afcQ1_normal = info.iloc[1,1]

    if pd.isna(nfcQ1_normal) or pd.isna(afcQ1_normal):
        return 'TBD'
    
    nfcQ1_added = (nfcQ1_normal + 1) % 10
    afcQ1_added = afcQ1_normal + 1 % 10
    
    return(nfcQ1_normal, afcQ1_normal, nfcQ1_added, afcQ1_added)


def q2_scores():
    info = pd.read_excel("boxesTest.xlsx", sheet_name="Sheet2")

    nfcQ2_normal = info.iloc[0,2]
    afcQ2_normal = info.iloc[1,2]

    if pd.isna(nfcQ2_normal) or pd.isna(afcQ2_normal):
        return 'TBD' 
    
    nfcQ2_added = nfcQ2_normal + 1 % 10
    afcQ2_added = afcQ2_normal + 1 % 10

    return(nfcQ2_normal, afcQ2_normal, nfcQ2_added, afcQ2_added)
           
def q3_scores():
    info = pd.read_excel("boxesTest.xlsx", sheet_name="Sheet2")

    nfcQ3_normal = info.iloc[0,3]
    afcQ3_normal = info.iloc[1,3]

    if pd.isna(nfcQ3_normal) or pd.isna(afcQ3_normal):
        return 'TBD' 
    
    nfcQ3_added = nfcQ3_normal + 1 % 10
    afcQ3_added = afcQ3_normal +1 % 10

    return(nfcQ3_normal, afcQ3_normal, nfcQ3_added, afcQ3_added)

def q4_scores():
    # Read the Excel file
    info = pd.read_excel("boxesTest.xlsx", sheet_name="Sheet2")

    # Extract values
    nfcFinalNormal = info.iloc[0, 4]
    afcFinalNormal = info.iloc[1, 4]

    # Check if values are NaN
    if pd.isna(nfcFinalNormal) or pd.isna(afcFinalNormal):
        return 'TBD'

    # Perform calculations
    nfcFinal_added = (nfcFinalNormal + 1) % 10
    afcFinal_added = (afcFinalNormal + 1) % 10
    nfcPlusTouchdown = (nfcFinalNormal + 6) % 10
    afcPlusTouchdown = (afcFinalNormal + 6) % 10

    # Ensure column 5 values exist before performing operations
    if pd.isna(info.iloc[0, 5]) or pd.isna(info.iloc[1, 5]):
        return 'TDB'

    finalScoreCombined = (info.iloc[0, 5] + info.iloc[1, 5])
    nfcNumCombined = int((finalScoreCombined / 10) % 10)
    afcNumCombined = finalScoreCombined % 10

    return (
        nfcFinalNormal, afcFinalNormal,
        nfcFinal_added, afcFinal_added,
        nfcPlusTouchdown, afcPlusTouchdown,
        nfcNumCombined, afcNumCombined
    )
