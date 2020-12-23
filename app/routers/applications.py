import json

from fastapi import APIRouter, HTTPException
from typing import Optional
from .CreateReport import ReportOutput, CreateReport
import datetime
import logging
import pytz

# should base be just 'today', or include time stamp? e.g. '%Y%m%d%H%M%S'
today_base = int(datetime.datetime.now().strftime('%Y%m%d'))
report_sequence = 0

router = APIRouter()

applicationReportList = {'Claim': ['ClaimCSV', 'ClaimXLS', 'ClaimPDF'],
                         'Member': ['MemberTXT'],
                         'DrugList': ['DrugXLS', 'DrugPDF'],
                         'ProdList': ['prodListTXT', 'prodCSV'],
                         'Covid': ['Drug_Change_Class',
                                   'Weekly_Report_Change',
                                   'Current_Drug_Class',
                                   ]
                         }


def get_valid_outputs():
    return ['csv', 'xls', 'txt', 'pdf']


@router.get("/Applications", tags=["Applications"])
async def application_inventory():
    json_str = "[ "
    for key in applicationReportList.keys():
        json_str += '{} - {},'.format(key, ','.join(applicationReportList[key]))
        print(json.dumps(applicationReportList, indent=4, sort_keys=True))
    return [json.dumps(applicationReportList)]


@router.get("/Applications/_metrics", tags=["Applications"])
async def application_metrics():
    json_rv = ''
    for key in applicationReportList.keys():
        json_rv += ','.join(key)
    return [json_rv]


# http://0.0.0.0:7000/Applications/Covid/Reports/Drug_Change_Class?output=xls&limit=10
# note: output=csv is default value ...
@router.get("/Applications/{appName}/Reports/{reportName}", tags=["Applications"])
async def create_report(appName: str, reportName: str,
                        output: Optional[str] = None,
                        limit: Optional[int] = None, ):
    logging.info('AppName {}, ReportName: {}'.format(appName, reportName))

    # check to see we are passed valid AppName *and* ReportName
    if appName not in applicationReportList.keys():
        raise HTTPException(status_code=404, detail="AppName ({}) not found, cannot run any reports".format(appName))
    if reportName not in applicationReportList[appName]:
        raise HTTPException(status_code=404, detail="AppName ({}), cannot run report({})".format(appName,
                                                                                                 reportName))
    if output.lower() not in get_valid_outputs():
        raise HTTPException(status_code=404, detail="AppName ({}), valid outputs are {})".format(appName,
                                                                                                 get_valid_outputs()))
    report_sequence_id = getReportSequenceId()
    utc_now = datetime.datetime.utcnow()

    rv_json = '"appName": {}, "report": {}, "reportId": {}, "report_start_utc_time": {}'.format(
        appName, reportName, report_sequence_id, utc_now)
    logging.info('AppName {}, ReportName: {}, ReportStartUTCTime: {}'.format(appName, reportName, utc_now))
    logging.debug(rv_json)
    data_source = './Data/{}.dat'.format(reportName)

    # WARN: next line, is hokey ... we're going to eval on the fly.
    report_out = eval('ReportOutput.{}'.format(output.upper()))

    report_id = 123
    report_target = './Reports/{}.{}'.format(report_sequence_id, report_out.name)
    report = CreateReport(data_source, report_target, report_out, report_id)
    report.run()
    return {rv_json}


@router.get("/Applications/{appName}/Reports", tags=["Applications"])
async def create_report(appName: str):
    global report_sequence
    logging.info('AppName {} report inquiry'.format(appName))

    # check to see we are passed valid AppName *and* ReportName
    if appName not in applicationReportList.keys():
        raise HTTPException(status_code=404, detail="AppName ({}) not found, cannot run any reports".format(appName))

    # we now have valid AppName *and* ReportName, assign this request to a ReportId
    utc_now = datetime.datetime.utcnow()
    rv_json = '"appName": {}, "available reports": {}'.format(appName, ','.join(applicationReportList[appName]))
    logging.info('AppName {} "available reports": {}'.format(appName, ','.join(applicationReportList[appName])))
    logging.debug(rv_json)
    return {rv_json}


def getReportSequenceId():
    global today_base, report_sequence
    # we now have valid AppName *and* ReportName, assign this request to a ReportId
    report_sequence_id = '{}_{:0>6d}'.format(today_base, report_sequence)
    report_sequence += 1
    return report_sequence_id
