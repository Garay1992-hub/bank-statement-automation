import pandas as pd
import os

folder = "client_data"

if not os.path.exists(folder):
    os.makedirs(folder)

# Data for the first month (January)
january_data = {
    'Date': ['2026-01-05', '2026-01-12', '2026-01-15', '2026-01-20'],
    'Description': ['Incoming Transfer', 'Server Payment', 'Software Subscription', 'Consulting'],
    'Amount': [1500.00, -50.00, -29.99, 800.00]
}

# Data for the second month (February) - Intentional duplicate row on Jan 20
february_data = {
    'Date': ['2026-01-20', '2026-02-02', '2026-02-18'],
    'Description': ['Consulting', 'Office Rent', 'Incoming Transfer'],
    'Amount': [800.00, -400.00, 1200.00]
}

# Save as CSV files in the folder
pd.DataFrame(january_data).to_csv(f'{folder}/january_statement.csv', index=False)
pd.DataFrame(february_data).to_csv(f'{folder}/february_statement.csv', index=False)

print("Test files successfully generated in 'client_data' folder.")