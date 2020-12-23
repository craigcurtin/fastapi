This project uses Python 3.8 and FastAPI to create a WebService demo for Pharmacy Reporting.

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

For details on FastAPI:
Documentation: https://fastapi.tiangolo.com
Source Code: https://github.com/tiangolo/fastapi

FastAPI has some 'self-documenting' features that ease its usage and deployment with APIM's Portal (https://test-developer.ssnc.cloud).


| To run on your desktop |
| ------ |
| $ git clone https://code.ssnc.global/CCurtin/fastapi |
| $ pip install -r requirements.txt --index-url https://artifacts-scm.dstcorp.net/artifactory/api/pypi/pypi-repos/simple|
| Launch PyCharm (Python IDE), create a virtual env, create a ‘run’ environment configuration |
| Run, by default the code runs on http://0.0.0.0:7000 … if you run, the below links will work as is |

```
 To run on your desktop 
 $ git clone https://code.ssnc.global/CCurtin/fastapi 
 $ pip install -r requirements.txt --index-url https://artifacts-scm.dstcorp.net/artifactory/api/pypi/pypi-repos/simple
 Launch PyCharm (Python IDE), create a virtual env, create a ‘run’ environment configuration 
 Run, by default the code runs on http://0.0.0.0:7000 … if you run, the below links will work as is 
```

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