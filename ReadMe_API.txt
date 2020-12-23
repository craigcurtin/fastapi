
Below is copied from @Chaudhary, Pradeep Kumar pdf 'requirments' emailed to team 2020-12-17

GET, POST /Applications/{ApplicationName}/Reports/{ReportName}
returns 200, ReportId

Create:
GET, POST /Applications/{ApplicationName}/Reports/{ReportName}

Status:
GET, POST /Applications/{ApplicationName}/Report/{ReportId}
returns status

GET, POST /reports
Top level API. Lists all report definitions. User can define new report. Application will be one of the attribute in request body

GET, POST /reports/applications/{APP_NAME}
List all report definitions for an app. User can define new report.

PUT /reports?type=<REPORT_TYPE>&status=<Y|N>
Enable or disable reports by type. Reports will have broad categorization. (Summary, Details, etc.) Required only in case of executing reports in RxNova DB

GET /reports/applications/{APP_NAME}/{reportName}?[report parameters] Initiates report request. Any report parameters can be added as request params. May be converted to POST if PHI / PII data is included.

GET /reports/applications/{APP_NAME}/instances
List all current requested reports for an app. If required, can be filtered based on logged in user. Each item has metadata like ID, name, requested timestamp, requested by, status, type

GET /reports/applications/{APP_NAME}/{reportName}/{id}
Details about a requested report. Contains link to download report if processed

DELETE /reports/applications/{APP_NAME}/{reportName}/{id} Delete a requested report. Allowed only if report is not yet processed.

some sample RESTful calls from Chrome/Browser:k
k
http://0.0.0.0:7000/Applications/Covid/Reports/Drug_Change_Class?output=csv

response:
["\"appName\": Covid, \"report\": Drug_Change_Class, \"reportId\": 20201223_000002, \"report_start_utc_time\": 2020-12-23 17:28:39.585135"]

Chrome:kkjkk
kkkk
http://0.0.0.0:7000/Applications
"{\"Claim\": [\"ClaimCSV\", \"ClaimXLS\", \"ClaimPDF\"], \"Member\": [\"MemberTXT\"], \"DrugList\": [\"DrugXLS\", \"DrugPDF\"], \"ProdList\": [\"prodListTXT\", \"prodCSV\"], \"Covid\": [\"Drug_Change_Class\", \"Weekly_Report_Change\", \"Current_Drug_Class\"]}"]


