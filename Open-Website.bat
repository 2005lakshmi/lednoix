@echo off
setlocal

set PORT=8080

cd /d "%~dp0"

echo Starting local server on port %PORT% ...
start "Website Server - leave this window open, close it when done" cmd /k python -m http.server %PORT%

timeout /t 2 /nobreak >nul

echo Opening site in your browser ...
start http://localhost:%PORT%/index.html