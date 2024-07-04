from model import Donors, Session, Beneficiaries, Donations
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask import redirect
from sqlalchemy.exc import IntegrityError
from schemas import DonorsListSchema, DonorSchema, BeneficiariesListSchema, DonationPostSchema, GetBeneficiarySchema, DeleteDonationSchema, BeneficiarySchema, PostBeneficiarySchema, list_beneficiary, PostDonorSchema, list_donor, list_donation, MessageSchema, GetDonorSchema, DonationListSchema, list_message
from flask_cors import CORS

info = Info(title="mvp API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


doc_tag = Tag(name="Documentação")
donors_tag = Tag(name="Donors")
donations_tag = Tag(name="Donations")
beneficiaries_tag = Tag(name="Beneficiaries")

@app.get('/', tags=[doc_tag])
def doc():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get("/donors", tags=[donors_tag], responses={"200": DonorsListSchema, "500": MessageSchema})
def get_donors():
    try:  
        session = Session()
        donors = session.query(Donors).all()
        result = []
        for donor in donors:
            result.append(list_donor(donor))
        return result, 200
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))

@app.get("/donors/<int:id>", tags=[donors_tag], responses={"200": DonorSchema, "500": MessageSchema, "404": MessageSchema})
def get_donor(path: GetDonorSchema):
    try:
        session = Session()
        donor = session.query(Donors).filter(Donors.id == path.id).one_or_none()
        if not donor:
            return list_message(MessageSchema(message="Donor not found", code=404))
        return list_donor(donor), 200
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))
    
@app.post("/donor", tags=[donors_tag], responses={"200": MessageSchema, "500": MessageSchema, "409": MessageSchema})
def create_donor(body: PostDonorSchema):
    try:
        session = Session()
        donor = Donors(name=body.name, cnpj=body.cnpj, address=body.address)
        session.add(donor)
        session.commit()
        return list_message(MessageSchema(message="Donor not found", code=200))
    except IntegrityError:
        return list_message(MessageSchema(message="Donor already exists", code=409))
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))    

@app.get("/beneficiaries", tags=[beneficiaries_tag], responses={"200": BeneficiariesListSchema, "500": MessageSchema})
def get_beneficiaries():
    try:
        session = Session()
        beneficiaries = session.query(Beneficiaries).all()
        result = []
        for beneficiary in beneficiaries:
            result.append(list_beneficiary(beneficiary))
        return result, 200
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))

@app.get("/beneficiaries/<int:id>", tags=[beneficiaries_tag], responses={"200": BeneficiarySchema, "500": MessageSchema, "404": MessageSchema})
def get_beneficiary(path: GetBeneficiarySchema):
    try:
        session = Session()
        beneficiary = session.query(Beneficiaries).filter(Beneficiaries.id == path.id).one_or_none()
        if not beneficiary:
            return list_message(MessageSchema(message="Beneficiary not found", code=404))
        else:
            return list_beneficiary(beneficiary), 200
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))
    
@app.post("/beneficiary", tags=[beneficiaries_tag], responses={"200": MessageSchema, "500": MessageSchema, "409": MessageSchema})
def create_beneficiary(body: PostBeneficiarySchema):
    try:
        session = Session()
        beneficiary = Beneficiaries(name=body.name, cpf=body.cpf, address=body.address)
        session.add(beneficiary)
        session.commit()
        return list_message(MessageSchema(message="Beneficiary added", code=200))
    except IntegrityError:
        return list_message(MessageSchema(message="Beneficiary already exists", code=409))
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))
    
@app.get("/donations", tags=[donations_tag], responses={"200": DonationListSchema, "500": MessageSchema})
def get_donations():
    try:
        session = Session()
        donations = session.query(Donations).all()
        result = []
        for donation in donations:
            donor, _ = get_donor(GetDonorSchema(id=donation.donor_id))
            beneficiary, _ = get_beneficiary(GetBeneficiarySchema(id=donation.beneficiary_id))
            result.append(list_donation(donation.__dict__, beneficiary, donor))
        return result, 200
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))

    
@app.post("/donation", tags=[donations_tag], responses={"200": MessageSchema, "500": MessageSchema})
def create_donation(body: DonationPostSchema):
    try:
        session = Session()
        donation = Donations(donor_id=body.donor_id, beneficiary_id=body.beneficiary_id, product=body.product, quantity=body.quantity)
        session.add(donation)
        session.commit()
        return list_message(MessageSchema(message="Donation added", code=200))
    except Exception as e:
        return list_message(MessageSchema(message=str(e), code=500))

@app.delete("/donations", tags=[donations_tag], responses={"200": MessageSchema, "500": MessageSchema, "404": MessageSchema})
def delete_donation(body: DeleteDonationSchema):
    try:
        session = Session()
        donation = session.query(Donations).filter(Donations.id == body.id).first()
        if donation:
            session.delete(donation)
            session.commit()
            return list_message(MessageSchema(message="Donation deleted", code=200))
        else:
            return list_message(MessageSchema(message="Donation not found", code=404))
    except Exception as e:
        list_message(MessageSchema(message=str(e), code=500))

if __name__ == "__main__":
    app.run(debug=True)
