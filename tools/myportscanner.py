from socket import*
import argparse
import threading

def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)
def input_parser():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--host",nargs="?",help="ip of target")
    parser.add_argument("-p","--ports",nargs="?",default=1000,help="number of ports to scan")
    final=vars(parser.parse_args())
    return final

def connect_target(t_ip,t_port): # connect to target ip and see ip open or not
    try:
        global coontarget
        conntarget=socket(AF_INET,SOCK_STREAM)
        conntarget.connect((t_ip,t_port))
        coontarget.send(b'Banner query\r\n')
        result=coontarget.recv(100)
        print("[+] {}/tcp open".format(t_port))
        print("[+] {}".format(result))
    except OSError:
        print("[-] {}/tcp closed".format(t_port))
    finally:
        conntarget.close()  # to confirm the connection is closed

def port_scan(target, ports):
    portlist =[createList(int(ports))]

    try:
        target_ip = gethostname()
        print("[+] scan result for {}".format(target_ip))
        i=0
        while i<=int(ports):
              port=portlist[i]
              connect_target(target_ip, int(port))
    except OSError:
        print("[^] cannot resolve {}: Unknown host".format(target))
        return  # exit port scan if target ip is not resolved
    t = threading.Thread(target=connect_target, args=(target, int(ports)))
    t.start()

if __name__ == '__main__':
    try:
        user_args = input_parser()
        host = user_args["host"]
        port_list = user_args["ports"].split(",")  # make list from port numbers
        for port in port_list:
            port_scan(host, port)

    except AttributeError:
        print("Error. please provide the command-line arguments before running.")
