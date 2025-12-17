import pandas as pd; import sqlite3

# Connect to the SQLite database (this will create the file if it doesn't exist)
connection = sqlite3.connect('lecture19.db'); cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS players;')
cursor.execute('''
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT, player_name TEXT NOT NULL UNIQUE,
    goals INT NOT NULL, victories INT NOT NULL
);
''')

cursor.execute('DROP TABLE IF EXISTS teams;')
cursor.execute('''
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT, team_name TEXT NOT NULL
);
''')
connection.commit() # Commit changes

# Insert data into the tables
cursor.execute('''
INSERT INTO players (player_name, goals, victories) VALUES
('Messi', 10, 5),
('Vini Jr', 8, 4),
('Neymar', 6, 3),
('Mbappé', 5, 2),
('Lewandowski', 4, 1),
('Haaland', 5, 3);
''')

cursor.execute('''
INSERT INTO teams (team_name) VALUES
('Inter Miami'),
('Real Madrid'),
('Santos'),
('Real Madrid'),
('Barcelona');
''')
connection.commit() # Commit changes

pd.read_sql('SELECT * FROM players', connection)

pd.read_sql('SELECT * FROM teams', connection)

pd.read_sql('''
SELECT players.player_name, teams.team_name, players.goals, players.victories
FROM players
INNER JOIN teams
ON players.player_id = teams.team_id;
''', connection)

pd.read_sql('''
SELECT players.player_name, teams.team_name, players.goals
FROM players
LEFT JOIN teams
ON players.player_id = teams.team_id;
''', connection)

pd.read_sql('''
SELECT players.player_name, teams.team_name, players.goals
FROM teams
LEFT JOIN players
ON players.player_id = teams.team_id;
''', connection)

pd.read_sql('''
SELECT players.player_id, players.player_name, teams.team_name, players.goals
FROM players
LEFT JOIN teams
ON players.player_id = teams.team_id

UNION

SELECT players.player_id, players.player_name, teams.team_name, players.goals
FROM teams
LEFT JOIN players
ON players.player_id = teams.team_id
ORDER BY players.player_id;
''', connection)

# Create the tables and insert data
cursor.execute('DROP TABLE IF EXISTS reviews;') 
cursor.execute('DROP TABLE IF EXISTS products;')
cursor.execute('''
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL 
);
''')

# Insert products
cursor.execute('''
INSERT INTO products (product_name, price) VALUES
    ('Coffee Maker', 99.99),
    ('Toaster', 29.99),
    ('Blender', 79.99),
    ('Microwave', 149.99),
    ('Air Fryer', 89.99);
''')

cursor.execute('''
CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
''')

# Insert reviews
cursor.execute('''
INSERT INTO reviews (product_id, rating, comment) VALUES
    (1, 5, 'Great coffee maker!'),
    (1, 4, 'Good but expensive'),
    (2, 3, 'Average toaster'),
    (3, 5, 'Best blender ever');
''')
connection.commit()
print("Tables 'products' and 'reviews' created and populated.")

# Displaying cross join between players and teams
pd.read_sql('''
SELECT players.player_name, teams.team_name
FROM players
CROSS JOIN teams
ORDER BY players.player_id, teams.team_id;
''', connection)

# Drop and recreate tables
cursor.execute('DROP TABLE IF EXISTS colours;')
cursor.execute('DROP TABLE IF EXISTS sizes;')
cursor.execute('CREATE TABLE colours (colour_name TEXT);')
cursor.execute('CREATE TABLE sizes (size_code TEXT);')
cursor.execute("INSERT INTO colours VALUES ('Black'), ('Red');")
cursor.execute("INSERT INTO sizes VALUES ('S'), ('M');")
connection.commit()

# Perform cross join and concatenate strings using ||
pd.read_sql('''
SELECT colours.colour_name, sizes.size_code, colours.colour_name || ' - ' || sizes.size_code as t_shirt
FROM colours
CROSS JOIN sizes
ORDER BY colours.colour_name, sizes.size_code DESC;
''', connection)

cursor.execute('DROP TABLE IF EXISTS family;')
cursor.execute('''
CREATE TABLE family (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mother_id INT 
);
''')

cursor.execute('''
INSERT INTO family (name, mother_id) VALUES
    ('Emma', NULL), -- grandmother (id 1)
    ('Sarah', 1),   -- Emma's daughter (id 2)
    ('Lisa', 1),    -- Emma's daughter (id 3)
    ('Tom', 2),     -- Sarah's son (id 4)
    ('Alice', 2);   -- Sarah's daughter (id 5)
''')
connection.commit()

pd.read_sql('SELECT * FROM family;', connection)

# Self join to find child-mother pairs
pd.read_sql('''
SELECT children.name as child, mothers.name as mother
FROM family AS children
JOIN family AS mothers ON children.mother_id = mothers.person_id
ORDER BY mothers.name;
''', connection)

