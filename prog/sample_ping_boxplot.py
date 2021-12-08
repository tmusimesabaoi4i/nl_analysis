import time
import datetime
import numpy as np
import matplotlib.pyplot as plt

packets_num = 1                     # パケットの数
byte_num = 1400                     # パケットのバイト数
ip_addr = '192.168.1.38'            # 送り先のIPアドレス
ROUND = int(1e3)                    # 送信回数

if __name__ == '__main__':
    OSNAME='linux'
    if OSNAME=='linux':
        import class_ping_linux
        pping = class_ping_linux.Ping_Linux(packets_num, byte_num, ip_addr)
    elif OSNAME=='windows':
        import class_ping_windows
        pping = class_ping_windows.Ping_Windows(packets_num, byte_num, ip_addr)
    else: pass

    l_ans = list()

    for i in range(0,ROUND):
        ans = pping.run()
        ans = ans['AVE_BANDWIDTH']
        l_ans.append(ans)
        time.sleep(0.1)

    np_ans = np.array(l_ans)

    dt_now = datetime.datetime.now()

    fig, ax = plt.subplots()
    ax.set_title('Bandwidth Measurement')
    ax.boxplot(np_ans, showfliers=False)
    ax.set_xlabel('')
    ax.set_ylabel('Bandwidth [M bit/sec]')
    ax.set_xticklabels([dt_now.strftime('%H:%M:%S')])
    plt.savefig('img_boxplot_'+OSNAME+'.svg', dpi=500)
    plt.savefig('img_boxplot_'+OSNAME+'.png', dpi=500)
