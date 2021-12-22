import numpy as np
import openpyxl
import matplotlib.pyplot as plt

packets_num = 1                     # パケットの数
byte_num = 1400                     # パケットのバイト数
ROUND = int(1e3)                    # 送信回数

OSNAME='linux'                      # プログラムを実行するOSの名前

if __name__ == '__main__':
    ip_addr_array = ['192.168.103.2','10.90.8.112']        # 送り先のIPアドレス
    #ip_addr_array = ['192.168.1.38','192.168.1.39']        # 送り先のIPアドレス

    file = 'sample_data_2'

    wb = openpyxl.load_workbook(file+'.xlsx')

    l_ans = [list() for i in range(0,len(ip_addr_array))]

    for ip_idx, ip_addr in enumerate(ip_addr_array):

        # シート名は「送り先IPアドレス」
        sheet_nameXL = 'SendTo_'+ ip_addr+ '.xlsx'
        ws = wb[sheet_nameXL]

        for i in range(0,ROUND):
            cellXL = ws.cell(row=i+1, column=1)
            ans = cellXL.value
            l_ans[ip_idx].append(ans)

    np_ans = np.array(l_ans)

    wb.close()

    capprops = dict(linestyle='-', linewidth=1, color='black')
    boxprops = dict(linestyle='-', linewidth=1, color='black')
    whiskerprops = dict(linestyle='-', linewidth=1, color='black')
    flierprops = dict(linestyle='-', linewidth=1, color='black')
    medianprops = dict(linestyle='-', linewidth=3, color='r')

    fig, ax = plt.subplots()
    ax.set_title('Bandwidth Measurement')
    pos = np.arange(len(np_ans)) + 1
    bp = ax.boxplot(np_ans.T, sym='k+',
                    positions=pos, whis=float('inf'), # 外れ値検出しない
                    capprops=capprops,
                    boxprops=boxprops,
                    whiskerprops=whiskerprops,
                    flierprops=flierprops,
                    medianprops=medianprops,
                    showmeans=True) # 平均値を表示する
    plt.savefig(file+'_XL'+'.svg', dpi=500)
    plt.savefig(file+'_XL'+'.png', dpi=500)

    q075, q050, q025 = np.percentile(np_ans[0], [75 ,50 ,25])
    q175, q150, q125 = np.percentile(np_ans[1], [75 ,50 ,25])
