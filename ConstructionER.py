import sqlite3


# -------------------Context Manager-------------------
class DatabaseContextManager(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


# ------------------------Table Creation------------------------
def create_table_clients():
    query = """CREATE TABLE IF NOT EXISTS Clients(
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_name VARCHAR(50),
    client_address VARCHAR(255))"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)


def create_table_company():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name VARCHAR(50),
    area_of_expertise VARCHAR(255),
    company_address VARCHAR(255),
    number_of_employees INTEGER)"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)


def create_table_construction_sites():
    query = """CREATE TABLE IF NOT EXISTS ConstructionSites(
    construction_site_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    company_id INTEGER,
    name_of_project VARCHAR(255),
    construction_site_address VARCHAR(255),
    construction_site_budget INTEGER,
    FOREIGN KEY(client_id) REFERENCES Clients(client_id),
    FOREIGN KEY(company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)


def create_table_jobs():
    query = """CREATE TABLE IF NOT EXISTS Jobs(
    job_number INTEGER PRIMARY KEY AUTOINCREMENT,
    construction_site_id INTEGER,
    job_start_date DATE,
    job_finish_date DATE,
    number_of_workers INTEGER,
    FOREIGN KEY(construction_site_id) REFERENCES ConstructionSites(construction_site_id))"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)


def create_table_employees():
    query = """CREATE TABLE IF NOT EXISTS Employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_number_id INTEGER,
    company_id INTEGER,
    employee_name VARCHAR(50),
    employee_surname VARCHAR(50),
    employee_address VARCHAR(255),
    employee_salary INTEGER,
    FOREIGN KEY(job_number_id) REFERENCES Jobs(job_number),
    FOREIGN KEY(company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)


def create_table_tools():
    query = """CREATE TABLE IF NOT EXISTS Tools(
    tool_id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    tool_name VARCHAR(255),
    is_battery_powered BOOL,
    number_of_batteries INTEGER,
    tool_voltage INTEGER,
    FOREIGN KEY(employee_id) REFERENCES Employees(employee_id))"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)


# ------------------------Clients-CRUD------------------------
def create_client(client_name: str, client_address: str):
    query = """INSERT INTO Clients(client_name, client_address) VALUES (?,?)"""
    params = [client_name, client_address]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_clients():
    query = """SELECT * FROM Clients"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_client(old_address, new_address):
    query = """UPDATE Clients
            SET client_address = ?
            WHERE client_address = ?"""
    params = [new_address, old_address]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def delete_client(client_id: int):
    query = """DELETE FROM Clients(
                WHERE client_id = ?"""
    params = [client_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


# ------------------------Companies-CRUD------------------------
def create_company(company_name: str, area_of_expertise: str, company_address: str, number_of_employees: int):
    query = """INSERT INTO Companies(company_name, area_of_expertise, company_address, number_of_employees)
            VALUES (?,?,?,?)"""
    params = [company_name, area_of_expertise, company_address, number_of_employees]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_company(old_number_of_employees, new_number_of_employees):
    query = """UPDATE Companies
            SET number_of_employees = ?
            WHERE number_of_employees = ?"""
    params = [new_number_of_employees, old_number_of_employees]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def delete_company(company_id: int):
    query = """DELETE FROM Companies(
                WHERE company_id = ?"""
    params = [company_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


# ------------------------Construction_Sites-CRUD------------------------
def create_construction_site(client_id: int, company_id: int, name_of_project: str, construction_site_address: str,
                             construction_site_budget: int):
    query = """INSERT INTO ConstructionSites(client_id, company_id, name_of_project,
            construction_site_address, construction_site_budget) VALUES (?,?,?,?,?)"""
    params = [client_id, company_id, name_of_project, construction_site_address, construction_site_budget]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_construction_sites():
    query = """SELECT * FROM ConstructionSites"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_construction_site(construction_site_id, new_construction_site_budget):
    query = """UPDATE ConstructionSites
            SET construction_site_budget = ?
            WHERE construction_site_id = ?"""
    params = [new_construction_site_budget, construction_site_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def delete_construction_site(construction_site_id: int):
    query = """DELETE FROM ConstructionSites(
                WHERE construction_site_id = ?"""
    params = [construction_site_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


# ------------------------Jobs-CRUD------------------------
def create_job(construction_site_id: int, job_start_date: str, job_finish_date: str, number_of_workers: int):
    query = """INSERT INTO Jobs(construction_site_id, job_start_date, job_finish_date, number_of_workers)
            VALUES (?,?,?,?)"""
    params = [construction_site_id, job_start_date, job_finish_date, number_of_workers]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_jobs():
    query = "SELECT * FROM Jobs"
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_job(job_number, new_number_of_workers):
    query = """UPDATE Jobs
            SET number_of_workers = ?
            WHERE job_number = ?"""
    params = [new_number_of_workers, job_number]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def delete_job(job_number: int):
    query = """DELETE FROM Jobs
            WHERE job_number = ?"""
    params = [job_number]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


# ------------------------Employees-CRUD------------------------
def create_employee(job_number_id: int, company_id: int, employee_name: str, employee_surname: str,
                    employee_address: str, employee_salary: int):
    query = """INSERT INTO Employees(job_number_id, company_id, employee_name,
            employee_surname, employee_address, employee_salary)
            VALUES (?,?,?,?,?,?)"""
    params = [job_number_id, company_id, employee_name, employee_surname, employee_address,
              employee_salary]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_employees():
    query = """SELECT * FROM Employees"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_employee(employee_id, new_salary):
    query = """UPDATE Employees
            SET employee_salary = ?
            WHERE employee_id = ?"""
    params = [new_salary, employee_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def delete_employee(employee_id):
    query = """DELETE FROM Employees
            WHERE employee_id = ?"""
    params = [employee_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_all_employee_data(employee_id):
    query = """SELECT employee_id, employee_name, employee_surname, employee_address, employee_salary,
    company_name, area_of_expertise, company_address, number_of_employees, job_start_date, job_finish_date FROM Employees
    JOIN Companies
    ON Employees.company_id = Companies.company_id
    JOIN Jobs
    ON Employees.job_number_id = Jobs.job_number
    WHERE employee_id = ?"""
    params = [employee_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


# ------------------------Tools-CRUD------------------------
def create_tool(employee_id: int, tool_name: str, is_battery_powered: bool, number_of_batteries: int, tool_voltage: int):
    query = """INSERT INTO Tools(employee_id, tool_name, is_battery_powered, number_of_batteries, tool_voltage)
            VALUES (?,?,?,?,?)"""
    params = [employee_id, tool_name, is_battery_powered, number_of_batteries, tool_voltage]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def get_tools():
    query = """SELECT * FROM Tools"""
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def update_tool(tool_id, new_number_of_batteries):
    query = """UPDATE Tools
            SET number_of_batteries = ?
            WHERE tool_id = ?"""
    params = [new_number_of_batteries, tool_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


def delete_tool(tool_id):
    query = """DELETE FROM Tools
            WHERE tool_id = ?"""
    params = [tool_id]
    with DatabaseContextManager("ConstructionDB") as db:
        db.execute(query, params)


# create_table_clients()
# create_table_company()
# create_table_construction_sites()
# create_table_jobs()
# create_table_employees()
# create_table_tools()

# create_client("SISK", "35 Geater London Road, London, UK")
# create_company("Brogan Group", "Scaffolding", "3 Arnos Grove, Greater London, UK", 200)
# create_construction_site(1, 1, "Walkie-Talkie", "20 Fenchurch Stree, London, UK", 350000000)
# create_job(1, "2012-11-30", "2016-04-04", 785)
# create_employee(1, 1, "Peter", "Arbuckle", "123 Silly House, Manchester, UK", 45300)
# create_tool(1, "Drill", 1, 4, 36)
get_all_employee_data(1)
