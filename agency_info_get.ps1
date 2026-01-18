$uri = "https://wsapi.ams360.com/v3/WSAPIService.svc"

$headers = @{
  "Content-Type" = "text/xml; charset=utf-8"
  "SOAPAction"   = "http://www.WSAPI.AMS360.com/v3.0/WSAPIServiceContract/AgencyInfoGet"
}

# Read ticket from file (created by your login step)
$ticketPath = ".\ams360_ticket.txt"
if (-not (Test-Path $ticketPath)) {
  Write-Host "❌ Ticket file not found: $ticketPath" -ForegroundColor Red
  exit 1
}

$ticket = (Get-Content $ticketPath -Raw).Trim()
if ([string]::IsNullOrWhiteSpace($ticket)) {
  Write-Host "❌ Ticket file is empty: $ticketPath" -ForegroundColor Red
  exit 1
}

# Load XML template and inject ticket
$xmlTemplate = Get-Content ".\agency_info_get.xml" -Raw
$body = $xmlTemplate.Replace("{{TICKET}}", $ticket)

$outPath = ".\agency_info_get_response.xml"

try {
  $resp = Invoke-WebRequest -UseBasicParsing -Uri $uri -Method Post -Headers $headers -Body $body -ErrorAction Stop
  $xmlText = $resp.Content
}
catch {
  # Capture SOAP fault body (important)
  $xmlText = $null
  if ($_.Exception.Response -and $_.Exception.Response.GetResponseStream()) {
    $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
    $xmlText = $reader.ReadToEnd()
  }

  Write-Host "❌ Request failed. SOAP response:" -ForegroundColor Red
  if ($xmlText) {
    Set-Content -Path $outPath -Value $xmlText -Encoding UTF8
    Write-Host "Saved to $outPath"
    Write-Output $xmlText
  } else {
    Write-Host $_
  }
  exit 1
}

Set-Content -Path $outPath -Value $xmlText -Encoding UTF8
Write-Host "✅ Saved response to $outPath" -ForegroundColor Green

# Optional: print a small snippet so you can confirm it's not a fault
if ($xmlText -match "<s:Fault" -or $xmlText -match "<Fault") {
  Write-Host "⚠️ Response contains a SOAP Fault. Check the saved XML." -ForegroundColor Yellow
} else {
  Write-Host "✅ Response looks successful (no Fault detected)." -ForegroundColor Green
}
