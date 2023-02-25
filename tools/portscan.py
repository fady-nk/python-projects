from socket import*
import argparse
import threading


def connection_scan(target_ip, target_port):
    global conn_socket
    try:
        conn_socket = socket(AF_INET,SOCK_STREAM)
        conn_socket.connect((target_ip, target_port))
        conn_socket.send(b'Banner_query\r\n')
        result=conn_socket.recv(100)
        print("[+] {}/tcp open".format(target_port))
        print("[+] {}".format(result))
    except OSError:
        print("[-] {}/tcp closed".format(target_port))
    finally:
        conn_socket.close()  # to confirm the connection is closed


def port_scan(target, port_num):
    try:
        target_ip = gethostbyname(target)
        print("[+] scan result for {}".format(target_ip))
        connection_scan(target_ip, int(port_num))
    except OSError:
        print("[^] cannot resolve {}: Unknown host".format(target))
        return  # exit port scan if target ip is not resolved
    t = threading.Thread(target=connection_scan, args=(target, int(port_num)))
    t.start()

def argument_parser():
    parser = argparse.ArgumentParser(description="tcp port scanner. Accepts a hostname/IP address and list of ports to ""scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="comma-separated port list, such as '25,88,8080'")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary
    return var_args


if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        port_list = user_args["ports"].split(",")  # make list from port numbers
        for port in port_list:
            port_scan(host, port)

    except AttributeError:
        print("Error. please provide the command-line arguments before running.")
