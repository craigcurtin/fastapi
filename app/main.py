import uvicorn
import logging
from fastapi import Depends, FastAPI
from ps_logger import setup_logger
from app.dependencies import get_query_token, get_token_header
from app.internal import admin
from app.routers import applications, items, users, reports

# bypass getting the header token when in Dev ...
forget_query_token_for_now = True

if forget_query_token_for_now:
    app = FastAPI()
else:
    app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(applications.router)
# app.include_router(reports.router)
app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    #    uvicorn.run(app, host="0.0.0.0", port=7000, log-level=logging.DEBUG)
    setup_logger('report_service', logging.DEBUG)
    logging.info("Web Server starting up ...")
    uvicorn.run(app, host="0.0.0.0",
                port=7000,
                log_level=logging.DEBUG,
                debug=True,
                # reload=True,
                )
