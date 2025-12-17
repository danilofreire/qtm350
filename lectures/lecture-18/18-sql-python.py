"""
SQLite and Python - Code Examples
=================================
This script contains all the Python code examples from the Quarto presentation
on SQLite and Python integration for QTM 350 - Data Science Computing.
"""

# Import required libraries
import sqlite3
import pandas as pd
import os

# =============================================================================
# CONNECTING SQLITE WITH PYTHON
# =============================================================================

# Database filename
db_file = 'lecture18.db'

# 1. Connect to the database (creates file if needed)
conn = sqlite3.connect(db_file)

# 2. Create a cursor object to execute commands
cur = conn.cursor()

# =============================================================================
# CREATING TABLES
# =============================================================================

# Use triple quotes for multi-line SQL
# Drop table if exists 
sql_drop = '''
DROP TABLE IF EXISTS drivers; 
'''

# Execute the SQL command
cur.execute(sql_drop)

# Create a new table named 'drivers'
sql_create = '''
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_name TEXT,
    team TEXT,
    nationality TEXT,
    victories INTEGER
);
'''
# Execute the SQL command
cur.execute(sql_create)

# Commit the transaction to save the table
conn.commit() 

# Check if the table was created
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='drivers';")

# =============================================================================
# INSERTING DATA
# =============================================================================

# Insert a few rows
cur.execute("INSERT INTO drivers (driver_name, team, nationality, victories) VALUES ('Lewis Hamilton', 'Mercedes', 'British', 103);")
cur.execute("INSERT INTO drivers (driver_name, team, nationality, victories) VALUES ('Max Verstappen', 'Red Bull Racing', 'Dutch', 55);")
cur.execute("INSERT INTO drivers (driver_name, team, nationality, victories) VALUES ('Fernando Alonso', 'Aston Martin', NULL, NULL);")
cur.execute("INSERT INTO drivers (driver_name, team, nationality) VALUES ('Charles Leclerc', 'Ferrari', 'Monégasque');") 

# Commit the insertions
conn.commit()

# =============================================================================
# FETCHING RESULTS
# =============================================================================

# Fetch all results at once
cur.execute('SELECT driver_id, driver_name, team FROM drivers') 
all_rows = cur.fetchall() # Get the list of tuples

# Print the fetched data
print("--- All drivers ---")
for row in all_rows:
    print(row) 

# Fetch one result at a time
cur.execute('SELECT driver_id, driver_name FROM drivers ORDER BY driver_id')

row1 = cur.fetchone()
print("\n--- First row ---")
print(row1) # First row

row2 = cur.fetchone()
print("\n--- Second row ---")
print(row2) # Second row

# Iterate over the cursor (more Pythonic and memory-efficient)
query = "SELECT driver_name, team FROM drivers WHERE driver_name LIKE 'M%'"
print("\n--- Drivers with names starting with M ---")
for row_tuple in cur.execute(query):
     print(row_tuple) 

# =============================================================================
# FILTERING DATA WITH IN, NOT IN, BETWEEN, AND NOT BETWEEN
# =============================================================================

# Use IN to check if a column's value matches any value in a specified list
query_in = "SELECT driver_name, team FROM drivers WHERE team IN ('Ferrari', 'Mercedes')" 
cur.execute(query_in)
print("\n--- Drivers from Ferrari or Mercedes ---")
for row in cur.fetchall():
    print(row)

# NOT IN works similarly to exclude values in the list
query_not_in = "SELECT driver_name, team FROM drivers WHERE team NOT IN ('Ferrari', 'Mercedes')" 
cur.execute(query_not_in)
print("\n--- Drivers not from Ferrari or Mercedes ---")
for row in cur.fetchall():
    print(row)

# BETWEEN checks if a value is within a specified range (inclusive of endpoints)
query_between = "SELECT driver_name, victories FROM drivers WHERE victories BETWEEN 10 AND 60" 
cur.execute(query_between)
print("\n--- Drivers with 10-60 victories ---")
for row in cur.fetchall():
    print(row)

