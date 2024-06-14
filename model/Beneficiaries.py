from sqlalchemy import Column, Integer, String
from model import Base


class Beneficiaries(Base):
  __tablename__ = 'beneficiaries'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  cpf = Column(String(11), nullable=False, unique=True)
  address = Column(String(255), default="")

  def __init__(self, name: str, cpf: str, address: str):
    if not self._is_valid_cpf(cpf):
      raise ValueError("CPF must be exactly 11 characters long")
    self.name = name
    self.cpf = cpf
    self.address = address

  @staticmethod
  def _is_valid_cpf(cpf: str) -> bool:
    return len(cpf) == 11 and cpf.isdigit()