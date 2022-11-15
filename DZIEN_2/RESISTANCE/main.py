from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

print("_________________ klasa OldResistor __________________")
r0 = OldResistor(10.2E2)
print(r0)
print(r0._ohms)
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("_________________ klasa Resistor __________________")
r1 = Resistor(50E3)
r1.ohms = 10E3
print(f"układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V, "
      f"\nnatężenie prądu: {r1.current} A")

print("_________________ klasa VoltageResistance __________________")
r2 = VoltageResistance(1E3)
print(f"natężenie początkowe prądu: {r2.current} A")
r2.voltage = 38
print(f"natężenie prądu: {r2.current} A")
print(f"napięcie prądu: {r2.voltage} A")

print("_________________ klasa BoundedResistance __________________")

try:
      r3 = BoundedResistance(1E2)
      r3.ohms = 5E3
      print(f'oporność: {r3.ohms} om')
except ValueError as h:
      print(str(h))
except Exception:
      print("nieoczekiwany błąd!!!")
