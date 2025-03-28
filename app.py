from flask import Flask, render_template
import pandas as pd
from winningCells import q1_scores, q2_scores, q3_scores, q4_scores, find_target_cell, above_cell, below_cell

app = Flask(__name__)

import pandas as pd

def excel_to_html_table(file_path):
    try:
        # Read Excel file into DataFrame, skipping the first row
        df = pd.read_excel(file_path, skiprows=1)
        df = df.iloc[:, 2:]  # Remove first two columns

        df.columns = df.columns.str.replace(r'\.\d+', '', regex=True)  # Remove .1, .2, etc.
        df.columns = df.columns.str.replace('Unnamed: 2', '')

        # Remove newline characters from text columns
        df = df.apply(lambda col: col.str.replace('\n', ' ') if col.dtype == 'object' else col)

        # Function to add classes to name and number
        def add_classes_to_row(row):
            first_number = True  # Track the first number in the row
            new_row = []

            for cell in row:
                if isinstance(cell, str):
                    parts = cell.split()
                    if parts[-1].isdigit():
                        name = ' '.join(parts[:-1])  # Extract name
                        number = parts[-1]  # Extract number
                        if first_number:
                            new_row.append(f'<span class="name">{name}</span> <span class="first-number">{number}</span>')
                            first_number = False
                        else:
                            new_row.append(f'<span class="name">{name}</span> <span class="number">{number}</span>')
                    else:
                        new_row.append(f'<span class="name">{cell}</span>')

                elif isinstance(cell, (int, float)):  # Handle numeric cells
                    if first_number:
                        new_row.append(f'<span class="afc-number">{cell}</span>')
                        first_number = False
                    else:
                        new_row.append(f'<span class="number">{cell}</span>')
                else:
                    new_row.append(cell)

            return new_row

        # Apply function row-wise and convert back to a DataFrame
        df = pd.DataFrame(df.apply(add_classes_to_row, axis=1).tolist(), columns=df.columns)

        # Convert DataFrame to HTML and wrap the table with a div
        html_table = df.to_html(classes="data", index=False, escape=False)

        return html_table

    except Exception as e:
        return f"Error reading Excel file: {str(e)}"




@app.route("/")
def index():
    file_path = "boxesTest.xlsx"  # Ensure this path is correct
    html_content = excel_to_html_table(file_path)
    
    return render_template("index.html", html_content=html_content)

@app.route('/how-to-win')  # URL path
def how_to_win():  
    return render_template('howToWin.html')  # Template file

