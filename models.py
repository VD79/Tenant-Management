from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship

from database import Base

class tenants_basic_details(Base):
    __tablename__ = "tenants_basic_details"
    tenant_id = Column(Integer,primary_key=True,index=True)
    tenant_first_name = Column(String(255))
    tenant_last_name = Column(String(255))
    tenant_age = Column(Integer)
    tenant_gender = Column(String(15))
    tenant_flat_number = Column(Integer)
    tenant_status = Column(String(20))
    record_created_date = Column(Date)
    record_modified_date = Column(Date)

class tenants_legal_identification(Base):
    __tablename__ = "tenants_legal_identification"
    tenant_id = Column(Integer, ForeignKey("tenants_basic_details.tenant_id"))
    tenant_legal_id_seq_number = Column(Integer,primary_key=True,index=True)
    tenant_legal_id_type = Column(String(50))
    tenant_legal_id_number = Column(String(20))
    tenant_legal_id_issued_country = Column(String(50))
    tenant_legal_id_issued_date = Column(Date)
    identification_record_status = Column(String(20))
    record_created_date = Column(Date)
    record_modified_date = Column(Date)
    __table_args__ = (
        UniqueConstraint('tenant_legal_id_type', 'tenant_legal_id_number',tenant_legal_id_issued_country, name='unq_cnstrnt_idntfctn'),
    )

class tenants_contact_details(Base):
    __tablename__ = "tenants_contact_details"
    tenant_id = Column(Integer, ForeignKey("tenants_basic_details.tenant_id"))
    tenant_contact_id = Column(Integer, primary_key=True,index=True)
    tenant_contact_type = Column(String(15))
    tenant_contact_number = Column(Integer)
    tenant_email = Column(String(255))
    contact_record_status = Column(String(20))
    record_created_date = Column(Date)
    record_modified_date = Column(Date)
    __table_args__ = (
        UniqueConstraint('tenant_contact_type', 'tenant_contact_number', name='unq_cnstrnt_cntct'),
    )

class login_details(Base):
    __tablename__ = "login_details"
    user_id = Column(Integer, primary_key=True,index=True)
    password = Column(String(100))