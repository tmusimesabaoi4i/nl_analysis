@echo off
setlocal enabledelayedexpansion
cd %~dp0

CALL C:\Users\yohei\python_env\py39\Scripts\activate.bat
python -m pip install -U pip
python -m pip install matplotlib
python -m pip install pandas
python -m pip install openpyxl
