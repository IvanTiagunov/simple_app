import uvicorn
from fastapi import FastAPI
from tasks import task_router
from users import user_router

app = FastAPI()
app.include_router(task_router)
app.include_router(user_router)


@app.get("/")
def welcome() -> dict:
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
