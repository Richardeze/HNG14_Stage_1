from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine, get_db
from schemas import ProfileCreate, ProfileResponse
from services.external_apis import fetch_external_data
from utils.classification import get_age_group
from uuid6 import uuid7
import os

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root
@app.get("/")
def root():
    return {
        "status": "success",
        "message": "HNG Stage 1 API is running"
    }

# ✅ TEST ROUTE (VERY IMPORTANT)
@app.get("/test/{name}")
async def test_api(name: str):
    data = await fetch_external_data(name)
    return {
        "status": "success",
        "data": data
    }

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "message": "Invalid input"
        }
    )

@app.post("/api/profiles", status_code=201)
async def create_profile(payload: ProfileCreate, db: Session = Depends(get_db)):
    name = payload.name.lower().strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail= "Missing or empty name"
        )

    existing_profile = db.query(models.Profile).filter(models.Profile.name == name).first()
    if existing_profile:
        return {
            "status": "success",
            "message": "Profile already exists",
            "data": ProfileResponse.model_validate(existing_profile)
        }

    data = await fetch_external_data(name)

    new_profile = models.Profile(
        id=str(uuid7()),
        name=name,
        gender=data["gender"],
        gender_probability=data["gender_probability"],
        sample_size=data["sample_size"],
        age=data["age"],
        age_group=data["age_group"],
        country_id=data["country_id"],
        country_probability=data["country_probability"],
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return {
        "status": "success",
        "data": ProfileResponse.model_validate(new_profile)
    }

@app.get("/api/profiles/{id}")
def get_profile(id: str, db: Session = Depends(get_db)):

    profile = db.query(models.Profile).filter(models.Profile.id == id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return {
        "status": "success",
        "data": ProfileResponse.model_validate(profile)
    }

@app.get("/api/profiles")
def get_profiles(
    gender: str = None,
    country_id: str = None,
    age_group: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(models.Profile)

    if gender:
        query = query.filter(models.Profile.gender.ilike(gender))

    if country_id:
        query = query.filter(models.Profile.country_id.ilike(country_id))

    if age_group:
        query = query.filter(models.Profile.age_group.ilike(age_group))

    profiles = query.all()

    return {
        "status": "success",
        "count": len(profiles),
        "data": [
            {
                "id": p.id,
                "name": p.name,
                "gender": p.gender,
                "age": p.age,
                "age_group": p.age_group,
                "country_id": p.country_id
            }
            for p in profiles
        ]
    }

@app.delete("/api/profiles/{id}", status_code=204)
def delete_profile(id: str, db: Session = Depends(get_db)):

    profile = db.query(models.Profile).filter(models.Profile.id == id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    db.delete(profile)
    db.commit()

    return

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port)
