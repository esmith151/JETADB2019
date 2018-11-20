import random 
import psycopg2
from config import config

employees_first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']
employees_last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

customers_first_names=[]
customers_last_names=[]

filename1='firstNames.txt'
filename2='lastNames.txt'

with open (filename1) as fin:
    for line in fin:
        customers_first_names.append(line.strip())


with open (filename2) as fin:
    for line in fin:
        customers_last_names.append(line.strip())

  


def insert_employee(Fname, Lname):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO employees(FName, LName)
             VALUES(%s, %s) RETURNING EmployeeId;"""
    conn = None
    EmployeeId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Fname,Lname))
        # get the generated id back
        EmployeeId = cur.fetchone()[0]
        print("The EmployeeId is: "+f'{EmployeeId}')
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return EmployeeId


def insert_customers(Fname, Lname, Phone, Email, Address, City, State, Zip):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO customers(Fname, Lname, Phone, Email, Address, City, State, Zip)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING CustomerId;"""
    conn = None
    CustomerId = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Fname,Lname,Phone,Email,Address,City,State,Zip))
        # get the generated id back
        CustomerId = cur.fetchone()[0]
        print("The CustomerId is: "+f'{CustomerId}')
        print(" ")
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return CustomerId




if __name__ == '__main__':
    
    #generates 100 fake employees
    # UNCOMMENT TO INSERT
    for x in range(1):
    
        first_employee = random.choice(employees_first_names)
        last_employee = random.choice(employees_last_names)

        # insert_employee(first_employee, first_employee)
        print(f'{first_employee} {last_employee}\n')



    #generates 100 fake customers
    # UNCOMMENT TO INSERT
    for x in range(1):
        first_customer = random.choice(customers_first_names)
        last_customer = random.choice(customers_last_names)

        phone_string = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

        emailAt = '@jetastore.com'
        email = f'{first_customer.lower()}{last_customer.lower()}{emailAt}'

        street_num = random.randint(100, 999)
        street = random.choice(street_names)
        city = random.choice(fake_cities)
        state = random.choice(states)
        zip_string = f'{random.randint(10000, 99999)}'
        address = f'{street_num} {street} St.,'
        
        # insert_customers(first_customer, last_customer, phone_string, email, address, city, state, zip_string)
        print(f'{first_customer}\n{last_customer}\n{phone_string}\n{email}\n{address}\n{city}\n{state}\n{zip_string}\n')
        print(" ")