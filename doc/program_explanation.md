# IN CASE OF PING
- [sample_ping_windows.py](../prog/sample_ping_windows.py)

上記プログラムを実行した場合、以下のような結果になる。

```
{'パケット受信数': 20, 'パケット送信数': 20, 'パケット損失数': 0, 'PACKET_LOSS_RATE': 0, 'RTT_MIN': 2, 'RTT_MAX': 2, 'RTT_AVE': 2, 'MAX_BANDWIDTH': 65.5, 'MIN_BANDWIDTH': 65.5, 'AVE_BANDWIDTH': 65.5}
```

# PING CLASS
[sample_ping_windows.py](../prog/sample_ping_windows.py)で作成したプグラムを
少し変更して、`ping`コマンドを`20`回実行しその結果を返却するクラスを作成します。
- [class_ping_windows.py](../prog/class_ping_windows.py)

上記プログラムを実行した場合、以下のような結果になる。

```
{'MAX_BANDWIDTH': 131.0, 'MIN_BANDWIDTH': 65.5, 'AVE_BANDWIDTH': 131.0}
```
