import re

gg = {
    "m": lambda g: 1 if g in [1117, 1445, 3211, 107, 774, 1659, 2131, 289, 968, 888, 1210, 83, 1199] else 0,
    "s": lambda h: str(int(h[-2:] + h[:-2], 16)),
    "b": "1678262402/"
}


value1 = 1117  
value2 = 1234  
if gg['m'](value1) == 1:
    b =  gg['b']
    s =  gg['s']("01e1")
    print(f"{b}{s}/{value1}/이미지명.*")

# print(gg['m'](value1)) # 1
# print(gg['m'](value2)) # 0
# print(gg['s']("01e1")) # 481
# print(gg['b']) # 1678262402/
