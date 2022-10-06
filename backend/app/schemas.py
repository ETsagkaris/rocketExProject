from pydantic import BaseModel
from typing import Optional


class ContactProperties(BaseModel):
    createdate: Optional[str]
    lastmodifieddate: Optional[str]
    company: Optional[str]
    email: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    website: Optional[str]


class Contact(BaseModel):
    id: str
    properties: ContactProperties
    createdAt: str
    updatedAt: str
    archived: bool


class ContactCreate(BaseModel):
    company: str
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str


class ContactUpdate(BaseModel):
    company: Optional[str]
    email: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    website: Optional[str]


class CompanyProperties(BaseModel):
    createdate: str
    hs_lastmodifieddate: str
    city: Optional[str]
    domain: Optional[str]
    industry: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    state: Optional[str]


class Company(BaseModel):
    id: str
    properties: CompanyProperties
    createdAt: str
    updatedAt: str
    archived: bool


class CompanyCreate(BaseModel):
    city: str
    domain: str
    industry: str
    name: str
    phone: str
    state: str


class CompanyUpdate(BaseModel):
    city: Optional[str]
    domain: Optional[str]
    industry: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    state: Optional[str]
