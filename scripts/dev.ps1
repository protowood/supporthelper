$env:PYTHONUTF8=1
$env:PYTHONIOENCODING='utf-8'

# Start backend
Write-Host 'Starting backend on http://127.0.0.1:8080'
python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8080 --reload