# =============================================================================
# PATTERN MATCHING WITH LIKE
# =============================================================================

# Starts with 'L'
print("\n--- Drivers whose names start with L ---")
cur.execute("SELECT driver_name FROM drivers WHERE driver_name LIKE 'L%'")
for row in cur.fetchall(): print(row)

# Ends with 'Racing'
print("\n--- Teams ending with 'Racing' ---")
cur.execute("SELECT team FROM drivers WHERE team LIKE '%Racing'")
for row in cur.fetchall(): print(row)

# 'a' as the second letter 
print("\n--- Drivers with 'a' as second letter ---")
cur.execute("SELECT driver_name FROM drivers WHERE driver_name LIKE '_a%'")
for row in cur.fetchall(): print(row)

# Case-insensitive search using LOWER()
print("\n--- Case-insensitive search for names starting with 'l' ---")
cur.execute("SELECT driver_name FROM drivers WHERE LOWER(driver_name) LIKE 'l%'")
for row in cur.fetchall(): print(row)

# Case-insensitive search using COLLATE NOCASE
print("\n--- Case-insensitive search using COLLATE NOCASE ---")
cur.execute("SELECT driver_name FROM drivers WHERE driver_name LIKE 'l%' COLLATE NOCASE")
for row in cur.fetchall(): print(row)

# =============================================================================
# HANDLING MISSING DATA (NULL VALUES)
# =============================================================================

# Find NULL values
print("\n--- Drivers with NULL victories ---")
cur.execute("SELECT driver_name, victories FROM drivers WHERE victories IS NULL")
for row in cur.fetchall(): print(row)

# Use COALESCE to replace NULL with a default value
print("\n--- Replace NULL victories with 0 ---")
cur.execute("SELECT driver_name, COALESCE(victories, 0) AS victories_filled FROM drivers")
for row in cur.fetchall(): print(row)

# COALESCE with subquery for dynamic default value
query_coalesce_sub = '''
SELECT driver_name,
  COALESCE(victories, 
    -- Subquery calculates average victories from non-NULL rows
    (SELECT CAST(AVG(victories) AS INTEGER) 
     FROM drivers 
     WHERE victories IS NOT NULL) 
  ) AS victories_imputed
FROM drivers; 
''' 
cur.execute(query_coalesce_sub)
print("\n--- Replace NULL victories with average of non-NULL victories ---")
for row in cur.fetchall(): print(row)

# =============================================================================
# WINDOW FUNCTIONS
# =============================================================================

# Add more data 
more_drivers_data = [
    ('Valtteri Bottas', 'Mercedes', 'Finnish', 10),
    ('Sergio Perez', 'Red Bull Racing', 'Mexican', 5),
    ('Lando Norris', 'McLaren', 'British', 2),
    ('Esteban Ocon', 'Alpine', 'French', 1) 
]

# Check if data already exists to avoid duplicates 
cur.execute("SELECT COUNT(*) FROM drivers WHERE driver_name = 'Valtteri Bottas'")
if cur.fetchone()[0] == 0: # Not found
    cur.executemany('INSERT INTO drivers (driver_name, team, nationality, victories) VALUES (?, ?, ?, ?)', more_drivers_data)
    conn.commit()
    print(f"\nAdded {len(more_drivers_data)} more drivers.")
else:
    print("\nAdditional drivers already exist.")

# Check SQLite Version
cur.execute("SELECT sqlite_version();")
print(f"SQLite Version: {cur.fetchone()[0]}")

# Window functions: AVG and RANK
query_window_avg_rank = '''
SELECT 
    driver_name, team, victories,
    ROUND(AVG(victories) OVER (), 2) AS avg_overall, 
    ROUND(AVG(victories) OVER (PARTITION BY team), 2) AS avg_team, 
    RANK() OVER (ORDER BY victories DESC) AS rank_overall 
FROM drivers
WHERE victories IS NOT NULL 
ORDER BY rank_overall; 
'''
cur.execute(query_window_avg_rank)
print("\n--- Window functions: AVG and RANK ---")
for row in cur.fetchall(): print(row)

