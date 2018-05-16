import decimal
import sqlite3

def adapt_currency(value):
    return str(value)
#register the function with sqlite
sqlite3.register_adapter(decimal.Decimal, adapt_currency)

#will be invode when reading from database
def convert_currency(bytes):
    return decimal.Decimal(bytes.decode())

sqlite3.register_converter("DECIMAL", convert_currency)

#now we can use DECIMAL as column type
decimal_ddl = """
CREATE TABLE financial(
year INTEGER,
month INTEGER,
category TEXT,
amount DECIMAL)
"""
#whatever is value of the DECIMAL will be saved as bytesin column decimal
#PRASE for DECIMAL TYPES is required for the connection
database = sqlite3.connect("adapting_decimal.db",
                           detect_types = sqlite3.PARSE_DECLTYPES)

crsr = database.cursor()
crsr.execute(decimal_ddl)

inserting = """
INSERT INTO financial(year, month, category, amount)
VALUES(:year, :month, :category , :amount)
"""
crsr.execute(inserting, dict(year = "2016", month="3", category="fuel",
                             amount = decimal.Decimal("33.23")))

query = """
SELECT * FROM financial
"""
for row in crsr.execute(query):
    print(row)


