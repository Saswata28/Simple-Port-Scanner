from socket import *


def scan_port(target_host, target_port):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((target_host, target_port))
        print(f"[+] {target_port}/tcp open")
        conn_socket.close()
    except:
        print(f"[-] {target_port}/tcp closed")


def multiple_port_scan(target_host, target_ports):
    try:
        target_ip = gethostbyname(target_host)
    except:
        print(f"[-] can't resolve for {target_host}")
        return
    try:
        target_name = gethostbyaddr(target_ip)
        print(f"[+] scan result of {target_name[0]}")
    except:
        print(f"[+] scan result of {target_ip}")
    setdefaulttimeout(1)
    for target_port in target_ports:
        print(f"scanning port {target_port}")
        scan_port(target_host, target_port)


if __name__ == '__main__':
    ip = input("Enter the ip: ")
    count_invalid_ports = 0
    while True:
        user_input = input(
            "Do you want to check for more than 1 port? (y/n): ").lower()
        if user_input == 'y' or user_input == 'yes':
            list_of_ports = input("Enter the ports like(80,443,220): ")
            list_of_ports = list_of_ports.replace("[", "")
            list_of_ports = list_of_ports.replace("]", "")
            list_of_ports = list_of_ports.split(",")
            list_of_ports = list(map(int, list_of_ports))
            for i in range(len(list_of_ports)):
                if list_of_ports[i] < 1 or list_of_ports[i] > 65535:
                    print(
                        f"There is a Invalid port on position {i+1} on the port list. port {list_of_ports[i]} doesn't exist.")
                    count_invalid_ports += 1
                else:
                    continue
            if count_invalid_ports > 0:
                print(
                    f"Can't continue the scan becuase of {count_invalid_ports} invalid ports.")
                break
            multiple_port_scan(ip, list_of_ports)
            break
        elif user_input == 'n' or user_input == 'no':
            port = input("Enter the port: ")
            scan_port(ip, port)
            break
        else:
            print("please enter y or n.")
            continue
