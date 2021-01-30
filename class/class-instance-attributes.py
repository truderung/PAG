
class PKW:
  definition = "Personenkraftwagen sind mehrspurige Fahrzeuge mit eigenem Antrieb zum vorwiegenden Zweck der Personenbeförderung."


a = PKW()
b = PKW()

print("-1-------------------------")
print(a.definition)
print(b.definition)

print("-1.1-------------------------")
print("PKW(a), Klassentyp: %s, Object-ID: %s, def-ID: %s" % (type(a), id(a), id(a.definition)))
print("PKW(b), Klassentyp: %s, Object-ID: %s, def-ID: %s" % (type(b), id(b), id(b.definition)))


print("-2-------------------------")
PKW.definition = "in Schritt 2 überschrieben"
print(a.definition)
print(b.definition)

print("-2.1-------------------------")
print("PKW(a), Klassentyp: %s, Object-ID: %s, def-ID: %s" % (type(a), id(a), id(a.definition)))
print("PKW(b), Klassentyp: %s, Object-ID: %s, def-ID: %s" % (type(b), id(b), id(b.definition)))


print("-3-------------------------")
a.definition = "in Schritt 3 überschrieben"
print(a.definition)
print(b.definition)

print("-3.1-------------------------")
print("PKW(a), Klassentyp: %s, Object-ID: %s, def-ID: %s" % (type(a), id(a), id(a.definition)))
print("PKW(b), Klassentyp: %s, Object-ID: %s, def-ID: %s" % (type(b), id(b), id(b.definition)))


print("-4-------------------------")
PKW.definition = "in Schritt 4 überschrieben"
print(a.definition)
print(a.__class__.definition)
print(b.definition)

print("-4.1-------------------------")
print("PKW(a), def-ID: %s, class-def-ID: %s" % (id(a.definition), id(a.__class__.definition)))
print("PKW(b), def-ID: %s, class-def-ID: %s" % (id(b.definition), id(b.__class__.definition)))

print("-5-------------------------")
print(a.__class__.__dict__["definition"])
print(a.__dict__["definition"])

print("-5.1-------------------------")
print("PKW(a), class-def-ID: %s, class-def-ID-in-dict: %s" % (id(a.__class__.definition), id(a.__class__.__dict__["definition"])))
print("PKW(a), def-ID: %s, def-ID-in-dict: %s" % (id(a.definition), id(a.__dict__["definition"])))

