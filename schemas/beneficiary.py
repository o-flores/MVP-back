from pydantic import BaseModel
from model import Beneficiaries
from typing import List, Union

class BeneficiarySchema(BaseModel):
  id: int
  name: str
  cpf: str
  address: Union[str, None]


class BeneficiariesListSchema(BaseModel):
  donors: List[BeneficiarySchema]

class GetBeneficiarySchema(BaseModel):
  id: int

class PostBeneficiarySchema(BaseModel):
  name: str
  address: Union[str, None]
  cpf: str

def list_beneficiary(beneficiary: Beneficiaries):
  return {
    "id": beneficiary.id,
    "name": beneficiary.name,
    "cpf": beneficiary.cpf,
    "address": beneficiary.address
  }