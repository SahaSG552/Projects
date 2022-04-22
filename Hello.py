def is_valid(ip_address):
    return list(map(lambda x: x.isdigit()
           and 0 <= int(x) <= 256, 
           ip_address.split(".")))


print(all(is_valid("12.90.dddd.1")))