# Window functions vs. GROUP BY
# GROUP BY example (summarizes)
cur.execute("SELECT team, ROUND(AVG(victories), 2) FROM drivers WHERE victories IS NOT NULL GROUP BY team")
print("\n--- GROUP BY Output ---")
for row in cur.fetchall(): print(row)

# Window Function example (adds detail to each row)
cur.execute('''
    SELECT driver_name, team, victories, 
           ROUND(AVG(victories) OVER (PARTITION BY team), 2) as avg_in_team
    FROM drivers 
    WHERE victories IS NOT NULL ORDER BY team, victories DESC
''')
print("\n--- Window Function Output ---")
for row in cur.fetchall(): print(row)

# =============================================================================
# STRING MANIPULATIONS
# =============================================================================

# Basic string functions
query_str1 = '''
SELECT driver_name, 
    LENGTH(driver_name) AS len,
    UPPER(driver_name) AS upper,
    LOWER(driver_name) AS lower,
    SUBSTR(driver_name, 1, 4) AS first_four -- Get first 4 characters
FROM drivers LIMIT 4;
'''
cur.execute(query_str1)
print("\n--- Basic string functions ---")
for row in cur.fetchall(): print(row)

# More string functions
query_str2 = '''
SELECT driver_name, 
    REPLACE(driver_name, ' ', '_') AS replaced_space,
    INSTR(LOWER(driver_name), 'a') AS first_a_pos, 
    'Driver: ' || driver_name AS labelled_name -- Concatenation
FROM drivers LIMIT 4;
'''
cur.execute(query_str2)
print("\n--- More string functions ---")
for row in cur.fetchall(): print(row)

# =============================================================================
# CONDITIONAL LOGIC WITH CASE
# =============================================================================

# Basic CASE statement
query_case1 = '''
SELECT driver_name, victories,
    CASE 
        WHEN victories > 50 THEN 'Legend' 
        ELSE 'Great Driver (or N/A)'     
    END AS category 
FROM drivers;
'''
cur.execute(query_case1)
print("\n--- Basic CASE statement ---")
for row in cur.fetchall(): print(row)

# CASE with multiple conditions
query_case2 = '''
SELECT driver_name, victories,
    CASE 
        WHEN victories > 100 THEN 'All-Time Great'
        WHEN victories > 50 THEN 'Legend'
        WHEN victories >= 10 THEN 'Race Winner'
        WHEN victories > 0 THEN 'Podium Potential'
        ELSE 'Data Missing or Zero Wins' 
    END AS status
FROM drivers ORDER BY victories DESC NULLS LAST;
'''
cur.execute(query_case2)
print("\n--- CASE with multiple conditions ---")
for row in cur.fetchall(): print(row)

# CASE for conditional NULL handling
query_case_null = '''
SELECT driver_name, 
    -- Fill nationality based on name if NULL
    CASE 
        WHEN nationality IS NULL AND driver_name = 'Fernando Alonso' THEN 'Spanish'
        WHEN nationality IS NULL THEN 'Unknown' 
        ELSE nationality
    END AS nationality_filled,
    -- Fill victories based on team if NULL
    CASE 
        WHEN victories IS NULL AND team = 'Aston Martin' THEN 32 -- Educated guess! 
        WHEN victories IS NULL THEN 0 
        ELSE victories
    END AS victories_filled
FROM drivers WHERE driver_name LIKE 'F%' OR driver_name LIKE 'L%'; -- Limit output
'''
cur.execute(query_case_null)
print("\n--- CASE for conditional NULL handling ---")
for row in cur.fetchall(): print(row)

# =============================================================================
# USING SQL WITH PANDAS
# =============================================================================

