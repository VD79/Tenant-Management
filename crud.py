from sqlalchemy.orm import Session
from fastapi import HTTPException
import models,Schemas, authentication
import datetime
from sqlalchemy import and_
from fastapi.responses import JSONResponse
import bcrypt

current_date = datetime.date.today()

def get_tenant(db: Session, tenant_id: int):
    return db.query(models.tenants_basic_details).filter(models.tenants_basic_details.tenant_id == tenant_id).first()

def get_tenants(db: Session):
    return db.query(models.tenants_basic_details)

def del_tenant(db:Session, tenant_id: int):
    db_user = get_tenant(db=db, tenant_id=tenant_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="tenant does not exists")
    try:
        db.delete(db_user)
        db.commit()
    except:
        db.rollback()
        raise

def put_tenant(db:Session, tenant_id: int, tenant:Schemas.tenants_basic_details_create_request):
    db_user = get_tenant(db=db, tenant_id=tenant_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="tenant does not exists")
    
    db_user.record_modified_date = current_date
    db_user.tenant_age = tenant.tenant_age
    db_user.tenant_first_name = tenant.tenant_first_name
    db_user.tenant_gender = tenant.tenant_gender
    db_user.tenant_flat_number = tenant.tenant_flat_number
    db_user.tenant_last_name = tenant.tenant_last_name

    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def patch_tenant(db:Session, tenant_id: int, tenant:Schemas.tenants_basic_details_patch_request):
    db_user = get_tenant(db=db, tenant_id=tenant_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="tenant does not exists")
    
    db_user.record_modified_date = current_date
    if(tenant.tenant_age is not None):
        db_user.tenant_age = tenant.tenant_age
    if(tenant.tenant_first_name is not None):
        db_user.tenant_first_name = tenant.tenant_first_name
    if(tenant.tenant_gender is not None):
        db_user.tenant_gender = tenant.tenant_gender
    if(tenant.tenant_flat_number is not None):
        db_user.tenant_flat_number = tenant.tenant_flat_number
    if(tenant.tenant_last_name is not None):
        db_user.tenant_last_name = tenant.tenant_last_name

    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def approve_tenant(db:Session, tenant_id: int, tenant:Schemas.tenants_basic_details_authorize_request):
    db_user = get_tenant(db=db, tenant_id=tenant_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="tenant does not exists")
    
    db_user.record_modified_date = current_date
    if(tenant.user_action.upper() == "APPROVE"):
        db_user.tenant_status = "Approved"
    elif(tenant.user_action.upper() == "REJECT"):
        db_user.tenant_status = "Not Approved"
    else:
         raise HTTPException(status_code=400, detail="Invalid user action")
    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def create_tenant(db: Session, tenant:Schemas.tenants_basic_details_create_request):
    db_user = models.tenants_basic_details(
    tenant_first_name = tenant.tenant_first_name,
    tenant_last_name =  tenant.tenant_last_name,
    tenant_age = tenant.tenant_age,
    tenant_gender =  tenant.tenant_gender,
    tenant_flat_number = tenant.tenant_flat_number,
    tenant_status = "Pending Approval",
    record_created_date =  current_date)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise

    return db_user



def get_idntfcn(db: Session, tenant_id: int, tenant_legal_id_seq_number: int):
    return db.query(models.tenants_legal_identification).filter(
        and_(
        models.tenants_legal_identification.tenant_id == tenant_id,
        models.tenants_legal_identification.tenant_legal_id_seq_number == tenant_legal_id_seq_number
     )
    ).first()
def get_idntfcns(db: Session, tenant_id: int):
    return db.query(models.tenants_legal_identification).filter(models.tenants_legal_identification.tenant_id == tenant_id)

def del_idntfcn(db:Session, tenant_id: int, tenant_legal_id_seq_number: int):
    db_user = get_idntfcn(db=db, tenant_id=tenant_id, tenant_legal_id_seq_number=tenant_legal_id_seq_number)
    if db_user is None:
        raise HTTPException(status_code=404, detail="identification does not exists")
    try:
        db.delete(db_user)
        db.commit()
    except:
        db.rollback()
        raise


def put_idntfcn(db:Session, tenant_id: int, tenant_legal_id_seq_number: int, idntfcn:Schemas.tenants_legal_identification_create_request):
    db_user = get_idntfcn(db=db, tenant_id=tenant_id, tenant_legal_id_seq_number=tenant_legal_id_seq_number)
    if db_user is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Identification does not exist"}
        )
    else:
        db_user.record_modified_date = current_date
        db_user.tenant_legal_id_type = idntfcn.tenant_legal_id_type
        db_user.tenant_legal_id_number = idntfcn.tenant_legal_id_number
        db_user.tenant_legal_id_issued_country = idntfcn.tenant_legal_id_issued_country
        db_user.tenant_legal_id_issued_date = idntfcn.tenant_legal_id_issued_date

        try:
            db.commit()
            db.refresh(db_user)
        except:
            db.rollback()
            raise
        return db_user


