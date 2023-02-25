import argparse
import nmap

def argument_parser():
    parser = argparse.ArgumentParser(
        description="tcp port scanner. Accepts a hostname/IP address and list of ports to ""scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="comma-separated port list, such as '25,88,8080'")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary
    return var_args

def nmap_scan(host_id,port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id,port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state'] #indicate the type of scan and port
    result = ("[*] {host} tcp/{port} {state}".format(host=host_id , port=port_num,state=state))

    return result

if __name__=="__main":
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["ports"].split(",")  # make list from port numbers
        for port in ports:
            print(nmap_scan(host,port))

    except AttributeError:
        print("Error. please provide the command-line arguments before running.")