# Reading data with pandas.read_sql
df = pd.read_sql('SELECT * FROM drivers', conn) 
print("\n--- All drivers as pandas DataFrame ---")
print(df) 

# read_sql with any SELECT query
query_pd = """
SELECT driver_name, team, victories 
FROM drivers 
WHERE victories > 5 OR victories IS NULL
ORDER BY team
"""
df_filtered_ordered = pd.read_sql(query_pd, conn)
print("\n--- Filtered and ordered DataFrame ---")
print(df_filtered_ordered)

# Manipulating DataFrames from SQL
avg_vic_pd = df.groupby('team')['victories'].mean().dropna()
print("\n--- Average victories by team ---")
print(avg_vic_pd)

# Example using pandas .query() method for filtering
print("\n--- British drivers with >50 victories ---")
print(df.query('victories > 50 and nationality == "British"'))

# Writing DataFrames to SQL (to_sql)
# Create a DataFrame with British drivers
df_british = df[df['nationality'] == 'British'].copy()

# Write to a new table named 'british_drivers'
# index=False: Important! Prevents pandas index from becoming a DB column
df_british.to_sql('british_drivers', conn, if_exists='replace', index=False)

# Verify by reading it back using pandas
print("\n--- British drivers table ---")
print(pd.read_sql('SELECT * FROM british_drivers', conn))

# =============================================================================
# PIVOT TABLES IN SQL
# =============================================================================

# Create and populate student_scores table
cur.execute('DROP TABLE IF EXISTS student_scores;')
cur.execute('CREATE TABLE student_scores (student_name TEXT, subject TEXT, score INTEGER, term TEXT);')
scores_data = [
    ('Alice', 'Maths', 90, 'Q1'), ('Alice', 'Maths', 80, 'Q2'), ('Alice', 'Science', 80, 'Q1'), ('Alice', 'Science', 75, 'Q2'),
    ('Bob', 'Maths', 80, 'Q1'), ('Bob', 'Maths', 100, 'Q2'), ('Bob', 'Science', 80, 'Q1'), ('Bob', 'Science', 70, 'Q2'),
    ('Charles', 'Maths', 70, 'Q1'), ('Charles', 'Maths', 75, 'Q2'), ('Charles', 'Science', 90, 'Q1'), ('Charles', 'Science', 85, 'Q2')
]
cur.executemany('INSERT INTO student_scores VALUES (?, ?, ?, ?)', scores_data)
conn.commit()

# Display raw data using pandas
print("\n--- Raw student scores data ---")
print(pd.read_sql('SELECT * FROM student_scores ORDER BY student_name, term, subject', conn))

# Pivoting with CASE and GROUP BY
pivot_query = '''
SELECT 
    student_name,
    -- Avg Maths: Only average score WHEN subject is Maths
    AVG(CASE WHEN subject = 'Maths' THEN score END) as Avg_Maths, 
    -- Avg Science: Only average score WHEN subject is Science
    AVG(CASE WHEN subject = 'Science' THEN score END) as Avg_Science
FROM student_scores
GROUP BY student_name 
ORDER BY student_name;
'''
# Display the pivoted result using pandas
df_pivot = pd.read_sql(pivot_query, conn)
print("\n--- Pivoted student scores ---")
print(df_pivot)

# =============================================================================
# EXERCISE SOLUTIONS
# =============================================================================

# Exercise 01 Solutions
print("\n--- Exercise 01 Solutions ---")

# Find M names
cur.execute("SELECT * FROM drivers WHERE driver_name LIKE 'M%';")
print("--- Drivers starting with M ---")
for row in cur.fetchall(): print(row)

# Find 7 char nationalities
cur.execute("SELECT * FROM drivers WHERE LENGTH(nationality) = 7;")
print("\n--- Nationalities with 7 chars ---")
for row in cur.fetchall(): print(row)

