from fastapi import FastAPI
import app.api.routers.root as rootRouter

app = FastAPI()
app.include_router(rootRouter.router)



