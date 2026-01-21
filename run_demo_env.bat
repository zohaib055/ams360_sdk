@echo off
setlocal

REM Fill in your AMS360 credentials here.
set "AMS360_AGENCY_NO=8880006-1"
set "AMS360_LOGIN_ID=bizassure"
set "AMS360_PASSWORD=wK1atfrjjY7"
set "AMS360_EMPLOYEE_CODE="

REM Optional: reuse a ticket instead of logging in.
REM set "AMS360_TICKET=YOUR_TICKET"

REM Optional: override endpoint or TLS behavior.
REM set "AMS360_ENDPOINT_URL=https://wsapi.ams360.com/v3/WSAPIService.svc"
REM set "AMS360_VERIFY_TLS=true"

REM Optional: pass a request payload as JSON.
REM set "AMS360_DEMO_PAYLOAD_JSON={\"NamePrefix\":\"A\"}"

REM Test login once and reuse the ticket for the demo.
set "LOGIN_JSON=%TEMP%\ams360_login.json"
python dist_ams360_sdk\demos\login_demo.py > "%LOGIN_JSON%"
if errorlevel 1 (
  echo Login failed. Aborting demo.
  exit /b 1
)
for /f "usebackq delims=" %%A in (`python -c "import json; print(json.load(open(r'%LOGIN_JSON%'))['ticket'])"`) do set "AMS360_TICKET=%%A"
del "%LOGIN_JSON%"

REM Run a demo (change the script name as needed).
python dist_ams360_sdk\demos\agency_info_get.py

endlocal
