import csv
import sqlite3

if __name__ == "__main__":
    # connect and create a database
    conn = sqlite3.connect("wines.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS  wines (name text, size text, price real, url text)"""
    )

    # open csv file
    with open("wines.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        item = next(csv_reader)
        for row in csv_reader:
            c.execute(
                "INSERT INTO wines VALUES (?, ?, ?, ?)",
                (row[0], row[1], row[2], row[3]),
            )

    conn.commit()
    conn.close()
