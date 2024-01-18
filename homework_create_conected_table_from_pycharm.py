import mysql.connector

with open('password.txt', 'r') as password:
    password = password.read()

db_connector = mysql.connector.connect(host='localhost', user='root',
                                       password=password, database='my_db_2')

cursor = db_connector.cursor()

create_table_cars = """
    CREATE TABLE cars (
        carID int primary key auto_increment not null,
        car_model varchar(55)
    );
"""
create_table_area_city = """
    CREATE TABLE area_city (
        areaID int primary key auto_increment not null,
        city_area varchar(55)
    );
"""
create_table_customers = """
    CREATE TABLE customers (
        customerID int primary key auto_increment not null,
        full_name varchar(55),
        carID int,
        areaID int,
        foreign key (carID) references cars(carID),
        foreign key (areaID) references area_city(areaID) 
    );
"""
insert_into_cars = """
INSERT INTO cars (car_model) VALUES 
        ('opel astra'),
        ('nisan leaf'),
        ('toyota yaris');
"""
insert_into_area_city = """    
INSERT INTO area_city (city_area) VALUES 
        ('tbilisi'),
        ('rustavi'),
        ('gori');
"""
insert_into_customers = """  
INSERT INTO customers (full_name, carID, areaID) VALUES
	('giorgi gelashvili', 1, 1),
	('qetevan cicvidzee', 2, 2),
	('tornike facacia', 3, 3);
"""

select_tables = """
    select customerID,full_name,car_model,city_area from customers cu
    JOIN cars c ON c.carID = cu.carID
    JOIN area_city a ON a.areaID = cu.areaID;
"""

cursor.execute(create_table_cars)
cursor.execute(create_table_area_city)
cursor.execute(create_table_customers)

try:
    cursor.execute(insert_into_cars)
    cursor.execute(insert_into_area_city)
    cursor.execute(insert_into_customers)
    db_connector.commit()
    print('tables created:')
    cursor.execute(select_tables)
    result = cursor.fetchall()
    for row in result:
        print(row)
except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    db_connector.close()



