from fastapi import FastAPI

app = FastAPI()

# Define a simple route
@app.get("/")
async def root():
    return {"message": "Hello World"}
