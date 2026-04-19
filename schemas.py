from pydantic import BaseModel
from datetime import datetime

class ProfileCreate(BaseModel):
    name: str

class ProfileResponse(BaseModel):
    id: str
    name: str
    gender: str
    gender_probability: float
    sample_size: int
    age: int
    age_group: str
    country_id: str
    country_probability: float
    created_at: datetime

    class Config:
        from_attributes = True

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)

        # Convert datetime to ISO 8601 with Z
        if data.get("created_at"):
            data["created_at"] = data["created_at"].isoformat().replace("+00:00", "Z")

        return data