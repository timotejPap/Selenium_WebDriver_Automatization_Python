"""
while True:
    try:
        vek = int(input("Zadaj svoj vek: "))
    except:
        print("Zadaj ciselnu hodnotu")
        continue
    if vek < 1:
        print("Zadaj kladne cislo")
        continue
    break
print("Tvoj vek je", vek)
"""
import pyinputplus as pyp
from pyinputplus import inputYesNo
"""
odpoved = pyp.inputInt("Zadaj cele cislo: ", min=18, max=99)
print("Odpoved je: ", odpoved)

odpoved = pyp.inputInt("Zadaj cele cislo: ", lessThan=6, blank=True)
print("Odpoved je: ", odpoved)

odpoved = pyp.inputInt("Zadaj cele cislo: ", limit=3, min=5, max=20, timeout=10)
print("Odpoved je: ", odpoved)

odpoved = pyp.inputInt("Zadaj cele cislo: ", default="NA", limit=3)
print("Odpoved je: ", odpoved)

odpoved = pyp.inputNum("Zadaj cele cislo: ", allowRegexes=[r"(I|V|X|L|C|D|M|i|v|x|l|c|d|m|)+", r"zero"])
print("Odpoved je: ", odpoved)


while True:
    odpoved = pyp.inputYesNo("Umyl si si dnes zuby? ", yesVal="áno", noVal="nie")
    if odpoved == "nie":
        print("Dovidenia")
    else:
        print("Skvelé")
        break
"""
odpoved = pyp.inputMenu(["kura", "rezen", "pizza"], numbered=True)
print("Odpoved je: ", odpoved)