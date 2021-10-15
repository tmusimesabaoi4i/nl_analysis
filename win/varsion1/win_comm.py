import subprocess
import re
import datetime

class WinComm :
    def __init__(self,num_p:float,size_p:float,addr:str) -> None :
        self.__num_p = num_p # num_p パケットの数 ( Number of packets )
        self.__size_p = size_p # size_p パケットの大きさ[byte] ( Size of packets )
        self.__addr = addr # addr 送り先アドレス ( Sending address )

        self.__s_time = 0 # 計測し終わった時刻を格納する
        self.__e_time = 0 # 計測し終わった時刻を格納する

        self.__min_band_bit = 0 # 最速帯域 [bit/sec]
        self.__max_band_bit = 0 # 最遅帯域 [bit/sec]
        self.__mean_band_bit = 0 # 平均帯域 [bit/sec]

        # 実行するコマンド
        self.__cmd = 'ping' + ' ' + '-n' + ' ' + str(self.__num_p) + ' ' + '-l' + ' ' + str(self.__size_p) + ' ' + self.__addr

        # 実行したコマンドの結果を格納する
        self.__jp_ping_info = ''

    def __run_cmd(self,cmd:str) -> str :
        returncode = subprocess.check_output(cmd, shell=True) # 実行した結果を格納
        jp_code = returncode.decode('cp932') # 日本語に直す
        return jp_code

    def __return_num_from_cmd(self,jp_code:str,return_len:int) -> list :
        ans_list = [[] for i in range(return_len)]
        n_list = 0
        flag = 1

        # flag #################################
        # 数字なら0、数字出ない場合は1を格納する
        ########################################
        for i in jp_code : # 文字列から数字のみを取り出す
            if (i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) : # 数字を読み込む
                ans_list[n_list].append(i)
                flag = 0
            elif flag == 0: # 初めて数字以外の文字列が出現した場合
                n_list = n_list + 1
                flag = 1
            else : pass # 二回目以降数字以外の文字列が出現した場合

        ans_num_list = []

        for l in ans_list : # リストから数字へ変換する
            s = 0 # 最高桁から下がっていく
            list_num = 0 # リストの数字
            for num_10 in l :
                list_num = list_num + int(num_10)*10**(len(l)-s-1)
                s = s + 1
            ans_num_list.append(list_num)

        del ans_list,n_list,flag,s,list_num
        return ans_num_list

# 192.168.1.18 の ping 統計以下の数字を取り出す
################################################################################
# (py39) D:\github\nl_analysis\cmd_win\varsion1>ping -n 2 192.168.1.18
#
# 192.168.1.18 に ping を送信しています 32 バイトのデータ:
# 192.168.1.18 からの応答: バイト数 =32 時間 =3ms TTL=128
# 192.168.1.18 からの応答: バイト数 =32 時間 =2ms TTL=128
#
# 192.168.1.18 の ping 統計:
#     パケット数: 送信 = 2、受信 = 2、損失 = 0 (0% の損失)、
# ラウンド トリップの概算時間 (ミリ秒):
#     最小 = 2ms、最大 = 3ms、平均 = 2ms
################################################################################

    def __set_speeddata(self) -> None : # 送信データと往復遅延時間から帯域の計算を行う
        self.__jp_ping_info = re.sub('.+\r\n','',self.__run_cmd(self.__cmd),2+self.__num_p)

        result_ping = self.__return_num_from_cmd(self.__jp_ping_info,7)

        if result_ping[4] == 0: result_ping[4] = 1 # 0の場合は1msecとする
        if result_ping[5] == 0: result_ping[5] = 1 # 0の場合は1msecとする
        if result_ping[6] == 0: result_ping[6] = 1 # 0の場合は1msecとする

        self.__min_band_bit = self.__size_p * 8 * 2 * 10**3 / result_ping[4]
        self.__max_band_bit = self.__size_p * 8 * 2 * 10**3 / result_ping[5]
        self.__mean_band_bit = self.__size_p * 8 * 2 * 10**3 / result_ping[6]

    def __return_time(self) -> str :
        return datetime.datetime.now()
    def __set_s_time(self) -> None :
        self.__s_time = self.__return_time()
    def __set_e_time(self) -> None :
        self.__e_time = self.__return_time()

    def run(self) -> float :
        self.__set_s_time()
        self.__set_speeddata()
        self.__set_e_time()
        return [self.__s_time,self.__e_time,self.__min_band_bit/1e6, self.__max_band_bit/1e6, self.__mean_band_bit/1e6]

if __name__ == '__main__':
    packets_num = 10 # パケットの数
    byte_num = 60000 # パケットのバイト数 = 60kB
    ip_addr = '192.168.1.18' # 送り先のIPアドレス
    v_win_comm = WinComm(packets_num,byte_num,ip_addr)
    print(v_win_comm.run())
