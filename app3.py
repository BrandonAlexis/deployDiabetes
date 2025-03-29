from fastapi import FastAPI

from routers import routerPrediction


app = FastAPI()
app.include_router(routerPrediction.router)


if __name__=="__main__":
    app.run()
