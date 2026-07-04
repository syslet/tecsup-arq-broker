@‌echo off
setlocal

REM ==========================================================
REM Abre 5 ventanas CMD y ejecuta comandos Python especificos
REM ==========================================================

cd /d "%~dp0"

start "BrokerServer" cmd /k "python broker_server.py"
start "Producer #1" cmd /k "python producer.py 5001"
start "Producer #2" cmd /k "python producer.py 5002"
start "Consumer #1" cmd /k "python consumer.py"
start "Consumer #2" cmd /k "python consumer.py"
start "Consumer #3" cmd /k "python consumer.py"

endlocal