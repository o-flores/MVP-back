from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

url = "mysql+pymysql://root:root@localhost/MVP"

engine = create_engine(url)

Session = sessionmaker(bind=engine)
