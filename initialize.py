import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, url, Donors, Beneficiaries
import urllib.parse as urlparse

parsed_url = urlparse.urlparse(url)
database = parsed_url.path[1:]
username = parsed_url.username
password = parsed_url.password
hostname = parsed_url.hostname

donors = [
    Donors(name='SUPERMERCADOS GUANABARA S.A.', cnpj='94846755000155', address=''),
    Donors(name='SUPERMERCADO EXTRA', cnpj='12345678000199', address=''),
    Donors(name='PÃO DE ACUCAR', cnpj='98765432000177', address=''),
]

beneficiaries = [
    Beneficiaries(name='Julia Rodrigues', cpf='11111111111', address=''),
    Beneficiaries(name='Gilmar Neves', cpf='22222222222', address=''),
    Beneficiaries(name='Gustavo Takeda', cpf='33333333333', address=''),
]
    

def create_database():
    connection = pymysql.connect(host=hostname, user=username, password=password)
    cursor = connection.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {database}")
    cursor.execute(f"CREATE DATABASE {database}")
    connection.close()

def initialize_database(engine):
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")

def insert_initial_data(session):
    session.add_all(donors)
    session.add_all(beneficiaries)
    session.commit()
    print("Initial data inserted successfully.")

if __name__ == "__main__":
    create_database()
    engine = create_engine(url, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    initialize_database(engine)
    insert_initial_data(session)