pd.read_sql('''
SELECT
    p1.player_name,
    p1.goals,
    p2.player_name as compared_to,
    p2.goals as their_goals,
    p1.goals - p2.goals as difference
FROM players AS p1
JOIN players AS p2
ON p1.player_id < p2.player_id -- Avoid duplicates and self-comparison
ORDER BY difference DESC;
''', connection)

# UNION example: Different categories for different criteria
pd.read_sql('''
SELECT player_name, goals, victories, 'Elite Scorer' as category
FROM players
WHERE goals > 9

UNION

SELECT player_name, goals, victories, 'Team Leader' as category
FROM players
WHERE victories > 2 AND goals < 10

ORDER BY category, player_name;
''', connection)

# UNION ALL keeps all rows, including duplicates if a player meets both criteria.
print(pd.read_sql('''
SELECT player_name, goals, victories, 'High Scorer (>7)' AS category
FROM players
WHERE goals > 7

UNION ALL

SELECT player_name, goals, victories, 'Many Victories (>3)' AS category
FROM players
WHERE victories > 3

ORDER BY player_name, category;
''', connection))

# Create the two separate tables for our example
cursor.execute('DROP TABLE IF EXISTS TopSpenders;')
cursor.execute('CREATE TABLE TopSpenders (customer_name TEXT);')
cursor.execute("INSERT INTO TopSpenders VALUES ('Alice'), ('Bob'), ('David');")

cursor.execute('DROP TABLE IF EXISTS FrequentShoppers;')
cursor.execute('CREATE TABLE FrequentShoppers (customer_name TEXT);')
cursor.execute("INSERT INTO FrequentShoppers VALUES ('Bob'), ('Charlie'), ('David');")
connection.commit()

# Now, find the customers who are in BOTH lists
print(pd.read_sql('''
    SELECT customer_name FROM TopSpenders
    
    INTERSECT
    
    SELECT customer_name FROM FrequentShoppers;
''', connection))

print(pd.read_sql('''
    SELECT customer_name FROM TopSpenders
    
    EXCEPT
    
    SELECT customer_name FROM FrequentShoppers;
''', connection))

# Messi already exists, and he has 10 goals and 5 victories
# We will insert him again with 2 more goals and 1 more victory
cursor.execute(""" 
INSERT INTO players (player_name, goals, victories) 
VALUES ('Messi', 2, 1) 
ON CONFLICT(player_name) DO UPDATE SET 
    goals = goals + excluded.goals,
    victories = victories + excluded.victories;
""")

pd.read_sql('SELECT * FROM players', connection)

# Drop the view if it exists
cursor.execute('DROP VIEW IF EXISTS player_stats;')

# Create the view
cursor.execute('''
CREATE VIEW player_stats AS
SELECT player_name, SUM(goals) AS total_goals, SUM(victories) AS total_victories
FROM players
GROUP BY player_name;
''')
connection.commit()

pd.read_sql('SELECT * FROM player_stats LIMIT 4', connection)

# Drop the view if it already exists to avoid errors on re-run
cursor.execute('DROP VIEW IF EXISTS colour_size;')

# Create the view using cursor.execute()
cursor.execute('''
CREATE VIEW colour_size AS
SELECT
    c.colour_name,
    s.size_code,
    c.colour_name || ' - ' || s.size_code as t_shirt -- Use || for concatenation
FROM colours AS c
CROSS JOIN sizes AS s
ORDER BY c.colour_name, s.size_code DESC;
''')
connection.commit() # Commit the view creation

# Now showcase the view by querying it with pandas
pd.read_sql('SELECT * FROM colour_size;', connection)

print("INNER JOIN Results (Only products with reviews):")
# INNER JOIN only includes products that have at least one review.
# Products like 'Microwave' and 'Air Fryer' are excluded.
print(pd.read_sql('''
    SELECT p.product_name, r.rating, r.comment
    FROM products p
    INNER JOIN reviews r ON p.product_id = r.product_id
    ORDER BY p.product_id, r.review_id; -- Added review_id for consistent ordering
''', connection))

print("\nLEFT JOIN Results (All products, reviews where available):")
print(pd.read_sql('''
    SELECT p.product_name, r.rating, r.comment
    FROM products p
    LEFT JOIN reviews r ON p.product_id = r.product_id
    ORDER BY p.product_id, r.review_id;
''', connection))

print("Self Join on Players to Compare Victories:")
print(pd.read_sql('''
SELECT
    p1.player_name,
    p1.victories,
    p2.player_name AS compared_to,
    p2.victories AS their_victories,
    -- Ensure floating point division by casting one operand to REAL or NUMERIC
    ROUND(CAST(p1.victories AS REAL) / p2.victories, 2) AS victories_ratio
FROM players p1
JOIN players p2
    ON p1.player_id < p2.player_id -- Avoid duplicates and self-comparison
WHERE
    p2.victories > 0 -- Avoid division by zero
ORDER BY
    p1.player_id, p2.player_id; -- Consistent ordering
''', connection))

# Ensure the connection is closed first
try:
    connection.close()
    print("SQLite connection closed.")
except Exception as e:
    print(f"Error closing connection (might be already closed): {e}")