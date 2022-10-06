from fastapi import FastAPI
import uvicorn

from app import schemas, api, logic


app = FastAPI()
app.router.route_class = api.Wrapper


@app.post("/contacts/", response_model=schemas.Contact, status_code=201)
def create_contact(
    contact: schemas.ContactCreate,
):
    return logic.create_contact(contact)


@app.put("/contacts/{contact_id}/",
         response_model=schemas.Contact)
def edit_contact(
    contact_id: str,
    contact: schemas.ContactUpdate,
):
    return logic.edit_contact(contact_id, contact)


@app.post("/companies/", response_model=schemas.Company, status_code=201)
def create_company(
    company: schemas.CompanyCreate,
):
    return logic.create_company(company)


@app.put("/companies/{company_id}/",
         response_model=schemas.Company)
def edit_company(
    company_id: str,
    company: schemas.CompanyUpdate,
):
    return logic.edit_company(company_id, company)


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
