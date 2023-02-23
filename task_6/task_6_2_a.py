ip_address = input("Enter ip address: ")
octets = ip_address.split(".")
correct_ip = True

if len(octets) != 4:
    correct_ip = False
else:
    for octet in octets:

        if not (octet.isdigit() and int(octet) in range(256)):
            correct_ip = False
            break

if not correct_ip:
    print("Неправильный IP-адрес")
else:
    octets_num = [int(i) for i in octets]

    if octets_num[0] in range(1, 224):
        print("unicast")
    elif octets_num[0] in range(224, 240):
        print("multicast")
    elif ip_address == "255.255.255.255":
        print("local broadcast")
    elif ip_address == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
ip = input("Введите IP-адрес в формате x.x.x.x: ")
octets = ip.split(".")
valid_ip = len(octets) == 4

for i in octets:
    valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

if valid_ip:
    if 1 <= int(octets[0]) <= 223:
        print("unicast")
    elif 224 <= int(octets[0]) <= 239:
        print("multicast")
    elif ip == "255.255.255.255":
        print("local broadcast")
    elif ip == "0.0.0.0":
        print("unassigned")
    else:
        print("unused")
else:
    print("Неправильный IP-адрес")