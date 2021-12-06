# IN CASE OF PING
```python
import subprocess
import re

packets_num = 20                    # パケットの数
byte_num = 65500                    # パケットのバイト数
ip_addr = '192.168.1.38'            # 送り先のIPアドレス

# 実行するコマンド
cmd = 'ping' + \
        ' -n ' + str(packets_num) + \
        ' -l ' + str(byte_num) + \
        ' ' + ip_addr

returncode = subprocess.check_output(cmd, shell=True)    # 実行した結果を格納
jp_code = returncode.decode('cp932')                     # 日本語に直す
jp_ping_info = re.sub('.+\r\n','',jp_code,2+packets_num) # 最後の部分のみ取り出す

jp_ping_result = list()                                  # 結果を格納するリスト
tmp = str()
for text in jp_ping_info :
    if (text in ['0', '1', '2', '3',\
             '4', '5', '6', '7', '8', '9', '.']) :
        tmp += text
    elif tmp != '' :
        jp_ping_result.append(tmp)
        tmp = str()
jp_ping_result = [int(tmp) for tmp in jp_ping_result]    # 文字列を数字に変換する

# 0で割る場合は除く
if jp_ping_result[4] != 0.0 :
    min_late = byte_num * 2.0 * 10**3 / jp_ping_result[4]
else :
    min_late = 0.0

if jp_ping_result[5] != 0.0 :
    max_late = byte_num * 2.0 * 10**3 / jp_ping_result[5]
else :
    max_late = 0.0

if jp_ping_result[6] != 0.0 :
    mean_late = byte_num * 2 * 10**3 / jp_ping_result[6]
else :
    mean_late = 0.0

jp_ping_result_dict = {
'パケット受信数':jp_ping_result[0],
'パケット送信数':jp_ping_result[1],
'パケット損失数':jp_ping_result[2],
'PACKET_LOSS_RATE':jp_ping_result[3],
'RTT_MIN':jp_ping_result[4], # [mm sec]
'RTT_MAX':jp_ping_result[5], # [mm sec]
'RTT_AVE':jp_ping_result[6], # [mm sec]
'MAX_BANDWIDTH':min_late/10**6, # [Mega byte / sec]
'MIN_BANDWIDTH':max_late/10**6, # [Mega byte / sec]
'AVE_BANDWIDTH':mean_late/10**6 # [Mega byte / sec]
}

print(jp_ping_result_dict)
```

上記プログラムを実行した場合、以下のような結果になる。

```
{'パケット受信数': 20, 'パケット送信数': 20, 'パケット損失数': 0, 'PACKET_LOSS_RATE': 0, 'RTT_MIN': 2, 'RTT_MAX': 2, 'RTT_AVE': 2, 'MAX_BANDWIDTH': 65.5, 'MIN_BANDWIDTH': 65.5, 'AVE_BANDWIDTH': 65.5}
```

# IN CASE OF SOCKET
### CLIENT
```python
```
### SERVER
```python
```
### RESULT
```
```
