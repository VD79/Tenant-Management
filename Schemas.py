from pydantic import BaseModel,ConfigDict, Field
from datetime import date
from typing import Optional

class tenants_basic_details_base(BaseModel):
    tenant_id : int = Field(..., alias="tenant-id", description="Unique Identifier of the tenant")
    tenant_first_name : str = Field(..., alias="tenant-first-name", description="First name of the tenant")
    tenant_last_name : str = Field(..., alias="tenant-last-name", description="Last name of the tenant")
    tenant_age : int = Field(..., alias="tenant-age", description="Age of the tenant")
    tenant_gender : str = Field(..., alias="tenant-gender", description="Gender of the tenant")
    tenant_flat_number : int = Field(..., alias="tenant-flat-number", description="Flat number of the tenant")
    tenant_status : str = Field(..., alias="tenant-status", description="Status of the tenant")
    record_created_date : date = Field(..., alias="record-created-date", description="Created on date")
    record_modified_date : date

class tenants_basic_details_create_request(BaseModel):
    tenant_first_name : str = Field(..., alias="tenant-first-name", description="First name of the tenant")
    tenant_last_name : str = Field(..., alias="tenant-last-name", description="Last name of the tenant")
    tenant_age : int = Field(..., alias="tenant-age", description="Age of the tenant")
    tenant_gender : str = Field(..., alias="tenant-gender", description="Gender of the tenant")
    tenant_flat_number : int = Field(..., alias="tenant-flat-number", description="Flat number of the tenant")
    
    model_config = ConfigDict(title = "tenants-basic-details-create-request")

class tenants_basic_details_patch_request(BaseModel):
    tenant_first_name : Optional[str] = Field(None, alias="tenant-first-name", description="First name of the tenant")
    tenant_last_name : Optional[str] = Field(None, alias="tenant-last-name", description="Last name of the tenant")
    tenant_age : Optional[int] = Field(None, alias="tenant-age", description="Age of the tenant")
    tenant_gender : Optional[str] = Field(None, alias="tenant-gender", description="Gender of the tenant")
    tenant_flat_number : Optional[int] = Field(None, alias="tenant-flat-number", description="Flat number of the tenant")

    model_config = ConfigDict(title = "tenants-basic-details-patch-request")

class tenants_basic_details_response(tenants_basic_details_base):
    record_modified_date : Optional[date] = Field(None, alias="last-modified-date", description="Last modifed date of the record")

    model_config = ConfigDict(from_attributes=True, title = "tenants-basic-details-response", populate_by_name=True)

class tenants_basic_details_create_response(BaseModel):
    tenant_id : int = Field(..., alias="tenant-id", description="Unique Identifier of the tenant")
    tenant_status : str = Field(..., alias="tenant-status", description="Status of the tenant")

    model_config = ConfigDict(from_attributes=True, title = "tenants-basic-details-response", populate_by_name = True)

class tenants_basic_details_authorize_request(BaseModel):
    user_action : str = Field(..., alias="user-action", description="Approve/Reject")

    model_config = ConfigDict(title = "tenants-basic-details-authorize-request")


class tenants_legal_identification_base(BaseModel):
    tenant_id : int = Field(..., alias="tenant-id", description="Unique Identifier of the tenant")
    tenant_legal_id_seq_number : int = Field(..., alias="tenant-legal-id-seq-number", description="Unique Identifier of the identification record")
    tenant_legal_id_type : str = Field(..., alias="tenant-legal-id-type", description="Id type of the tenant")
    tenant_legal_id_number : str = Field(..., alias="tenant-legal-id-number", description="Id number of the tenant")
    tenant_legal_id_issued_country : str = Field(..., alias="tenant-legal-id-issued-country", description="Id issued country")
    tenant_legal_id_issued_date : date = Field(..., alias="tenant-legal-id-issued-date", description="Id issued date")
    identification_record_status : str = Field(..., alias="identification-record-status", description="Status of the identifcation")
    record_created_date : date = Field(..., alias="record-created-date", description="Created on date")
    record_modified_date : date

class tenants_legal_identification_create_request(BaseModel):
    tenant_legal_id_type : str = Field(..., alias="tenant-legal-id-type", description="Id type of the tenant")
    tenant_legal_id_number : str = Field(..., alias="tenant-legal-id-number", description="Id number of the tenant")
    tenant_legal_id_issued_country : str = Field(..., alias="tenant-legal-id-issued-country", description="Id issued country")
    tenant_legal_id_issued_date : date = Field(..., alias="tenant-legal-id-issued-date", description="Id issued date")

    model_config = ConfigDict(title = "tenants-legal-identification-create-request")
    

