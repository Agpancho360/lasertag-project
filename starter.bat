:: starter.bat
@echo off
start python main.py
start cmd /k python udp_server.py
start cmd /k python udp_client.py
start python pythonTrafficGenerator.py
@REM cmd /k