from sqlalchemy import Column, Integer, String
from model import Base

class Donors(Base):
  __tablename__ = 'donors'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  cnpj = Column(String(14), nullable=False, unique=True)
  address = Column(String(255), default="")

  def __init__(self, name: str, cnpj: str, address: str):
    if not self._is_valid_cnpj(cnpj):
      raise ValueError("CNPJ must be exactly 14 characters long")
    self.name = name
    self.cnpj = cnpj
    self.address = address


  @staticmethod
  def _is_valid_cnpj(cnpj: str):
    return len(cnpj) == 14 and cnpj.isdigit()