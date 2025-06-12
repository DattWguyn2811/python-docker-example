from fastapi import FastAPI

app = FastAPI()

# Define a simple route
## This route will respond with a JSON message when accessed
@app.get("/")
async def root():
    return {"message": "Hello World"}
