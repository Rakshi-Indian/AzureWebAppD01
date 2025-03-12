import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

app = FastAPI()

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    valid_username = "admin"
    valid_password = "password"

    if credentials.username != valid_username or credentials.password != valid_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI on Azure Web App"}

@app.get("/secure-endpoint")
def secure_endpoint(username: str = Depends(authenticate)):
    return {"message": f"Hello, {username}. You have accessed a secure endpoint."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
