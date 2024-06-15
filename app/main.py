from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from Duck_Timer.app.routers import timer
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="Duck_Timer/app/static"), name="static")

app.include_router(timer.router)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("Duck_Timer/app/templates/index.html") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")