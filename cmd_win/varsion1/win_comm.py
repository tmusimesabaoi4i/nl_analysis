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

        self.__min_late = 0 # 最速帯域
        self.__max_late = 0 # 最遅帯域
        self.__mean_late = 0 # 平均帯域

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

        for i in jp_code :
            if (i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) :
                ans_list[n_list].append(i)
                flag = 0
            elif flag == 0:
                n_list = n_list + 1
                flag = 1

        ans_num_list = []

        for l in ans_list :
            s = 0
            ans_num = 0
            for num_10 in l :
                ans_num = ans_num + int(num_10)*10**(len(l)-s-1)
                s = s + 1
            ans_num_list.append(ans_num)

        del ans_list,n_list,flag,s,ans_num
        return ans_num_list

    def __return_time(self) -> str :
        jp_time_info = self.__run_cmd('ECHO %time%')
        jp_date_info = self.__run_cmd('ECHO %date%')

        result_date = self.__return_num_from_cmd(jp_date_info,3)
        result_time = self.__return_num_from_cmd(jp_time_info,4)

        return datetime.datetime(year=result_date[0],
            month=result_date[1],
            day=result_date[2],
            hour = result_time[0],
            minute = result_time[1],
            second = result_time[2],
            microsecond = result_time[3])

    def __set_speeddata(self) -> None :
        self.__jp_ping_info = re.sub('.+\r\n','',self.__run_cmd(self.__cmd),2+self.__num_p)

        result_ping = self.__return_num_from_cmd(self.__jp_ping_info,7)

        self.__min_late = self.__size_p * 8 * 2 * 10**3 / result_ping[4]
        self.__max_late = self.__size_p * 8 * 2 * 10**3 / result_ping[5]
        self.__mean_late = self.__size_p * 8 * 2 * 10**3 / result_ping[6]

    def __set_s_time(self) -> None :
        self.__s_time = self.__return_time()

    def __set_e_time(self) -> None :
        self.__e_time = self.__return_time()

    def run(self) -> float :
        self.__set_s_time()
        self.__set_speeddata()
        self.__set_e_time()
        return [self.__s_time,self.__e_time,self.__min_late/1e6, self.__max_late/1e6, self.__mean_late/1e6]

if __name__ == '__main__':
    packets_num = 10 # パケットの数
    byte_num = 60000 # パケットのバイト数 = 60kB
    ip_addr = '192.168.1.18' # 送り先のIPアドレス
    win_comd = WinComm(packets_num,byte_num,ip_addr)
    print(win_comd.run())
