from sqlalchemy import Column, Integer, ForeignKey
from model import Base

class Donations(Base):
  __tablename__ = 'donations'

  id = Column(Integer, primary_key=True, autoincrement=True)
  donor_id= Column(Integer, ForeignKey("donors.id"))
  beneficiary_id= Column(Integer, ForeignKey("beneficiaries.id"))