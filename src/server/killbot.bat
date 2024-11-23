@echo off

for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8080') do (
    set "PID=%%a"
    goto found
)

echo  No robot running @ port 8080.
exit /b

:found
echo  Scanning... Deviant found @ 8080:
netstat -ano | findstr :8080

set /p CONFIRM= Do you want to lose all the moments like tears in rain? (yes/no): 

if /i "%CONFIRM%"=="yes" (
    taskkill /PID %PID% /F
    echo Process %PID% has been eliminated. Mission complete.
) else (
    echo Process %PID% remains operational. No action taken.
)
