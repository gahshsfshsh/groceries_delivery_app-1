from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
      title="Groceries Delivery App Backend",
      description="Backend API for groceries delivery Flutter app",
      version="1.0.0",
)

origins = [
      "*"
]

app.add_middleware(
      CORSMiddleware,
      allow_origins=origins,
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)

@app.get("/")
def read_root():
      return {"status": "ok", "message": "Groceries Delivery API is running"}
  
