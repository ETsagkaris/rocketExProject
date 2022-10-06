import requests
from . import errors, settings


HEADERS = {
    "Authorization": f"Bearer {settings.token}",
    "Content-Type": "application/json",
}


def create_contact(contact):
    response = requests.post(
        f"{settings.endpoint}/contacts",
        json={"properties": contact.dict()},
        headers=HEADERS
    )
    data = response.json()
    if response.status_code != 201:
        raise errors.JsonException(
            errors.CONTACT_CREATION_FAILED,
            data=data, code=response.status_code)
    return data


def edit_contact(contact_id, contact):
    response = requests.patch(
        f"{settings.endpoint}/contacts/{contact_id}",
        json={"properties": contact.dict()},
        headers=HEADERS
    )
    data = response.json()
    if response.status_code != 200:
        raise errors.JsonException(
            errors.CONTACT_UPDATE_FAILED,
            data=data, code=response.status_code)
    return data


def create_company(company):
    response = requests.post(
        f"{settings.endpoint}/companies",
        json={"properties": company.dict()},
        headers=HEADERS
    )
    data = response.json()
    if response.status_code != 201:
        raise errors.JsonException(
            errors.COMPANY_CREATION_FAILED,
            data=data, code=response.status_code)
    return data


def edit_company(company_id, company):
    response = requests.patch(
        f"{settings.endpoint}/companies/{company_id}",
        json={"properties": company.dict()},
        headers=HEADERS
    )
    data = response.json()
    if response.status_code != 200:
        raise errors.JsonException(
            errors.COMPANY_UPDATE_FAILED,
            data=data, code=response.status_code)
    return data
