from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

url = "mysql+pymysql://root:root@localhost/MVP"

engine = create_engine(url)

Session = scoped_session(sessionmaker(bind=engine))
