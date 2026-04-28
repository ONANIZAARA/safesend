from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import messages, numbers, reports

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SafeSend API",
    description="Offline + Scam-Aware Payment Protection System for Africa",
    version="1.0.0"
)

# Fix CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes
app.include_router(messages.router)
app.include_router(numbers.router)
app.include_router(reports.router)

# Serve frontend
@app.get("/")
def home():
    return FileResponse("index.html")