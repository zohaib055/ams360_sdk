# login.ps1 — AMS360 WSAPI v3 Login (no EmployeeCode)

$uri = "https://wsapi.ams360.com/v3/WSAPIService.svc"

$headers = @{
    "Content-Type" = "text/xml; charset=utf-8"
    "SOAPAction"   = "http://www.WSAPI.AMS360.com/v3.0/WSAPIServiceContract/Login"
}

$body = Get-Content ".\login.xml" -Raw

try {
    $response = Invoke-WebRequest `
        -UseBasicParsing `
        -Uri $uri `
        -Method Post `
        -Headers $headers `
        -Body $body `
        -ErrorAction Stop

    $xmlText = $response.Content
}
catch {
    # Even failures return SOAP XML — capture it
    $stream = $_.Exception.Response.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($stream)
    $xmlText = $reader.ReadToEnd()

    Write-Host "❌ SOAP Fault:" -ForegroundColor Red
    Write-Output $xmlText
    exit 1
}

Write-Host "✅ Raw Response:" -ForegroundColor Green
Write-Output $xmlText

# Parse XML
[xml]$xml = $xmlText

# Extract Ticket (WSAPI v3)
$ticketNode = $xml.SelectSingleNode("//*[local-name()='Ticket']")

if (-not $ticketNode -or [string]::IsNullOrWhiteSpace($ticketNode.InnerText)) {
    Write-Host "❌ Ticket not found in response" -ForegroundColor Red
    exit 1
}

$ticket = $ticketNode.InnerText.Trim()

Write-Host "`n✅ WSAPI Ticket:" -ForegroundColor Green
Write-Host $ticket

# Save ticket for later calls
Set-Content -Path ".\ams360_ticket.txt" -Value $ticket -Encoding UTF8
Write-Host "✅ Ticket saved to ams360_ticket.txt" -ForegroundColor Green
