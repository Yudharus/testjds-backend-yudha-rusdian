from fastapi import FastAPI
from controllers import data_controller
import models.model as models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(data_controller.router)

# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
