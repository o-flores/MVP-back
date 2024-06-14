from sqlalchemy import Column, Integer, String
from model import Base


class Beneficiaries(Base):
  __tablename__ = 'beneficiaries'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  cpf = Column(String(11), nullable=False)
  address = Column(String(255), default="")

  def __init__(self, name: str, cpf: str, address: str):
    self.name = name
    self.cpf = cpf
    self.address = address