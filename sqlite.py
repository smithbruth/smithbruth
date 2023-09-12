import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
        movieID TEXT PRIMARY KEY,
        movieName TEXT,
        movieYear INTEGER,
        imdbRating REAL
    )
''')

# Create an empty list named stephen_king_adaptations_list
stephen_king_adaptations_list = []

# Read the file and insert data into the list
with open("stephen_king_adaptations.txt", "r") as file:
    for line in file:
        adaptation = line.strip().split(',')
        try:
            # Convert imdbRating to a floating-point number
            adaptation[3] = float(adaptation[3])
            stephen_king_adaptations_list.append(adaptation)  # Add data to the list
        except ValueError as e:
            print(f"Error inserting data: {e}")
            print(f"Error data: {adaptation}")

# Insert data from the list into the database table
for adaptation in stephen_king_adaptations_list:
    try:
        cursor.execute("INSERT INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating) VALUES (?, ?, ?, ?)", adaptation)
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
        print(f"Error data: {adaptation}")

conn.commit()

# User interaction
while True:  #while loop
    print("\nOptions:")
    print("1. Movie Name")
    print("2. Movie Year")
    print("3. Movie Rating")
    print("4. Quit")
    
    option = input("Select an option: ")
    
    if option == '4':
        print("Goodbye!")
        break
    
    if option in ['1', '2', '3']:
        search_term = input("Enter the search term: ")
        
        if option == '1':
            results = [result for result in stephen_king_adaptations_list if search_term.lower() in result[1].lower()]
        elif option == '2':
            results = [result for result in stephen_king_adaptations_list if search_term == str(result[2])]
        elif option == '3':
            try:
                rating_limit = float(search_term)
                results = [result for result in stephen_king_adaptations_list if result[3] >= rating_limit]
            except ValueError:
                print("Invalid rating limit.")
                continue
        
        if results:
            for result in results:
                print(f"Movie ID: {result[0]}, Movie Name: {result[1]}, Year: {result[2]}, Rating: {result[3]}")
        else:
            print("No matching movies found.")
    else:
        print("Invalid option. Please select a valid option (1-4).")

conn.close()