@app.route('/winners')  # URL path
def winners():
    with app.test_client() as client:
        response = client.get('/')
        html_data = response.data

    #nfcN1, afcN1, nfcA1, afcA1 = q1_scores()
    
    
    q1_result = q1_scores()
    q2_result = q2_scores()
    q3_result = q3_scores()
    q4_result = q4_scores()

    if q1_result == "TBD":
        return render_template('winners.html', 
            q1WinnerBoxNormal="TBD",
            q1WinnerBoxAdded="TBD",
            q2WinnerBoxNormal="TBD",
            q2WinnerBoxAdded="TBD",
            q2WinnerBoxAbove="TBD",
            q2WinnerBoxBelow="TBD",
            q3WinnerBoxNormal="TBD",
            q3WinnerBoxAdded="TBD",
            q4WinnerBoxNormal="TBD",
            q4WinnerBoxAdded="TBD",
            q4WinnerBoxAbove="TBD",
            q4WinnerBoxBelow="TBD",
            q4WinnerBoxPlusTouchdown="TBD",
            q4WinnerBoxCombinedScores="TBD"
        )
    elif q2_result == "TBD":
        nfcN1, afcN1, nfcA1, afcA1 = q1_scores()
        return render_template('winners.html', 
            q1WinnerBoxNormal=find_target_cell(html_data, nfcN1, afcN1),
            q1WinnerBoxAdded=find_target_cell(html_data, nfcA1, afcA1),
            q2WinnerBoxNormal="TBD",
            q2WinnerBoxAdded="TBD",
            q2WinnerBoxAbove="TBD",
            q2WinnerBoxBelow="TBD",
            q3WinnerBoxNormal="TBD",
            q3WinnerBoxAdded="TBD",
            q4WinnerBoxNormal="TBD",
            q4WinnerBoxAdded="TBD",
            q4WinnerBoxAbove="TBD",
            q4WinnerBoxBelow="TBD",
            q4WinnerBoxPlusTouchdown="TBD",
            q4WinnerBoxCombinedScores="TBD"
        )
    elif q3_result == "TBD":
        nfcN1, afcN1, nfcA1, afcA1 = q1_scores()
        nfcN2, afcN2, nfcA2, afcA2 = q2_scores()
        return render_template('winners.html',
            q1WinnerBoxNormal=find_target_cell(html_data, nfcN1, afcN1),
            q1WinnerBoxAdded=find_target_cell(html_data, nfcA1, afcA1),
            q2WinnerBoxNormal=find_target_cell(html_data, nfcN2, afcN2),
            q2WinnerBoxAdded=find_target_cell(html_data, nfcA2, afcA2),
            q2WinnerBoxAbove=above_cell(html_data, nfcN2, afcN2),
            q2WinnerBoxBelow=below_cell(html_data, nfcN2, afcN2),
            q3WinnerBoxNormal="TBD",
            q3WinnerBoxAdded="TBD",
            q4WinnerBoxNormal="TBD",
            q4WinnerBoxAdded="TBD",
            q4WinnerBoxAbove="TBD",
            q4WinnerBoxBelow="TBD",
            q4WinnerBoxPlusTouchdown="TBD",
            q4WinnerBoxCombinedScores="TBD"
        )
    elif q4_result == "TBD":
        nfcN1, afcN1, nfcA1, afcA1 = q1_scores()
        nfcN2, afcN2, nfcA2, afcA2 = q2_scores()
        nfcN3, afcN3, nfcA3, afcA3 = q3_scores()
        return render_template('winners.html', 
            q1WinnerBoxNormal=find_target_cell(html_data, nfcN1, afcN1),
            q1WinnerBoxAdded=find_target_cell(html_data, nfcA1, afcA1),
            q2WinnerBoxNormal=find_target_cell(html_data, nfcN2, afcN2),
            q2WinnerBoxAdded=find_target_cell(html_data, nfcA2, afcA2),
            q2WinnerBoxAbove=above_cell(html_data, nfcN2, afcN2),
            q2WinnerBoxBelow=below_cell(html_data, nfcN2, afcN2),
            q3WinnerBoxNormal=find_target_cell(html_data, nfcN3, afcN3),
            q3WinnerBoxAdded=find_target_cell(html_data, nfcA3, afcA3),
            q4WinnerBoxNormal="TBD",
            q4WinnerBoxAdded="TBD",
            q4WinnerBoxAbove="TBD",
            q4WinnerBoxBelow="TBD",
            q4WinnerBoxPlusTouchdown="TBD",
            q4WinnerBoxCombinedScores="TBD"
        )
    else:
        nfcN1, afcN1, nfcA1, afcA1 = q1_scores()
        nfcN2, afcN2, nfcA2, afcA2 = q2_scores()
        nfcN3, afcN3, nfcA3, afcA3 = q3_scores()
        nfcN4, afcN4, nfcA4, afcA4, nfcT4, afcT4, nfcC4, afcC4 = q4_scores()
        return render_template('winners.html', 
            q1WinnerBoxNormal=find_target_cell(html_data, nfcN1, afcN1),
            q1WinnerBoxAdded=find_target_cell(html_data, nfcA1, afcA1),
            q2WinnerBoxNormal=find_target_cell(html_data, nfcN2, afcN2),
            q2WinnerBoxAdded=find_target_cell(html_data, nfcA2, afcA2),
            q2WinnerBoxAbove=above_cell(html_data, nfcN2, afcN2),
            q2WinnerBoxBelow=below_cell(html_data, nfcN2, afcN2),
            q3WinnerBoxNormal=find_target_cell(html_data, nfcN3, afcN3),
            q3WinnerBoxAdded=find_target_cell(html_data, nfcA3, afcA3),
            q4WinnerBoxNormal=find_target_cell(html_data, nfcN4, afcN4),
            q4WinnerBoxAdded=find_target_cell(html_data, nfcA4, afcA4),
            q4WinnerBoxAbove=above_cell(html_data, nfcN4, afcN4),
            q4WinnerBoxBelow=below_cell(html_data, nfcN4, afcN4),
            q4WinnerBoxPlusTouchdown=find_target_cell(html_data, nfcT4, afcT4),
            q4WinnerBoxCombinedScores=find_target_cell(html_data, nfcC4, afcC4)
        )
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

    
    

