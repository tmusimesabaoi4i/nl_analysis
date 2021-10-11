import subprocess

cmd = 'ECHO %date% %time%' # 実行するコマンド

returncode = subprocess.check_output(cmd, shell=True) # 実行した結果を格納
jp_code = returncode.decode('cp932') # 日本語に直す
print(jp_code)
