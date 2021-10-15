import subprocess
import re

packets_num = 10 # パケットの数
byte_num = 60000 # パケットのバイト数 = 60kB
ip_addr = '192.168.1.18' # 送り先のIPアドレス
cmd = 'ping -n ' + str(packets_num) + ' -l ' + str(byte_num) + ' ' + ip_addr # 実行するコマンド

returncode = subprocess.check_output(cmd, shell=True) # 実行した結果を格納
jp_code = returncode.decode('cp932') # 日本語に直す

jp_png_info = re.sub('.+\r\n','',jp_code,2+packets_num)

#################################
# パケット受信数
# パケット送信数
# パケット損失数
# パケット損失率
# ラウンドトリップ最小時間
# ラウンドトリップ最大時間
# ラウンドトリップ平均時間
# の順にpingの結果が格納される
#################################
result = [[],[],[],[],[],[],[]]

n_result = 0
k = 0
flag = 1

for i in jp_png_info :
    if (i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) :
        result[n_result].append(i)
        flag = 0
    elif flag == 0:
        n_result = n_result + 1
        flag = 1

n_result = 0
result_num = []
for l in result :
    s = 0
    ans_num = 0
    for num_10 in l :
        ans_num = ans_num + int(num_10)*10**(len(l)-s-1)
        s = s + 1
    result_num.append(ans_num)

print('#########################################################################')
print('( パケット受信数'+str(result_num[0])+' [個] ',end=' , ')
print('パケット送信数'+str(result_num[1])+' [個] ',end=' , ')
print('パケット損失数'+str(result_num[2])+' [個] ',end=' , ')
print('パケット損失率'+str(result_num[3])+' [%] ',end=' , ')
print('ラウンドトリップ最小時間'+str(result_num[4])+' [msec] ',end=' , ')
print('ラウンドトリップ最大時間'+str(result_num[5])+' [msec] ',end=' , ')
print('ラウンドトリップ平均時間'+str(result_num[6])+' [msec] )')
print('#########################################################################')
min_late = byte_num * 8 * 2 * 10**3 / result_num[4]
max_late = byte_num * 8 * 2 * 10**3 / result_num[5]
mean_late = byte_num * 8 * 2 * 10**3 / result_num[6]
print('最速帯域'+str(min_late/10**6)+' [M bit/sec] ',end=' , ')
print('最遅帯域'+str(max_late/10**6)+' [M bit/sec] ',end=' , ')
print('平均帯域'+str(mean_late/10**6)+' [M bit/sec] )')
print('#########################################################################')
