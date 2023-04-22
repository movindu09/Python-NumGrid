from prettytable import PrettyTable
from datetime import datetime
import random 
import sys

# Ask the user to input the dimensions of the grid
# Get the command line arguments
if len(sys.argv) > 1:
    param = sys.argv[1]
    rows, cols = param.split("x")

    # Get the number of rows and columns from the arguments
    num_rows = int(rows)
    num_cols = int(cols)

else:
  num_rows = 5
  num_cols = 5
  print("Please Enter a Grid value between 3x3 and 9x9, below grid a default grid (eg: 3x4)")

if num_rows > 9 or num_cols > 9 or num_rows < 3 or num_cols < 3:
  print("Enter Grid values between 3x3 and 9x9")

else:
  # Create the grid as an array with empty cells
  grid = [[ "" for _ in range(num_cols)] for _ in range(num_rows)]

  # Generate random numbers and empty cells in the grid
  for x in range(num_rows):
    for y in range(num_cols):
      if random.random() > 0.12:
        grid[x][y] = random.randint(10, 99)

  # Create a pretty table for the grid
  table = PrettyTable()
  for row in grid:
    table.add_row(row)

  # Create a list to store the results for each column
  column_results = []

  # Go through each column in the grid and each cell in the column
  for y in range(num_cols):
    column_empty = False
    
    for x in range(num_rows):
      if not grid[x][y]:
        column_empty = True
        break

    # Append "OK" to the column_results list if the column is not empty, else append "NO"
    if not column_empty:
      column_results.append("OK")
    else:
      column_results.append("NO")

  # Append the column_results as a new row in the grid
  grid.append(column_results)

  # Create a pretty table from the grid
  table = PrettyTable()
  for row in grid:
    table.add_row(row)
    
  table.hrules = 1
  table.header = False

# Print the table
print(table)

#Save the output as a new file every time it runs with date and time
timestamp = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
with open("output_" + timestamp + ".txt", "w") as x:
  print(table, file=x)

# Get the HTML representation of the table
html = table.get_html_string(attributes={'border': 1,'style': 'text-align:center; '+"Horizontal: "})

# Write the HTML to a file
with open("output_" + timestamp + ".html", "w") as f:
  f.write(html)