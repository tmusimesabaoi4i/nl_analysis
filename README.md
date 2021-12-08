# ABOUT REPOSITORY
ネットワークの帯域を計測するためのプログラムを保管するレポジトリです。

- [[Sample Program Explanation]](/doc/program_explanation.md)

# WINDOWS PYTHON
#### [WINDOWS]CREATING VIRTUAL ENVIRONMENT
```
python -m venv C:\Users\yohei\py39
```
#### [WINDOWS]ACTIVATE THE VIRTUAL ENVIRONMENT
```
CALL C:\Users\yohei\py39\Scripts\activate.bat
```
#### [WINDOWS]DEACTIVATE THE VIRTUAL ENVIRONMENT
```
CALL C:\Users\yohei\py39\Scripts\deactivate.bat
```

# LINUX PYTHON
#### [LINUX]INSTALL PYTHON
```
sudo apt remove python3 -y &&
sudo apt remove pip -y &&
sudo apt update &&
sudo apt full-upgrade -y &&
sudo apt autoremove -y &&
sudo apt clean &&
sudo apt install python3 -y &&
sudo apt install python3-pip -y &&
sudo apt install python3-venv -y
```
#### [LINUX]CREATING VIRTUAL ENVIRONMENT
```
python3 -m venv /mnt/d/py39
```
#### [LINUX]ACTIVATE THE VIRTUAL ENVIRONMENT
```
source /mnt/d/py39/bin/activate
```
#### [LINUX]DEACTIVATE THE VIRTUAL ENVIRONMENT
```
deactivate
```
#### INSTALL THE PYTHON LIBRARIES
```
yes | python3 -m pip install --upgrade pip setuptools wheel &&

source /mnt/d/py39/bin/activate &&
yes | python3 -m pip install Flask &&
yes | python3 -m pip install scipy &&
yes | python3 -m pip install openpyxl &&
yes | python3 -m pip install matplotlib &&
yes | python3 -m pip install sounddevice &&
yes | python3 -m pip install opencv-python
```

# MEASUREMENT METHOD
`ping`を利用し、帯域の計測を行います。

# IN CASE OF PING
`ping`コマンドを利用した帯域計測の方法について説明します。
まずは、`ping`の基本的な使い方とその結果を示します。

### FOR WINDOWS
`ping -n 要求数 -l データサイズ 宛先アドレス`というコマンドでpingを実行します。

例えば、`ping -n 10 -l 65500 192.168.***.38`の場合は
`192.168.***.38`に対して65500byteのデータを10回送信した場合の結果を見ることができます。
具体的に`192.168.1.38`に送信した場合の結果を表示します。

```
192.168.1.38 に ping を送信しています 65500 バイトのデータ:
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128
192.168.1.38 からの応答: バイト数 =65500 時間 =2ms TTL=128

192.168.1.38 の ping 統計:
    パケット数: 送信 = 10、受信 = 10、損失 = 0 (0% の損失)、
ラウンド トリップの概算時間 (ミリ秒):
    最小 = 2ms、最大 = 2ms、平均 = 2ms
```

### FOR LINUX
`ping -c 要求数 -s データサイズ 宛先アドレス`というコマンドでpingを実行します。

例えば、`ping -c 10 -s 65500 192.168.***.38`の場合は
`192.168.***.38`に対して65500byteのデータを10回送信した場合の結果を見ることができます。
具体的に`192.168.1.38`に送信した場合の結果を表示します。

```
PING 192.168.1.38 (192.168.1.38) 65500(65528) bytes of data.
65508 bytes from 192.168.1.38: icmp_seq=1 ttl=128 time=3.37 ms
65508 bytes from 192.168.1.38: icmp_seq=2 ttl=128 time=2.54 ms
65508 bytes from 192.168.1.38: icmp_seq=3 ttl=128 time=2.33 ms
65508 bytes from 192.168.1.38: icmp_seq=4 ttl=128 time=2.48 ms
65508 bytes from 192.168.1.38: icmp_seq=5 ttl=128 time=2.51 ms
65508 bytes from 192.168.1.38: icmp_seq=6 ttl=128 time=2.76 ms
65508 bytes from 192.168.1.38: icmp_seq=7 ttl=128 time=2.43 ms
65508 bytes from 192.168.1.38: icmp_seq=8 ttl=128 time=2.40 ms
65508 bytes from 192.168.1.38: icmp_seq=9 ttl=128 time=2.77 ms
65508 bytes from 192.168.1.38: icmp_seq=10 ttl=128 time=2.73 ms

--- 192.168.1.38 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9011ms
rtt min/avg/max/mdev = 2.326/2.630/3.367/0.286 ms
```

### CALCULATE BANDWIDTH
`ping`を実行すると、[ラウンドトリップタイム(RTT)](https://jprs.jp/glossary/index.php?ID=0195#:~:text=%E9%80%9A%E4%BF%A1%E7%9B%B8%E6%89%8B%E3%81%AB%E3%83%87%E3%83%BC%E3%82%BF%E3%82%92,%E9%80%9A%E4%BF%A1%E3%81%AE%E5%BE%80%E5%BE%A9%E6%99%82%E9%96%93%EF%BC%89%E3%81%A7%E3%81%99%E3%80%82)が表示されます。
そして、実行結果の一番最後には、RTTの最大値・RTTの最小値・RTTの平均値が
表示されます。RTTは通信の往復時間なので、帯域は以下のように計算することが出来ます。

<p align="center">
<img src="https://latex.codecogs.com/gif.latex?\mathrm{BANDWIDTH}&space;=&space;{\mathrm{data&space;size}}&space;*&space;2&space;/&space;\mathrm{RTT}" title="\mathrm{BANDWIDTH} = {\mathrm{data size}} * 2 / \mathrm{RTT}" />
</p>

### CAUTION
windowsでは`ping`の受送信がファイヤーウォールによって禁止されている場合があるそうです。
なので、`ping`が通らない時はファイヤーウォールの設定を変更する必要があります。
<sup id="note_ref-1"><a href="#note-1">[参考1]</a></sup>

# REFERENCE
<b><a id="note-1" href="#note_ref-1">[参考1]</a></b> [【Windows 10対応】Windowsのファイアウォールで「ping」コマンドへの応答を許可する](https://atmarkit.itmedia.co.jp/ait/articles/1712/21/news018.html)
