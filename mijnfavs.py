import sys, sqlite3, random, csv

class functions():
	def __init__(self):
		try:
			self.db_connection = sqlite3.connect("mijnfavorieten.db")
			self.db_cursor = self.db_connection.cursor()
		except Exception as e:
			print(f"Error making connection to database: {e}")
			sys.exit(-1)


	def showall(self):
		try:
			my_query = "SELECT * FROM Mijnfavorietendb"
			self.db_cursor.execute(my_query)
			rows = self.db_cursor.fetchall()  # Fetch all rows
			for row in rows:
				print(row)
		except Exception as e:
			print(f"Error fetching data in showall: {e}")

	def feelrandom(self):
		try:
			my_query = "SELECT Name FROM Mijnfavorietendb"
			self.db_cursor.execute(my_query)
			rows = self.db_cursor.fetchall()
			randChoice = random.choice(rows)
			print(randChoice)
		except Exception as e:
			print(f"Error fetching random choice: {e}")

	def addGame(self, name, year):
		try:
			my_query = "INSERT INTO Mijnfavorietendb (Name, Yearstarted) VALUES (?, ?)"
			self.db_cursor.execute(my_query, (name, year))
			self.db_connection.commit()
			print("Game succesfully added")
		except Exception as e:
			print(f"Error adding to database: {e}")
			sys.exit(-1)

	def changeName(self, name, newname):
		try:
			my_query = "UPDATE Mijnfavorietendb SET Name = ? WHERE Name = ?"
			self.db_cursor.execute(my_query, (newname, name))
			self.db_connection.commit()
			print("Name succesfully Changed")
		except Exception as e:
			print(f"Error changing name: {e}")
			sys.exit(-1)

	def changeYear(self, name, year, newyear):
		try:
			my_query = "UPDATE Mijnfavorietendb SET Yearstarted = ? WHERE Yearstarted = ?"
			self.db_cursor.execute(my_query, (newyear, year))
			self.db_connection.commit()
			print("Year succesfully Changed")
		except Exception as e:
			print(f"Error changing year: {e}")
			sys.exit(-1)

	def exportToCSV(self):
		filename="report.csv"
		my_query = "SELECT * FROM Mijnfavorietendb"
		self.db_cursor.execute(my_query)
		rows = self.db_cursor.fetchall()

		column_names = [description[0] for description in self.db_cursor.description]

		print(column_names)
		print(rows)

		try:
			with open(filename, mode='w') as file:
				writer = csv.writer(file)
				writer.writerow(column_names)
				writer.writerow(rows)
			print(f"Report successfully saved. The filename is {filename}")
		except Exception as e:
			print(f"Error writing to CSV file: {e}")
			sys.exit(-1)

if __name__ == '__main__':
	functions = functions()

	print("----------ALL----------")
	functions.showall()
	print("----------RANDOM CHOICE----------")
	functions.feelrandom()

	print("----------CSV----------")
	functions.exportToCSV()

	"""
	!!!!WERKT!!!!
	print("----------ADD----------")
	functions.addGame("testgame", 2020)

	print("----------UPDATE----------")
	functions.changeName('testgame', 'Assetto Corsa')
	functions.changeYear('Assetto Corsa', 2020, 2018)
	"""