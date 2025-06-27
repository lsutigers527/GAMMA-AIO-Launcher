@echo off
REM Build a standalone exe for gamma_aio_launcher.py
pip install pyinstaller
pyinstaller --onefile --windowed gamma_aio_launcher.py
pause