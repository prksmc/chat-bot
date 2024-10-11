from fastapi import FastAPI

@app.get("/testing")
async def testing():
    return {"message": "It works!"}
