import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(
    title="Azure WebApp with Swagger and Basic Authentication",
    description="A FastAPI app deployed on Azure with Basic Authentication",
    version="1.0"
)

security = HTTPBasic()

# Get credentials from environment variables (default values for local testing)
VALID_USERNAME = os.getenv("BASIC_AUTH_USERNAME", "admin")
VALID_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "password123")

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """Authenticate user with Basic Auth"""
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/", dependencies=[Depends(authenticate)], tags=["Root"])
def read_root():
    """Root endpoint - Requires authentication"""
    return {"message": "Authenticated access granted!"}

@app.get("/health", tags=["Health"])
def health_check():
    """Health check - No authentication required"""
    return {"status": "Healthy"}

# Run the application using Uvicorn (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
