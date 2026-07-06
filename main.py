from fastapi import FastAPI

app = FastAPI(title="generated-app")

@app.get('/items')
async def list_items():
    return []
