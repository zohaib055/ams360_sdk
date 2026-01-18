# CLI

python -m ams360_sdk.cli --list-ops
python -m ams360_sdk.cli --agency-info


# ENV Vars

$env:AMS360_AGENCY_NO="8880006-1"
$env:AMS360_LOGIN_ID="testuser"
$env:AMS360_PASSWORD="yourpass"
# optional when you mapped "Specific Employee = WSAPI"
$env:AMS360_EMPLOYEE_CODE=""