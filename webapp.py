from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(title="Azure WebApp with Swagger",
              description="A simple FastAPI app deployed on Azure",
              version="1.0")

# Sample endpoint
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Azure Web App running FastAPI with Swagger!"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "Healthy"}

# Run the application using Uvicorn (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