# Find L or M names
cur.execute("SELECT * FROM drivers WHERE driver_name LIKE 'L%' OR driver_name LIKE 'M%';")
print("\n--- Drivers starting with L or M ---")
for row in cur.fetchall(): print(row)

# Find 1-10 wins
cur.execute("SELECT * FROM drivers WHERE victories BETWEEN 1 AND 10;")
print("\n--- Drivers with 1-10 wins ---")
for row in cur.fetchall(): print(row)

# Exercise 02 Solution
print("\n--- Exercise 02 Solution ---")

# Query and display using standard fetch
query_rank_nationality = '''
SELECT 
    driver_name, nationality, victories,
    RANK() OVER (PARTITION BY nationality ORDER BY victories DESC) AS rank_nationality
FROM drivers
WHERE victories IS NOT NULL 
ORDER BY nationality, rank_nationality; 
'''
cur.execute(query_rank_nationality)
print("\n--- Drivers ranked by victories within nationality ---")
for row in cur.fetchall(): print(row)

# Exercise 03 Solution
print("\n--- Exercise 03 Solution ---")

query_driver_level = '''
SELECT 
    driver_name, victories,
    CASE 
        WHEN victories IS NULL THEN 'Unknown' 
        WHEN victories > 50 THEN 'Expert'
        WHEN victories BETWEEN 10 AND 50 THEN 'Intermediate' 
        WHEN victories < 10 THEN 'Beginner' 
    END AS driver_level
FROM drivers
ORDER BY victories DESC NULLS LAST; 
'''
cur.execute(query_driver_level)
print("--- Driver classification using CASE ---")
for row in cur.fetchall(): print(row)

# Exercise 04 Solution
print("\n--- Exercise 04 Solution ---")

# 1. Create employees table
cur.execute('DROP TABLE IF EXISTS employees;') 
cur.execute('''
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT, department TEXT, salary INTEGER
);''')

# 2. Insert data
employee_data = [
    ('Alice', 'HR', 50000), ('Bob', 'IT', 60000),
    ('Charlie', 'HR', 70000), ('David', 'IT', 80000)
]
cur.executemany('INSERT INTO employees (employee_name, department, salary) VALUES (?, ?, ?)', employee_data)
conn.commit()
print("Employees table created and populated.")

# 3. Read data with pandas
df_employees = pd.read_sql('SELECT * FROM employees', conn)
print("\n--- Employees DataFrame ---")
print(df_employees)

# 4. Compute average salary by department using pandas
avg_salary_dept = df_employees.groupby('department')['salary'].mean()
print("\n--- Average salary by department (pandas) ---")
print(avg_salary_dept)

# =============================================================================
# CLEAN UP
# =============================================================================

# Clean up: Close the connection
if 'conn' in locals() and conn:
    conn.close()
    print("\nSQLite connection closed.")

# =============================================================================
# OPTIONAL: DATABASE CLEANING FUNCTIONS
# =============================================================================

def clean_database_file(db_path):
    """Option 1: Delete the database file"""
    if os.path.exists(db_path):
        try:
            # Ensure connection is closed first!
            os.remove(db_path)
            print(f"Deleted database file: {db_path}")
        except OSError as e:
            print(f"Error deleting file {db_path}: {e}")

def clean_database_tables(db_path):
    """Option 2: Drop all tables programmatically"""
    conn_clean = sqlite3.connect(db_path)
    cur_clean = conn_clean.cursor()
    cur_clean.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = cur_clean.fetchall()
    print(f"Tables to drop: {tables}")
    for table_name_tuple in tables:
        cur_clean.execute(f"DROP TABLE IF EXISTS {table_name_tuple[0]}")
        print(f"Dropped table: {table_name_tuple[0]}")
    conn_clean.commit()
    conn_clean.close()
    print("Finished dropping tables.")

# Uncomment to use the cleaning functions:
# clean_database_file(db_file)  # Option 1: Delete the file
# clean_database_tables(db_file)  # Option 2: Drop all tables