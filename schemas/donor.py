from pydantic import BaseModel
from model import Donors
from typing import List, Union

class DonorSchema(BaseModel):
  id: int
  name: str
  cnpj: str
  address: Union[str, None]


class DonorsListSchema(BaseModel):
  donors: List[DonorSchema]

class GetDonorSchema(BaseModel):
  id: int

class PostDonorSchema(BaseModel):
  name: str
  address: Union[str, None]
  cnpj: str

def list_donor(donor: Donors):
  return {
    "id": donor.id,
    "name": donor.name,
    "cnpj": donor.cnpj,
    "address": donor.address
  }