class tenants_legal_identification_patch_request(BaseModel):
    tenant_legal_id_type : Optional[str] = Field(None, alias="tenant-legal-id-type", description="Id type of the tenant")
    tenant_legal_id_number : Optional[str] = Field(None, alias="tenant-legal-id-number", description="Id number of the tenant")
    tenant_legal_id_issued_country : Optional[str] = Field(None, alias="tenant-legal-id-issued-country", description="Id issued country")
    tenant_legal_id_issued_date : Optional[date] = Field(None, alias="tenant-legal-id-issued-date", description="Id issued date")

    model_config = ConfigDict(title = "tenants-legal-identification-patch-request")



class tenants_legal_identification_response(tenants_legal_identification_base):
    record_modified_date : Optional[date] = Field(None, alias="last-modified-date", description="Last modifed date of the record")
    
    model_config = ConfigDict(from_attributes=True, title = "tenants-legal-identification-response", populate_by_name = True)

class tenants_legal_identification_create_response(BaseModel):
    tenant_id : int = Field(..., alias="tenant-id", description="Unique Identifier of the tenant")
    tenant_status : str = Field(..., alias="tenant-status", description="Status of the tenant")
    tenant_legal_id_seq_number : int = Field(..., alias="tenant-legal-id-seq-number", description="Unique Identifier of the identification record") 
    identification_record_status : str = Field(..., alias="identification-record-status", description="Status of the identifcation")
    
    model_config = ConfigDict(from_attributes=True, title = "tenants-legal-identification-creaate-response", populate_by_name = True)




class tenants_contact_details_base(BaseModel):
    tenant_id : int = Field(..., alias="tenant-id", description="Unique Identifier of the tenant")
    tenant_contact_id : int = Field(..., alias="tenant-contact-id", description="Unique Identifier of contact")
    tenant_contact_type : str = Field(..., alias="tenant-contact-type", description="Type of contact")
    tenant_contact_number : int = Field(...,alias = "tenant-contact-number", description = "Contact number of tenant")
    tenant_email : str = Field(...,alias = "tenant-email", description = "Email of tenant")
    contact_record_status : str = Field(..., alias="contact-record-status", description="Status of the conatct")
    record_created_date : date = Field(..., alias="record-created-date", description="Created on date")
    record_modified_date : date

class tenants_contact_details_create_request(BaseModel):
    tenant_contact_type : str = Field(..., alias="tenant-contact-type", description="Type of contact")
    tenant_contact_number : int = Field(...,alias = "tenant-contact-number", description = "Contact number of tenant")
    tenant_email : str = Field(...,alias = "tenant-email", description = "Email of tenant")

    model_config = ConfigDict(title = "tenants-contact-details-create-request")


class tenants_contact_details_patch_request(BaseModel):
    tenant_contact_type : Optional[str] = Field(None, alias="tenant-contact-type", description="Type of contact")
    tenant_contact_number : Optional[int] = Field(None,alias = "tenant-contact-number", description = "Contact number of tenant")
    tenant_email : Optional[str] = Field(None,alias = "tenant-email", description = "Email of tenant")

    model_config = ConfigDict(title = "tenants-contact-details-patch-request")



class tenants_contact_details_response(tenants_contact_details_base):
    record_modified_date : Optional[date] = Field(None, alias="last-modified-date", description="Last modifed date of the record")
    
    model_config = ConfigDict(from_attributes=True, title = "tenants-contact-details-response", populate_by_name = True)


class tenants_contact_details_create_response(BaseModel):
    tenant_id : int = Field(..., alias="tenant-id", description="Unique Identifier of the tenant")
    tenant_status : str = Field(..., alias="tenant-status", description="Status of the tenant")
    tenant_contact_id : int =  Field(..., alias="tenant-contact-id", description="Unique Identifier of contact")
    contact_record_status : str = Field(..., alias="contact-record-status", description="Status of the conatct")

    model_config = ConfigDict(from_attributes=True, title = "tenants-contact-details-create-response", populate_by_name = True)


class login_response(BaseModel):
    login_flag : int = Field(..., alias="login-flag", description="It determines whether login is succesfull or not")

class user_respone(BaseModel):
    user_id : int = Field(..., alias="user-id", description="ID of the user")
    model_config = ConfigDict(from_attributes=True, title = "create-user-response", populate_by_name = True)

class user_request(BaseModel):
    password : str = Field(..., alias="password", description="Password of the user")