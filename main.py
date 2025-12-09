from fastapi import FastAPI

app = FastAPI()  # Initialize FastAPI application


@app.get("/")  # Define a GET endpoint at the root URL
async def read_root():
    return {"message": "Hello, World!"}  # Return a simple JSON response


@app.get('/greet')  # Defining a GET endpoint
async def greet_name(name: str) -> dict:
    # Return a greeting message with the provided name
    return {"greeting": f"Hello, {name}!"}