def patch_idntfcn(db:Session, tenant_id: int, tenant_legal_id_seq_number: int, idntfcn:Schemas.tenants_legal_identification_patch_request):
    db_user = get_idntfcn(db=db, tenant_id=tenant_id, tenant_legal_id_seq_number = tenant_legal_id_seq_number)
    if db_user is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Identification does not exist"}
        )
    
    db_user.record_modified_date = current_date
    if(idntfcn.tenant_legal_id_type is not None):
        db_user.tenant_legal_id_type = idntfcn.tenant_legal_id_type
    if(idntfcn.tenant_legal_id_number is not None):
        db_user.tenant_legal_id_number = idntfcn.tenant_legal_id_number
    if(idntfcn.tenant_legal_id_issued_country is not None):
        db_user.tenant_legal_id_issued_country = idntfcn.tenant_legal_id_issued_country
    if(idntfcn.tenant_legal_id_issued_date is not None):
        db_user.tenant_legal_id_issued_date = idntfcn.tenant_legal_id_issued_date

    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def create_idntfcn(db: Session, tenant_id: int, idntfcn:Schemas.tenants_legal_identification_create_request):
    db_user = models.tenants_legal_identification(
    tenant_id = tenant_id,
    tenant_legal_id_type = idntfcn.tenant_legal_id_type,
    tenant_legal_id_number = idntfcn.tenant_legal_id_number,
    tenant_legal_id_issued_country = idntfcn.tenant_legal_id_issued_country,
    tenant_legal_id_issued_date = idntfcn.tenant_legal_id_issued_date,
    identification_record_status = "Pending Approval",
    record_created_date = current_date)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def approve_idntfcn(db:Session, tenant_id: int,tenant_legal_id_seq_number: int, idntfcn:Schemas.tenants_basic_details_authorize_request):
    db_user = get_idntfcn(db=db, tenant_id=tenant_id, tenant_legal_id_seq_number= tenant_legal_id_seq_number)
    if db_user is None:
        raise HTTPException(status_code=404, detail="identification does not exists")
    
    db_user.record_modified_date = current_date
    if(idntfcn.user_action.upper() == "APPROVE"):
        db_user.identification_record_status = "Approved"
    elif(idntfcn.user_action.upper() == "REJECT"):
        db_user.identification_record_status = "Not Approved"
    else:
         raise HTTPException(status_code=400, detail="Invalid user action")
    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user



def get_cntct(db: Session, tenant_id: int, tenant_contact_id: int):
    return db.query(models.tenants_contact_details).filter((models.tenants_contact_details.tenant_id == tenant_id) & (models.tenants_contact_details.tenant_contact_id == tenant_contact_id)).first()

def get_cntcts(db: Session, tenant_id: int):
     return db.query(models.tenants_contact_details).filter(models.tenants_contact_details.tenant_id == tenant_id)

def del_cntct(db:Session, tenant_id: int, tenant_contact_id: int):
    db_user = get_cntct(db=db, tenant_id=tenant_id, tenant_contact_id=tenant_contact_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="contact does not exists")
    try:
        db.delete(db_user)
        db.commit()
    except:
        db.rollback()
        raise


def put_cntct(db:Session, tenant_id: int, tenant_contact_id: int, cntct:Schemas.tenants_contact_details_create_request):
    db_user = get_cntct(db=db, tenant_id=tenant_id, tenant_contact_id= tenant_contact_id)
    if db_user is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Contact does not exist"}
        )
    
    db_user.record_modified_date = current_date
    db_user.tenant_contact_type = cntct.tenant_contact_type
    db_user.tenant_contact_number = cntct.tenant_contact_number
    db_user.tenant_email = cntct.tenant_email

    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def patch_cntct(db:Session, tenant_id: int, tenant_contact_id: int, cntct:Schemas.tenants_contact_details_patch_request):
    db_user = get_cntct(db=db, tenant_id=tenant_id, tenant_contact_id = tenant_contact_id)
    if db_user is None:
        return JSONResponse(
            status_code=404,
            content={"detail": "Contact does not exist"}
        )
    
    db_user.record_modified_date = current_date
    if(cntct.tenant_contact_type is not None):
        db_user.tenant_contact_type = cntct.tenant_contact_type
    if(cntct.tenant_contact_number is not None):
        db_user.tenant_contact_number = cntct.tenant_contact_number
    if(cntct.tenant_email is not None):
        db_user.tenant_email = cntct.tenant_email

    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def create_cntct(db: Session, tenant_id: int, cntct:Schemas.tenants_contact_details_create_request):
    db_user = models.tenants_contact_details(
    tenant_id = tenant_id,
    tenant_contact_type = cntct.tenant_contact_type,
    tenant_contact_number = cntct.tenant_contact_number,
    tenant_email = cntct.tenant_email,
    contact_record_status = "Pending Approval",
    record_created_date = current_date)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user


def approve_cntct(db:Session, tenant_id: int,tenant_contact_id: int, cntct:Schemas.tenants_basic_details_authorize_request):
    db_user = get_cntct(db=db, tenant_id=tenant_id, tenant_contact_id= tenant_contact_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="contact does not exists")
    
    db_user.record_modified_date = current_date
    if(cntct.user_action.upper() == "APPROVE"):
        db_user.contact_record_status = "Approved"
    elif(cntct.user_action.upper() == "REJECT"):
        db_user.contact_record_status = "Not Approved"
    else:
         raise HTTPException(status_code=400, detail="Invalid user action")
    try:
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user

def create_user(db: Session, usr:Schemas.user_request):
    hashed_password = bcrypt.hashpw(usr.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    db_user = models.login_details(
    password = hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        db.rollback()
        raise
    return db_user

def login(db:Session,user_id:int, password:str):
    hashed_password = db.query(models.login_details).filter(models.login_details.user_id == user_id).first()
    if not hashed_password:
        return 0
    db_password = hashed_password.password
    if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
        return 1
    else:
        return 0