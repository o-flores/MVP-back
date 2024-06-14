from sqlalchemy import Column, Integer, String
from model import Base

class Donors(Base):
  __tablename__ = 'donors'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  cnpj = Column(String(14), nullable=False)
  address = Column(String(255), default="")

  def __init__(self, name: str, cnpj: str, address: str):
    self.name = name
    self.cnpj = cnpj
    self.address = address

