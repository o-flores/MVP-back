from pydantic import BaseModel
from typing import List
from model import Donations, Beneficiaries, Donors

class DonationSchema(BaseModel):
  id: int
  donor_id: int
  donor_name: str
  beneficiary_id: int
  beneficiary_name: str
  product: str
  quantity: str


class DonationListSchema(BaseModel):
  donors: List[DonationSchema]

class DonationPostSchema(BaseModel):
  beneficiary_id: int
  donor_id: int
  product: str
  quantity:str

class DeleteDonationSchema(BaseModel):
  id: int


def list_donation(donation: Donations, beneficiary: Beneficiaries, donor: Donors):
  return {
    "id": donation['id'],
    "beneficiary_id": beneficiary['id'],
    "beneficiary_address": beneficiary['address'],
    "cpf": beneficiary['cpf'],
    "beneficiary_name": beneficiary['name'],
    "donor_id": donor['id'],
    "donor_name": donor['name'],
    "donor_address": donor['address'],
    "cnpj": donor['cnpj'],
    "product": donation['product'],
    "quantity": donation['quantity']
  }