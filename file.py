def totHosts(CIDR):
    return (2**(32-CIDR))

def subnetMask(CIDR):
    if CIDR % 8 == 0:
        mask = 255
    else:
        mask = (256 - (2**(8-(CIDR % 8))))
    if (CIDR - 1) // 8 == 0:
        return f"{mask}.0.0.0"
    elif (CIDR - 1) // 8 == 1:
        return f"255.{mask}.0.0"
    elif (CIDR - 1) // 8 == 2:
        return f"255.255.{mask}.0"
    elif (CIDR - 1) // 8 == 3:
        return f"255.255.255.{mask}"

def lastIP(CIDR, IPaddr):
    IPbin = []
    for i in IPaddr.split("."):
        IPbin.append('{:08b}'.format(int(i)))
    IPbin = "".join(IPbin)
    tothostsbin = '{:08b}'.format(totHosts(CIDR))
    sum = int(IPbin, 2) + int(tothostsbin, 2) - int('1', 2)
    sumbin = bin(sum)[2:]
    IPaddr = []
    for i in range(0, len(sumbin), 8):
        IPaddr.append(int(sumbin[i:i+8], 2))
    return f"{IPaddr[0]}.{IPaddr[1]}.{IPaddr[2]}.{IPaddr[3]}"

def firstIP(IPaddr):
    IPbin = []
    for i in IPaddr.split("."):
        IPbin.append('{:08b}'.format(int(i)))
    IPbin = "".join(IPbin)
    sum = int(IPbin, 2) + int('1', 2)
    sumbin = bin(sum)[2:]
    IP = []
    for i in range(0, len(sumbin), 8):
        IP.append(int(sumbin[i:i+8], 2))
    return f"{IP[0]}.{IP[1]}.{IP[2]}.{IP[3]}"

def findClass(IPaddr):
    IPaddr = IPaddr.split(".")
    if int(IPaddr[0]) > 0 and int(IPaddr[0]) < 127:
        return "A"
    elif int(IPaddr[0]) > 127 and int(IPaddr[0]) < 192:
        return "B"
    elif int(IPaddr[0]) > 191 and int(IPaddr[0]) < 224:
        return "C"
    elif int(IPaddr[0]) > 223 and int(IPaddr[0]) < 240:
        return "D"
    elif int(IPaddr[0]) > 239 and int(IPaddr[0]) < 256:
        return "E"

IP = input("Enter IP address: ")
IPaddr = IP.split("/")[0]
CIDR = int("".join(IP.split("/")[1]))
print(f"\nNetwork: {IPaddr}")
print(f"This IP address belongs to Class {findClass(IPaddr)}")
print(f"Subnet Mask: {subnetMask(CIDR)}")
print(f"Total Hosts: {totHosts(CIDR) - 2}")
print(f"First subnet IP: {IPaddr}")
print(f"First Host IP: {firstIP(IPaddr)}")
print(f"Broadcast IP: {lastIP(CIDR, IPaddr)}")