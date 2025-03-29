from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import crud, models, Schemas,authentication
from database import SessionLocal, engine
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI( 
    root_path="/tenant-management",
    title="Tenant Management REST APIs",
    description="These APIs deals with the tenant's information such as basic details,legal identification details and contact details.",
    contact={
        "name": "Developer - Vamsi Darsi",
        "email": "vamsidarsi10@gmail.com",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for better security
    allow_methods=["GET", "POST", "PUT", "DELETE","PATCH"],  # HTTP methods allowed
    allow_headers=["*"],  # Allow all headers
)

@app.middleware("http")
async def no_cache_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store"
    return response

def get_current_user(request: Request):
    session_token = request.cookies.get("session_id")
    if not session_token or session_token not in session_store:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return session_store[session_token]


templates = Jinja2Templates(directory="C://Newfast//.newenv//templates")

@app.get("/login", response_class=HTMLResponse, tags=["login-screen"], summary="Login", include_in_schema=True)
async def read_root(request: Request):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("Login.html", {"request": request})

@app.get("/home", response_class=HTMLResponse, tags=["home-screen"], summary="Home", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("Home.html", {"request": request})

@app.get("/logout", response_class=HTMLResponse, tags=["logout"], summary="logout", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("Logout.html", {"request": request})

@app.get("/tenant", response_class=HTMLResponse, tags=["tenant-screen"], summary="Tenant Basic Details", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("Tenant.html", {"request": request})

@app.get("/identification", response_class=HTMLResponse, tags=["identification-screen"], summary="Identification", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("Identification.html", {"request": request})

@app.get("/contact-details", response_class=HTMLResponse, tags=["contact-details-screen"], summary="Contact-Details", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("Contact.html", {"request": request})



@app.get("/get-a-tenant", response_class=HTMLResponse, tags=["tenant-details-ui"], summary="Get a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/Read.html", {"request": request})

@app.get("/create-a-tenant", response_class=HTMLResponse, tags=["tenant-details-ui"], summary="Create a tenant",include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/Insert.html", {"request": request})

@app.get("/modify-a-tenant", response_class=HTMLResponse,tags=["tenant-details-ui"], summary="Modify a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/Change.html", {"request": request})

@app.get("/modify-a-tenant-partially", response_class=HTMLResponse, tags=["tenant-details-ui"], summary="Modify a tenant patially",include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/ChangePartially.html", {"request": request})

@app.get("/get-all-tenants", response_class=HTMLResponse, tags=["tenant-details-ui"], summary="Get all tenants", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/ReadAll.html", {"request": request})

@app.get("/delete-a-tenant", response_class=HTMLResponse, tags=["tenant-details-ui"], summary="Delete a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/RemoveFromDB.html", {"request": request})

@app.get("/authorize-a-tenant", response_class=HTMLResponse, tags=["tenant-details-ui"], summary="Authorize a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Tenant/Authorize.html", {"request": request})







@app.get("/get-an-identification", response_class=HTMLResponse, tags=["identification-ui"], summary="Get an identification of a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/Read.html", {"request": request})

@app.get("/get-all-identifications", response_class=HTMLResponse, tags=["identification-ui"], summary="Get all identifications of a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/ReadAll.html", {"request": request})

@app.get("/create-an-identification", response_class=HTMLResponse, tags=["identification-ui"], summary="Create an identification of a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/Insert.html", {"request": request})

@app.get("/modify-an-identification", response_class=HTMLResponse, tags=["identification-ui"], summary="Modify an identification of a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/Change.html", {"request": request})

@app.get("/modify-an-identification-partially", response_class=HTMLResponse, tags=["identification-ui"], summary="Modify an identification of a tenant partially", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/ChangePartially.html", {"request": request})

@app.get("/authorize-an-identification", response_class=HTMLResponse, tags=["identification-ui"], summary="Authorize an identification of a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/Authorize.html", {"request": request})

@app.get("/delete-an-identification", response_class=HTMLResponse, tags=["identification-ui"], summary="Delete an identification of a tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Identification/RemoveFromDB.html", {"request": request})







@app.get("/get-a-contact", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Get a contact of tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/Read.html", {"request": request})

@app.get("/get-all-contacts", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Get all contacts of tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/ReadAll.html", {"request": request})

@app.get("/create-a-contact", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Create a contact of tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/Insert.html", {"request": request})

@app.get("/modify-a-contact", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Modify a contact of tenant", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/Change.html", {"request": request})

@app.get("/modify-a-contact-partially", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Modify a contact of tenant partially", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/ChangePartially.html", {"request": request})

@app.get("/authorize-a-contact", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Authorize a contact of tenant partially", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/Authorize.html", {"request": request})

@app.get("/delete-a-contact", response_class=HTMLResponse, tags=["contact-details-ui"], summary="Delete a contact of tenant partially", include_in_schema=True)
async def read_root(request: Request, current_user: str = Depends(get_current_user)):
    # Render the HTML file using Jinja2Templates
    return templates.TemplateResponse("/Contact/RemoveFromDB.html", {"request": request})




#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()


session_store ={}

@app.get("/login/user/{user-id}/password/{password}",
         response_model=Schemas.login_response, 
         tags=["login"], 
         summary="Validates the login credentials", 
         description="This API will helps to the user to get logged in")
def login(user_id:str,password:str, response : Response,db:Session=Depends(get_db)):
    login_flag = crud.login(db=db,user_id =user_id, password = password )
    if login_flag ==0:
        return {"login-flag" : 0}
    else:
        session_token = authentication.create_session_token({"username": user_id})
        session_store[session_token] = user_id
        response.set_cookie(key="session_id", value=session_token)
        return {"login-flag":1}

@app.post("/user",
          response_model=Schemas.user_respone, 
          tags=["login"], 
          summary="Create a user", 
          description="This API will helps in creating the new user", 
          status_code=201)
def post_user(user:Schemas.user_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.create_user(db=db,usr=user)
    except IntegrityError:
        db.rollback()


@app.post("/tenant-details",
          response_model=Schemas.tenants_basic_details_create_response, 
          tags=["tenant-details"], 
          summary="Create a tenant", 
          description="This API will helps in creating details of a tenant in the database", 
          status_code=201)
def post_tenant(tenant:Schemas.tenants_basic_details_create_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.create_tenant(db=db,tenant=tenant)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="tenant already exists for provided tenant Id"
        )


@app.get("/tenant-details/{tenant-id}",
         response_model=Schemas.tenants_basic_details_response, 
         tags=["tenant-details"], 
         summary="Get a tenant", 
         description="This API will helps in retrieving details of tenant from the database")
def get_tenant(tenant_id:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    db_tenant = crud.get_tenant(db=db,tenant_id =tenant_id )
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="tenant does not exists")
    return db_tenant


@app.put("/tenant-details/{tenant-id}",
         response_model=Schemas.tenants_basic_details_response, 
         tags=["tenant-details"], 
         summary="Update a tenant", 
         description="This API will helps in updating details of tenant in the database")
def put_tenant(tenant_id:int, tenant:Schemas.tenants_basic_details_create_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.put_tenant(db=db,tenant_id =tenant_id, tenant = tenant )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="tenant already exists"
        )


@app.patch("/tenant-details/{tenant-id}",
           response_model=Schemas.tenants_basic_details_response, 
           tags=["tenant-details"], 
           summary="Update a tenant partially", 
           description="This API will helps in partially updating the details of tenant in the database")
def patch_tenant(tenant_id:int, tenant:Schemas.tenants_basic_details_patch_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.patch_tenant(db=db,tenant_id =tenant_id, tenant = tenant )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="tenant already exists"
        )


@app.patch("/tenant-details/{tenant-id}/authorize",
           response_model=Schemas.tenants_basic_details_create_response, 
           tags=["tenant-details"], 
           summary="Approve a tenant", 
           description="This API will helps in approving tenant in the database")
def approve_tenant(tenant_id:int, tenant:Schemas.tenants_basic_details_authorize_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    return crud.approve_tenant(db=db,tenant = tenant,tenant_id =tenant_id )


@app.get("/tenant-details",
         response_model=List[Schemas.tenants_basic_details_response], 
         tags=["tenant-details"], 
         summary="Get all tenants", 
         description="This API will helps in retrieving details of all tenants from the database")
def get_tenants(db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    db_tenant = crud.get_tenants(db=db)
    if len(list(db_tenant))==0:
        raise HTTPException(status_code=404, detail="tenants does not exists")
    return db_tenant


@app.delete("/tenant-details/{tenant-id}", 
            tags=["tenant-details"], 
            summary="Delete a tenant",
            description="This API will helps in deleting details of tenant from the database", 
            status_code=204)
def del_tenant(tenant_id:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    crud.del_tenant(db=db,tenant_id =tenant_id )
    return None



@app.post("/tenant-details/{tenant-id}/identification",
          response_model=Schemas.tenants_legal_identification_create_response, 
          tags=["identification"], 
          summary="Create an identification", 
          description="This API will helps in creating identification details of a tenant in the database",
          status_code=201)
def post_idntcn(tenant_id:int, idntfcn:Schemas.tenants_legal_identification_create_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        resp = crud.create_idntfcn(db=db,tenant_id=tenant_id,idntfcn=idntfcn)
        tenant_resp = get_tenant(db=db, tenant_id=tenant_id)
        id_crt_resp = Schemas.tenants_legal_identification_create_response(tenant_id=resp.tenant_id, tenant_status=tenant_resp.tenant_status, tenant_legal_id_seq_number=resp.tenant_legal_id_seq_number,identification_record_status=resp.identification_record_status)
        return id_crt_resp
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Identification already exists"
        )
    except Exception:
        db.rollback()


@app.get("/tenant-details/{tenant-id}/identification/{id-seq-num}",
         response_model=Schemas.tenants_legal_identification_response, 
         tags=["identification"], 
         summary="Get an identification", 
         description="This API will helps in retrieving details of tenant's legal identification from the database")
def get_idntfcn(tenant_id:int, id_seq_num:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    db_tenant = crud.get_idntfcn(db=db,tenant_id =tenant_id, tenant_legal_id_seq_number = id_seq_num)
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="tenant identification does not exists")
    return db_tenant


@app.put("/tenant-details/{tenant-id}/identification/{id-seq-num}",
         response_model=Schemas.tenants_legal_identification_response, 
         tags=["identification"], 
         summary="Update an identification", 
         description="This API will helps in updating identification details in the database")
def put_idntfcn(tenant_id:int, id_seq_num:int, idntfcn:Schemas.tenants_legal_identification_create_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.put_idntfcn(db=db,tenant_id =tenant_id,tenant_legal_id_seq_number = id_seq_num, idntfcn = idntfcn )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Identification already exists"
        )
    except Exception:
        db.rollback()


@app.patch("/tenant-details/{tenant-id}/identification/{id-seq-num}",
           response_model=Schemas.tenants_legal_identification_response, 
           tags=["identification"], summary="Update an identification partially", 
           description="This API will helps in partially updating identification details in the database")
def patch_idntfcn(tenant_id:int, id_seq_num:int,idntfcn:Schemas.tenants_legal_identification_patch_request,db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.patch_idntfcn(db=db,tenant_id =tenant_id, tenant_legal_id_seq_number = id_seq_num, idntfcn = idntfcn )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Identification already exists"
        )
    except Exception:
        db.rollback()


@app.patch("/tenant-details/{tenant-id}/identification/{id-seq-num}/authorize",
           response_model=Schemas.tenants_legal_identification_create_response, 
           tags=["identification"], 
           summary="Approve an identification", 
           description="This API will helps in approving identification in the database")
def approve_idntfcn(tenant_id:int,id_seq_num:int, idntfcn:Schemas.tenants_basic_details_authorize_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
        resp = crud.approve_idntfcn(db=db, tenant_id =tenant_id , tenant_legal_id_seq_number = id_seq_num, idntfcn = idntfcn)
        tenant_resp = get_tenant(db=db, tenant_id=tenant_id)
        id_crt_resp = Schemas.tenants_legal_identification_create_response(tenant_id=resp.tenant_id, tenant_status=tenant_resp.tenant_status, tenant_legal_id_seq_number=resp.tenant_legal_id_seq_number,identification_record_status=resp.identification_record_status)
        return id_crt_resp


@app.get("/tenant-details/{tenant-id}/identification",
         response_model=List[Schemas.tenants_legal_identification_response], 
         tags=["identification"], 
         summary="Get all identifications", 
         description="This API will helps in retrieving details of tenant's all legal identifications from the database")
def get_idntfcns(tenant_id:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    db_tenant = crud.get_idntfcns(db=db,tenant_id =tenant_id)
    if len(list(db_tenant))==0:
        raise HTTPException(status_code=404, detail="identifications does not exists")
    return db_tenant


@app.delete("/tenant-details/{tenant-id}/identification/{id-seq-num}", 
            tags=["identification"], 
            summary="Delete an identification", 
            description="This API will helps in deleting details of tenant's legal identification from the database", 
            status_code=204)
def del_idntfcn(tenant_id:int,id_seq_num:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    crud.del_idntfcn(db=db,tenant_id =tenant_id, tenant_legal_id_seq_number= id_seq_num)
    return None




@app.post("/tenant-details/{tenant-id}/contact-details",
          response_model=Schemas.tenants_contact_details_create_response, 
          tags=["contact-details"], 
          summary="Create a contact", 
          description="This API will helps in creating contact details of a tenant in the database", 
          status_code=201)
def post_cntct(tenant_id:int, cntct:Schemas.tenants_contact_details_create_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        resp = crud.create_cntct(db=db,tenant_id=tenant_id,cntct=cntct)
        tenant_resp = get_tenant(db=db, tenant_id=tenant_id)
        cntct_crt_resp = Schemas.tenants_contact_details_create_response(tenant_id=resp.tenant_id, tenant_status=tenant_resp.tenant_status, tenant_contact_id=resp.tenant_contact_id,contact_record_status=resp.contact_record_status)
        return cntct_crt_resp
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="contact details already exists"
        )
    except Exception:
        db.rollback()


@app.get("/tenant-details/{tenant-id}/contact-details/{tenant-contact-id}",
         response_model=Schemas.tenants_contact_details_response, 
         tags=["contact-details"], 
         summary="Get a contact", 
         description="This API will helps in retrieving details of tenant's contact details from the database")
def get_cntct(tenant_id:int, tenant_contact_id:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    db_tenant = crud.get_cntct(db=db,tenant_id =tenant_id, tenant_contact_id = tenant_contact_id)
    if db_tenant is None:
        raise HTTPException(status_code=404, detail="tenant contact details does not exists")
    return db_tenant


@app.put("/tenant-details/{tenant-id}/contact-details/{tenant-contact-id}",
         response_model=Schemas.tenants_contact_details_response, 
         tags=["contact-details"], 
         summary="Update a contact", 
         description="This API will helps in updating contact details in the database")
def put_cntct(tenant_id:int, tenant_contact_id:int, cntct:Schemas.tenants_contact_details_create_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
   try:
       return crud.put_cntct(db=db,tenant_id =tenant_id, tenant_contact_id = tenant_contact_id , cntct = cntct)
   except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="contact details already exists"
        )
   except Exception:
        db.rollback()


@app.patch("/tenant-details/{tenant-id}/contact-details/{tenant-contact-id}",
           response_model=Schemas.tenants_contact_details_response, 
           tags=["contact-details"], 
           summary="Update a contact partially", 
           description="This API will helps in partially updating contact details in the database")
def patch_cntct(tenant_id:int,tenant_contact_id:int,cntct:Schemas.tenants_contact_details_patch_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        return crud.patch_cntct(db=db,tenant_id =tenant_id, tenant_contact_id = tenant_contact_id, cntct = cntct )
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="contact details already exists"
        )
    except Exception:
        db.rollback()


@app.patch("/tenant-details/{tenant-id}/contact-details/{tenant-contact-id}/authorize",
           response_model=Schemas.tenants_contact_details_create_response, 
           tags=["contact-details"], 
           summary="Approve a contact", 
           description="This API will helps in approving contact in the database")
def approve_cntct(tenant_id:int,tenant_contact_id:int,cntct : Schemas.tenants_basic_details_authorize_request, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
        resp = crud.approve_cntct(db=db, tenant_id =tenant_id, tenant_contact_id = tenant_contact_id , cntct = cntct)
        tenant_resp = get_tenant(db=db, tenant_id=tenant_id)
        cntct_crt_resp = Schemas.tenants_contact_details_create_response(tenant_id=resp.tenant_id, tenant_status=tenant_resp.tenant_status, tenant_contact_id=resp.tenant_contact_id,contact_record_status=resp.contact_record_status)
        return cntct_crt_resp


@app.get("/tenant-details/{tenant-id}/contact-details",
         response_model=List[Schemas.tenants_contact_details_response], 
         tags=["contact-details"], 
         summary="Get all contacts", 
         description="This API will helps in retrieving details of tenant's all contact details from the database")
def get_cntcts(tenant_id:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    db_tenant = crud.get_cntcts(db=db,tenant_id =tenant_id)
    if len(list(db_tenant))==0:
        raise HTTPException(status_code=404, detail="contacts does not exists")
    return db_tenant


@app.delete("/tenant-details/{tenant-id}/contact-details/{tenant-contact-id}", 
            tags=["contact-details"], 
            summary="Delete a contact", 
            description="This API will helps in deleting contact details of tenant from the database", 
            status_code=204)
def del_cntct(tenant_id:int,tenant_contact_id:int, db:Session=Depends(get_db), current_user: str = Depends(get_current_user)):
    crud.del_cntct(db=db,tenant_id =tenant_id, tenant_contact_id= tenant_contact_id)
    return None


@app.get("/log-out", tags=["login"], 
         summary="Log Out", 
         description="This API will helps user to log out")
async def logout(request: Request, response: Response, current_user: str = Depends(get_current_user)):
    session_token = request.cookies.get("session_id")
    if session_token:
        session_store.pop(session_token, None)
    response.delete_cookie("session_id")
    return {"detail": "Logged out successfully"}
