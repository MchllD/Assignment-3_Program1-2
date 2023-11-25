import sqlite3

def create_tables():
    conn = sqlite3.connect('Product.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Fruits (
            id TEXT PRIMARY KEY, 
            name TEXT, 
            price INTEGER)''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vegetables (
            id TEXT PRIMARY KEY,
            name TEXT, 
            price INTEGER)''')
    
    conn.commit()
    conn.close()
    
def insert_products():
    conn = sqlite3.connect('Product.db')
    cursor = conn.cursor()
    
    fruits_data = [
        ( 'F1', 'Apple', 30),
        ( 'F2', 'Orange', 20),
        ( 'F3', 'Mango', 40)
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO Fruits (id, name, price) VALUES (?, ?, ?)', fruits_data)
    
    vegetables_data = [
       ('V1', 'Carrots', 25),
       ('V2', 'Potato', 25),
       ('V3', 'Cabbage', 30)
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO Vegetables (id, name, price) VALUES (?, ?, ?)', vegetables_data)

     
    conn.commit()
    conn.close()

def get_product_prices():
    conn = sqlite3.connect('Product.db')  
    cursor = conn.cursor()
    
    cursor.execute('SELECT price FROM Fruits')
    fruits_prices = [row[0] for row in cursor.fetchall()]
    
    cursor.execute('SELECT price FROM Vegetables')
    vegetables_prices = [row[0] for row in cursor.fetchall()]
    
    create_tables()
    prices = get_product_prices()
    print("Fruits Prices:", prices[0])
    print("Vegetables Prices:", prices[1])
    
    conn.close()
    insert_products()
    
    return fruits_prices, vegetables_prices




    
    
   
   