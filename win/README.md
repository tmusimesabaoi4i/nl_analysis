## 環境の構築
基本的にwindowsでもubuntuでも仮想環境を構築する必要があります。
```
set VENV=py39
python -m venv C:\Users\yohei\python_env\%VENV%
```
## ライブラリのインストール
```
set VENV=py39
CALL C:\Users\yohei\python_env\%VENV%\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel

python -m pip install matplotlib
python -m pip install pandas
python -m pip install openpyxl
```
## 計測手法
- [version1](/version1/README.md)
