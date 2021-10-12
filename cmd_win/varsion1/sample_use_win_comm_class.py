import datetime
import win_comm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # install openpyxl

packets_num = 10 # パケットの数
byte_num = 60000 # パケットのバイト数 = 60kB
ip_addr = '192.168.1.18' # 送り先のIPアドレス

min_band_mbit = np.zeros(0)
max_band_mbit = np.zeros(0)
mean_band_mbit = np.zeros(0)
execute = np.zeros(0)
execute_day = np.zeros(0)
execute_time = np.zeros(0)

dt_start_time = datetime.datetime.now()
while 1 :
    dt_end_time = datetime.datetime.now()
    dt_diff = dt_end_time - dt_start_time

    win_comd = win_comm.WinComm(packets_num,byte_num,ip_addr)
    speed_test = win_comd.run()
    print(speed_test[0])

    execute = np.append(execute,speed_test[0])
    execute_day = np.append(execute_day,speed_test[0].day)
    execute_time = np.append(execute_time,[str(speed_test[0].hour) + ':' + str(speed_test[0].minute) + ':' + str(speed_test[0].second)])
    min_band_mbit = np.append(min_band_mbit,speed_test[2])
    max_band_mbit = np.append(max_band_mbit,speed_test[3])
    mean_band_mbit = np.append(mean_band_mbit,speed_test[4])

    if dt_diff > datetime.timedelta(days=0, seconds=10, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) : break

save_data = np.stack([execute, execute_day, execute_time, min_band_mbit, mean_band_mbit, max_band_mbit],1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(execute_time, min_band_mbit, label='minimum latency')
ax.plot(execute_time, mean_band_mbit, label='average latency')
ax.plot(execute_time, max_band_mbit, label='maximum latency')
ax.set_xlabel('measured time')
ax.set_ylabel('bandwidth [M bit/sec]')
plt.legend(loc='best')
plt.savefig('5g_latency_plot.png')

col = ['計測時刻（詳細）','計測日','計測時間','最小遅延時帯域','平均遅延時帯域','最大遅延時帯域']
df = pd.DataFrame(save_data,columns=col)
df.to_excel('out.xlsx', sheet_name="test")
