This project uses Python 3.8 and FastAPI to create a WebService demo for Pharmacy Reporting.

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

For details on FastAPI:
Documentation: https://fastapi.tiangolo.com
Source Code: https://github.com/tiangolo/fastapi

FastAPI has some 'self-documenting' features that ease its usage and deployment with APIM's Portal (https://test-developer.ssnc.cloud).

By default, the code executes on http://0.0.0.0:7000

To see the Swagger/OpenAPI interface:
http://0.0.0.0:7000/docs

To see the Alternative ReDoc interface:
http://0.0.0.0:7000/redoc

To see the Swagger/OpenAPI JSON doc (for uploading to APIM):
http://0.0.0.0:7000/openapi.json

#some sample URLs to test the functionality of the Reporting WebService
http://0.0.0.0:7000/Applications/Covid/Reports/Drug_Change_Class?output=csv

#generate .xls reports
http://0.0.0.0:7000/Applications/Covid/Reports/Drug_Change_Class?output=xls

#generate an inventory of Applications/Reports that can be generated
http://0.0.0.0:7000/Applications

... stay tuned, more to come ...