🚀 HNG14 Stage 1 – Data Persistence & API Design (FastAPI)

This project is a backend API built with FastAPI for the HNG Stage 1 task.
It integrates multiple external APIs, processes the data, stores it in a database, and exposes endpoints to manage user profiles.

📌 Features
🔗 Integration with 3 external APIs:
Genderize (gender prediction)
Agify (age prediction)
Nationalize (country prediction)
🧠 Data classification:
Age groups (child, teenager, adult, senior)
Country selection based on highest probability
💾 Data persistence using SQLAlchemy
♻️ Idempotency (prevents duplicate records)
🔍 Filtering support on GET requests
❌ Proper error handling (HNG-compliant format)
🌐 CORS enabled for public access
🛠 Tech Stack
FastAPI
SQLAlchemy
SQLite (can be switched to MySQL/Postgres)
HTTPX (for external API calls)
Pydantic
UUID v7 (uuid6 library)
📡 API Endpoints
1️⃣ Create Profile

POST /api/profiles

Request:
{
  "name": "emmanuel"
}
Response:
{
  "status": "success",
  "data": {
    "id": "018f...",
    "name": "emmanuel",
    "gender": "male",
    "gender_probability": 0.99,
    "sample_size": 1234,
    "age": 25,
    "age_group": "adult",
    "country_id": "NG",
    "country_probability": 0.85,
    "created_at": "2026-04-01T12:00:00Z"
  }
}
Idempotency:

If the name already exists:

{
  "status": "success",
  "message": "Profile already exists",
  "data": { ... }
}
2️⃣ Get Single Profile

GET /api/profiles/{id}

3️⃣ Get All Profiles

GET /api/profiles

Optional Filters:
gender
country_id
age_group

Example:

/api/profiles?gender=male&country_id=NG
4️⃣ Delete Profile

DELETE /api/profiles/{id}

Response:

204 No Content
⚠️ Error Handling

All errors follow this format:

{
  "status": "error",
  "message": "Error message"
}
Common Errors:
400 → Missing or empty name
422 → Invalid input type
404 → Profile not found
502 → External API failure
🌍 External APIs Used
https://api.genderize.io
https://api.agify.io
https://api.nationalize.io
🧪 Running Locally
1. Clone repo
git clone https://github.com/Richardeze/HNG14_Stage_1.git
cd your-repo
2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run server
uvicorn main:app --reload
5. Open docs
http://127.0.0.1:8000/docs
🚀 Deployment

This API is deployed on:

🚀 HNG14 Stage 1 – Data Persistence & API Design (FastAPI)

This project is a backend API built with FastAPI for the HNG Stage 1 task.
It integrates multiple external APIs, processes the data, stores it in a database, and exposes endpoints to manage user profiles.

📌 Features
🔗 Integration with 3 external APIs:
Genderize (gender prediction)
Agify (age prediction)
Nationalize (country prediction)
🧠 Data classification:
Age groups (child, teenager, adult, senior)
Country selection based on highest probability
💾 Data persistence using SQLAlchemy
♻️ Idempotency (prevents duplicate records)
🔍 Filtering support on GET requests
❌ Proper error handling (HNG-compliant format)
🌐 CORS enabled for public access
🛠 Tech Stack
FastAPI
SQLAlchemy
SQLite (can be switched to MySQL/Postgres)
HTTPX (for external API calls)
Pydantic
UUID v7 (uuid6 library)
📡 API Endpoints
1️⃣ Create Profile

POST /api/profiles

Request:
{
  "name": "emmanuel"
}
Response:
{
  "status": "success",
  "data": {
    "id": "018f...",
    "name": "emmanuel",
    "gender": "male",
    "gender_probability": 0.99,
    "sample_size": 1234,
    "age": 25,
    "age_group": "adult",
    "country_id": "NG",
    "country_probability": 0.85,
    "created_at": "2026-04-01T12:00:00Z"
  }
}
Idempotency:

If the name already exists:

{
  "status": "success",
  "message": "Profile already exists",
  "data": { ... }
}
2️⃣ Get Single Profile

GET /api/profiles/{id}

3️⃣ Get All Profiles

GET /api/profiles

Optional Filters:
gender
country_id
age_group

Example:

/api/profiles?gender=male&country_id=NG
4️⃣ Delete Profile

DELETE /api/profiles/{id}

Response:

204 No Content
⚠️ Error Handling

All errors follow this format:

{
  "status": "error",
  "message": "Error message"
}
Common Errors:
400 → Missing or empty name
422 → Invalid input type
404 → Profile not found
502 → External API failure
🌍 External APIs Used
https://api.genderize.io
https://api.agify.io
https://api.nationalize.io
🧪 Running Locally
1. Clone repo
git clone https://github.com/Richardeze/HNG14_Stage_1.git
cd your-repo
2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run server
uvicorn main:app --reload
5. Open docs
http://127.0.0.1:8000/docs
🚀 Deployment

This API is deployed on: https://huggingface.co/spaces/RichardEze/HNG14_Stage_1









