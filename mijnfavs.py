import sys, sqlite3, random, csv

class functions():
	def __init__(self):
		try:
			self.db_connection = sqlite3.connect("Database/mijnfavorieten.db")
			self.db_cursor = self.db_connection.cursor()
		except Exception as e:
			print(f"Error making connection to database: {e}")
			sys.exit(-1)

	def showAll(self):
		try:
			my_query = "SELECT * FROM Mijnfavorietendb"
			self.db_cursor.execute(my_query)
			rows = self.db_cursor.fetchall()  # Fetch all rows
			column_names = [description[0] for description in self.db_cursor.description]

			print(column_names)
			for row in rows:
				print(row)
		except Exception as e:
			print(f"Error fetching data in showall: {e}")

	def feelRandom(self):
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

	def changeYear(self, name, newyear):
		try:
			my_query = "UPDATE Mijnfavorietendb SET Yearstarted = ? WHERE Name = ?"
			self.db_cursor.execute(my_query, (newyear, name))
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

	print("----------CSV----------")
	functions.exportToCSV()

	validGeneral = False
	validDetail = False

	while(validGeneral == False):
		validGeneral = True
		choice = input("Options: r (read options), a (add something), u (update options), e (export to csv file): ")

		if(choice == "r"):
			while(validDetail == False):
				validDetail = True
				choice2 = input("a (see all entries), r (Random game): ")

				if(choice2 == "a"):
					functions.showAll()
				elif(choice2 == "r"):
					functions.feelRandom()
				else:
					print("Not a valid option")
					validDetail = False

		elif(choice == "a"):
			name = input("What is the name of the game?: ")
			year = input ("What is the year you started playing said game?: ")
			functions.addGame(name, year)
		elif(choice == "u"):
			while(validDetail == False):
				validDetail = True
				choice2 = input("n (change name), y (change year): ")

				if(choice2 == "n"):
					name = input("What is the current name of the game?: ")
					newname = input ("What is the name you want to change it to?: ")
					functions.changeName(name, newname)
				elif(choice2 == "y"):
					name = input("What is the name of the game?: ")
					year = input ("What is the year you want to change it to?: ")
					functions.changeName(name, year)
				else:
					print("Not a valid option")
					validDetail = False
		elif(choice == "e"):
			functions.exportToCSV()
		else:
			print("Not a valid option")
			validGeneral = False