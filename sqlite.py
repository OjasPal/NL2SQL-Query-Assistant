import sqlite3

with sqlite3.connect("student.db") as connection:
    cursor = connection.cursor()

    table_info = """
        CREATE TABLE IF NOT EXISTS STUDENT (
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS INT
    );
    """

    cursor.execute(table_info)
    cursor.execute("DELETE FROM STUDENT")

    students = [
        ('Aryan', 'Machine Learning', 'A', 90),
        ('Siddharth', 'Software Development', 'D', 79),
        ('Chaitanya', 'Cybersecurity', 'B', 80),
        ('Vedya', 'Data Science', 'A', 100),
        ('Shivam', 'DevOps', 'C', 50),
        ('Gokul', 'Software Development', 'B', 75),
        ('Kavya', 'DevOps', 'D', 68),
        ('Ananya', 'Data Science', 'D', 95),
        ('Aarav', 'Cybersecurity', 'D', 82),
        ('Rohan', 'Machine Learning', 'D', 88)
    ]

    cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)

    print("The inserted records are: ")
    data = cursor.execute("SELECT * FROM STUDENT")
    for row in data:
        print(row)