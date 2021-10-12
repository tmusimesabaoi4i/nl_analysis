# https://qiita.com/okadate/items/00227316187b60f861f5
import datetime
import win_comm as wc
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # install openpyxl

from matplotlib import ticker # 軸

class Test :
    def __init__(self,img_file:str,xlsx_file:str,num_p:float,size_p:float,addr:str,t_d:datetime.timedelta) -> None :
        self.__num_p = num_p # num_p パケットの数 ( Number of packets )
        self.__size_p = size_p # size_p パケットの大きさ[byte] ( Size of packets )
        self.__addr = addr # addr 送り先アドレス ( Sending address )
        self.__t_d = t_d # どれぐらいの時間コマンドを実行するか

        self.__img_file = img_file # 画像を保存するファイル名
        self.__xlsx_file = xlsx_file # エクセルデータを保存するファイル名

        self.__win_comm = 0 # WinCommクラスを格納するための変数


        # self.__min_band_mbit
        # self.__max_band_mbit
        # self.__mean_band_mbit
        # self.__execute_time

    def __set_comm(self) -> None :
        self.__win_comm = wc.WinComm(self.__num_p,self.__size_p,self.__addr)

    def __do_comm(self) -> float :
        min_band_mbit = np.zeros(0)
        max_band_mbit = np.zeros(0)
        mean_band_mbit = np.zeros(0)
        execute_time = np.zeros(0)

        dt_start_time = datetime.datetime.now()
        while 1 :
            dt_end_time = datetime.datetime.now()
            dt_diff = dt_end_time - dt_start_time

            speed_test = self.__win_comm.run()
            min_band_mbit = np.append(min_band_mbit,speed_test[2])
            max_band_mbit = np.append(max_band_mbit,speed_test[3])
            mean_band_mbit = np.append(mean_band_mbit,speed_test[4])
            execute_time = np.append(execute_time,[str(speed_test[0].hour) + ':' + str(speed_test[0].minute) + ':' + str(speed_test[0].second)])

            print(str(dt_end_time)+' done.')

            if dt_diff > self.__t_d : break

        self.__min_band_mbit = min_band_mbit
        self.__max_band_mbit = max_band_mbit
        self.__mean_band_mbit = mean_band_mbit
        self.__execute_time = execute_time

        del min_band_mbit,max_band_mbit,mean_band_mbit,execute_time,dt_start_time,dt_end_time,dt_diff

    def __save_img(self) -> None :
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(self.__execute_time, self.__min_band_mbit, label='最小遅延時帯域')
        ax.plot(self.__execute_time, self.__max_band_mbit, label='最大遅延時帯域')
        ax.plot(self.__execute_time, self.__mean_band_mbit, label='平均遅延時帯域')
        ax.xaxis.set_major_locator(ticker.MaxNLocator(5)) # Locator 目盛り位置
        ax.set_xlabel('measured time [24-hour clock]')
        ax.set_ylabel('bandwidth [M bit/sec]')
        ax.set_title('計測日：'+str(datetime.datetime.now().month)+'月'+str(datetime.datetime.now().day)+'日', fontname='Meiryo')
        plt.legend(loc='best',prop = {'family' : 'Meiryo'})
        plt.savefig(self.__img_file, bbox_inches='tight',format="png", dpi=500)

        del fig,ax

    def __save_xlsx(self) -> None :
        col = ['計測時間','最小遅延時帯域','最大遅延時帯域','平均遅延時帯域']
        df = pd.DataFrame(np.stack([self.__execute_time, self.__min_band_mbit, self.__max_band_mbit, self.__mean_band_mbit],1),columns=col)
        df.to_excel(self.__xlsx_file)

        del col,df

    def run(self) :
        self.__set_comm()
        self.__do_comm()
        self.__save_img()
        self.__save_xlsx()

if __name__ == '__main__':
    img_file = 'result.png'
    xlsx_file = 'data.xlsx'
    packets_num = 60 # パケットの数
    byte_num = 60000 # パケットのバイト数 = 60kB
    ip_addr = '192.168.1.18' # 送り先のIPアドレス
    t_d = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=10, hours=0, weeks=0)
    v_win_test = Test(img_file,xlsx_file,packets_num,byte_num,ip_addr,t_d)
    v_win_test.run()
