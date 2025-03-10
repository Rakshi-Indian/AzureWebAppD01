from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(title="Azure WebApp with Swagger",
              description="A simple FastAPI app deployed on Azure",
              version="1.0")

# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Azure Web App running FastAPI with Swagger!"}

# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "Healthy"}

# API data endpoint
@app.get("/api/data", tags=["API"])
def get_data():
    return {"data": "This is your API response data."}

# Run the application using Uvicorn (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
