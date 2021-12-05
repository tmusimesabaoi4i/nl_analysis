import socket
import sys
import time
import datetime

# Global variables
PORT = 50000           # Port No
BUFSIZE = int(2**12)   # Buffer size
PACKET_NUM = int(1e3)  # Number of packets sent
SLEEP_TIME = int(5)  # Number of sleep time

start_time = datetime.datetime.now()

for i in range(10):
    # Sleep to prevent errors
    print('sleep start')
    time.sleep(SLEEP_TIME)
    print('sleep end')

    # Error Number
    n_ok = 0
    n_eroor = 0

    # Get the measured time
    measured_time = datetime.datetime.now()

    # Measure the execution time
    time_sta = time.process_time()

    for j in range(PACKET_NUM):
        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # not a local environment, the IP address of the server.
            HOST = 'localhost' # HOST = 'IP address of the server'

            try:
                # Connect to server
                sock.connect((HOST, PORT))
            except:
                print('Cant connect')
                sys.exit()

            data = bytes(BUFSIZE)

            # Send data
            sock.send(data)

            # Receive data from the server and shut down
            received = sock.recv(BUFSIZE)

            if (data == received) and \
                    (len(received) == len(data)):
                n_ok += 1
            else:
                n_error += 1

    # Measure the execution time
    time_end = time.process_time()
    execution_time = time_end - time_sta

    # Error rate
    percent_receive = float(n_ok)/float(n_ok+n_error)

    # Bandwidth calculation [Mbyte/sec]
    if execution_time != 0:
        bandwidth = PACKET_NUM*BUFSIZE/(execution_time*1e6)
    else:
        bandwidth = 0

    print('----------------------------')
    print('{0} >>> TIME: {1:f} [sec], '+ \
        'BANDWIDTH: {2:f}[Mbyte/sec], '+ \
        'RECEPTION: {3:f}'\
        .format(measured_time, execution_time, bandwidth, percent_receive))
    print('----------------------------')

    print(datetime.datetime.now()-start_time)
