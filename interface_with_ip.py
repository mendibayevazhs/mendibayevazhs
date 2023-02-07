from pprint import pprint

def get_intf_ip_dict(filename):
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip
    return intf_ip_dict

config_list = ["config_r1.txt", "config1.txt"]
for cfg in config_list:
    result = get_intf_ip_dict(cfg)
    pprint(result)
