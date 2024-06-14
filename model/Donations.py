from sqlalchemy import Column, Integer, ForeignKey, String
from model import Base

class Donations(Base):
  __tablename__ = 'donations'

  id = Column(Integer, primary_key=True, autoincrement=True)
  donor_id= Column(Integer, ForeignKey("donors.id"))
  beneficiary_id= Column(Integer, ForeignKey("beneficiaries.id"))
  product = Column(String(255))
  quantity = Column(String(255))

  
  def __init__(self, donor_id: int, beneficiary_id: int, product: str, quantity: str):
    self.donor_id = donor_id
    self.beneficiary_id = beneficiary_id
    self.product = product
    self.quantity = quantity