from sqlalchemy import create_engine, MetaData, Table, inspect
import mysql.connector

# create engine to connect to MySQL
engine = create_engine('mysql+mysqlconnector://julien:jupwd@0.0.0.0:3306/classicmodels')

inspector = inspect(engine)


table_names = inspector.get_table_names()

print("-------------------", "TABLE DISPONIBLES", sep="\n")
print(table_names)

def displayTableColumns(tabName):
	print("-------------------", "COLONNES DE LA TABLE "+tabName.upper(), sep="\n")
	columns = inspector.get_columns(tabName)
	for column in columns:
		print(f"{column['name']}: {column['type']}")

def displayQuery(title, query):
	print("-------------------", "QUERY", sep="\n")
	print(title, "-----", sep="\n")
	with engine.connect() as conn:
		result = conn.execute(query)
		for row in result:
		    print(row)

for name in table_names:
	displayTableColumns(name)

title1 = "liste de bureaux triés par pays, état, ville."
query1 = """
SELECT officeCode, country, state, city 
FROM offices
ORDER BY country, state, city
"""

displayQuery(title1, query1)

title2 = "Combien d'employés y a-t-il dans l'entreprise ?"
query2 = """
SELECT count(customerNumber) FROM customers
"""

displayQuery(title2, query2)

title3 = "Quel est le total des paiements reçus ?"
query3 = """
SELECT sum(amount) FROM payments
"""

displayQuery(title3, query3)

title4 = "Dressez la liste des lignes de produits contenant des 'Voitures'."
query4 = """
SELECT p.productCode, p.productName
FROM products as p
WHERE LOWER(p.productLine) LIKE '%cars%'
"""

displayQuery(title4, query4)

print("FIN DES QUERY")
# create metadata object
metadata = MetaData()
