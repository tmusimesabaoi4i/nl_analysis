# ABOUT REPOSITORY
ネットワークの帯域を計測するためのプログラムを保管するレポジトリです。

# CREATING VIRTUAL ENVIRONMENT
```
python -m venv C:\Users\yohei\py39
```

# ACTIVATE THE VIRTUAL ENVIRONMENT
```
CALL C:\Users\yohei\py39\Scripts\activate.bat
```

# DEACTIVATE THE VIRTUAL ENVIRONMENT
```
CALL C:\Users\yohei\py39\Scripts\deactivate.bat
```

# INSTALL THE PYTHON LIBRARIES
```
python -m pip install --upgrade pip setuptools wheel

python -m pip install Flask
python -m pip install scipy
python -m pip install matplotlib
python -m pip install sounddevice
python -m pip install pyrealsense2
python -m pip install opencv-python
```

# MEASUREMENT METHOD
PINGを利用した計測が帯域の計測の主なやり方ですが、
SOCKET通信を利用した方法での計測も行います。

# IN CASE OF PING

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

### FOR WINDOWS
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
