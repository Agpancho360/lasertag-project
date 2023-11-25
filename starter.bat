:: starter.bat
@echo off
start cmd /k python udp_server.py
start cmd /k python udp_client.py
start python main.py
start python pythonTrafficGenerator.py
@REM cmd /k