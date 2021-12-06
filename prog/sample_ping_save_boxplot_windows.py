import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import class_ping_windows

packets_num = 1                     # パケットの数
byte_num = 65500                    # パケットのバイト数
ip_addr = '192.168.1.38'            # 送り先のIPアドレス

if __name__ == '__main__':
    pw = class_ping_windows.Ping_Windows(packets_num, byte_num, ip_addr)

    l_ans = list()

    for i in range(0,int(1e2)):
        ans = pw.run()
        ans = ans['AVE_BANDWIDTH']
        l_ans.append(ans)
        time.sleep(0.1)

    np_ans = np.array(l_ans)

    dt_now = datetime.datetime.now()

    fig, ax = plt.subplots()
    ax.set_title('Bandwidth Measurement')
    ax.boxplot(np_ans, showfliers=False)
    ax.set_xlabel('')
    ax.set_ylabel('Bandwidth [M byte/sec]')
    ax.set_xticklabels([dt_now.strftime('%H:%M:%S')])
    plt.savefig('img_sample_ping_save_xl_window.svg', dpi=500)
    plt.savefig('img_sample_ping_save_xl_window.png', dpi=500)
