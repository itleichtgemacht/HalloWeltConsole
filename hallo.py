# Mit import wird ein Modul geladen. In diesem Beispiel
# das "time" Modul, um die aktuelle Stunde zu ermitteln
import time

# hier wird aus der aktuellen lokalen Uhrzeit des rechners
# die Stunden in die Variable "stunde" gespeichert 
stunde = time.localtime()[3]

# Nun wird der Benutzer nach seinem Namen gefragt,
# den er eingeben kann
name = input("Bitte Name eingeben: ")

# haben wir vor 12 Uhr wird "Guten Morgen" und der Name ausgegeben 
if stunde < 12:
    print("Guten Morgen", name)
# haben wir zwischen 12 und 18 Uhr geben wir "Guten Tag" aus 
elif stunde >= 12 and stunde < 18:
    print("Guten Tag", name)
# Und ansosnten geben wir "Gute Nacht" aus 
else:
    print("Gute Nacht", name)
    