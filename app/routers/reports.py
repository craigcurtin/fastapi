# from fastapi import APIRouter
#
# router = APIRouter()
#
#
# @router.get("/Applications/{appName}/Reports/{reportName}", tags=["reports"])
# async def report_create( appName : str, reportName : str):
#     return [ { "AppName": appName }, { "reportName" : reportName }]
#
#
# @router.get("/Applications/{appName}/Report/Status/{reportId}", tags=["reports"])
# async def report_status():
#     return [ { "AppName" : appName }, { "reportId" : reportId } ]
