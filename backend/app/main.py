from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.heal import router as heal_router
from app.routes.status import router as status_router
from app.routes.diagnosis import router as diagnosis_router
from app.routes.recovery import router as recovery_router
from app.routes.ai import router as ai_router
from app.routes.self_healing import router as self_healing_router
from app.routes.logs import router as logs_router
from app.routes.history import router as history_router
from app.routes.auto_monitor import router as auto_monitor_router
from app.routes.dashboard import router as dashboard_router
from app.services.background_monitor import start_background_monitor


@asynccontextmanager
async def lifespan(app: FastAPI):
    start_background_monitor(30)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(heal_router)
app.include_router(status_router)
app.include_router(diagnosis_router)
app.include_router(recovery_router)
app.include_router(ai_router)
app.include_router(self_healing_router)
app.include_router(logs_router)
app.include_router(history_router)
app.include_router(auto_monitor_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"message": "Self Healing AI is running"}