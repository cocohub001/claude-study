from fastapi import FastAPI
from src.routers import admin, gateway

app = FastAPI(title="Python API Gateway")

app.include_router(admin.router)
app.include_router(gateway.router)


@app.get("/health")
async def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
