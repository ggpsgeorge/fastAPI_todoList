from fastapi import FastAPI
import app.api.routers.root as rootRouter
import app.api.routers.task_routes as taskRouter

app = FastAPI()
app.include_router(rootRouter.router)
app.include_router(taskRouter.router)


