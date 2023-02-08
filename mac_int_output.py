table = [['100','a1b2.ac10.7000','DYNAMIC','Gi0/1'],
         ['200','a1b3.ab10.8000','DYNAMIC','Gi0/2']]
for vlan, mac, *others, intf in table:
    print(f"{vlan:10}{mac:20}{intf}")

result = [print(f"{vlan:10}{mac:20}{intf}") for vlan, mac, *others, intf in table]
