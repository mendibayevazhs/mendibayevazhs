from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import csv
import netmiko
import time
IP_LIST = open('devices.txt')
for IP in IP_LIST:
    connect = {
    'device_type': 'cisco_ios',
    'ip': IP,
    'username': 'username',
    'password': 'password',
    'secret': 'cisco',
    }
    try:
        net_connect = ConnectHandler(**connect)
        print(f"Yeah, I connected to device {IP}")
        net_connect.enable()
    except NameError :
        print (f"ERROR {IP}")
        continue

    except NetmikoAuthenticationException:
        print (f"Maybe Password does not correct {IP}")
        continue

    except NetmikoTimeoutException:
        print (f"Device not reachable {IP}.")
        continue

    except AuthenticationException:
        print (f"Authentication Failure {IP}.")
        continue

    except SSHException:
        print (f"Make sure SSH is enabled in device {IP}.")
        continue
    print ('\n Initiating config \n')
    serial_number_output = net_connect.send_command('show version')
    hostname_output = net_connect.send_command('show run | in hostname')
    SAVE_FILE = open("serial_number.txt", 'a')
    SAVE_FILE.write(f"IP ADDRESS: {IP}")
    SAVE_FILE.write(f"\n{hostname_output}")
    SAVE_FILE.write(f"\n{serial_number_output}")
    SAVE_FILE.close
    print (f"\n Finished config {IP} \n")
