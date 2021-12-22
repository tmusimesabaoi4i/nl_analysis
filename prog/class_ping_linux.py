import subprocess
import re

class Ping_Linux:
    def __init__(self, packets_num: int,
        byte_num: int, ip_addr: str) -> None:
        self.__packets_num = packets_num
        self.__byte_num = byte_num
        self.__ip_addr = ip_addr

        self.__cmd = 'ping' + \
                ' -c ' + str(packets_num) + \
                ' -s ' + str(byte_num) + \
                ' ' + ip_addr

    def run_command(self) -> None:
        cmd = self.__cmd

        returncode = subprocess.check_output(cmd, shell=True)    # 実行した結果を格納
        jp_code = returncode.decode('cp932')                     # 日本語に直す

        self.__command_result = jp_code
        del cmd, returncode, jp_code

    def order_result(self) -> None:
        jp_code = self.__command_result
        packets_num = self.__packets_num

        jp_ping_info = re.sub('.+\n','',jp_code,2+packets_num) # 最後の部分のみ取り出す

        jp_ping_result = list()                                  # 結果を格納するリスト
        tmp = str()
        for text in jp_ping_info:
            if (text in ['0', '1', '2', '3',\
                     '4', '5', '6', '7', '8', '9', '.']):
                tmp += text
            elif tmp != '':
                jp_ping_result.append(tmp)
                tmp = str()
        jp_ping_result = [float(tmp) for tmp in jp_ping_result]    # 文字列を数字に変換する

        self.__int_command_result = jp_ping_result
        del jp_code, packets_num, jp_ping_info, jp_ping_result, tmp

    def ans(self) -> None:
        jp_ping_result = self.__int_command_result
        byte_num = self.__byte_num

        if jp_ping_result[4] != 0.0:
            min_late = byte_num * 2.0 * 8.0 * 10**3 / jp_ping_result[4]
        else:
            min_late = 0.0

        if jp_ping_result[5] != 0.0:
            mean_late = byte_num * 2.0 * 8.0 * 10**3 / jp_ping_result[5]
        else:
            mean_late = 0.0

        if jp_ping_result[6] != 0.0:
            max_late = byte_num * 2.0 * 8.0 * 10**3 / jp_ping_result[6]
        else:
            max_late = 0.0

        self.__command_result_dict = {
        'MAX_BANDWIDTH':min_late/10**6, # [Mega bit / sec]
        'MIN_BANDWIDTH':max_late/10**6, # [Mega bit / sec]
        'AVE_BANDWIDTH':mean_late/10**6 # [Mega bit / sec]
        }
        del jp_ping_result, byte_num, min_late, max_late, mean_late

    def run(self) -> dict:
        self.run_command()
        self.order_result()
        self.ans()
        return self.__command_result_dict

if __name__ == '__main__':
    packets_num = 20
    byte_num = 1400
    ip_addr = '192.168.1.38'
    pl = Ping_Linux(packets_num, byte_num, ip_addr)
    ans = pl.run()
    print(ans)
