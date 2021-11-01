#ik ben van plan om een quiz te maken.
print("hello, wat is jouw naam")
name = input ("type je naam ")
#-------------------------------------------------------------------
print("Welkom "+ name )
start = input("wil je een quiz maken " + name + " ") 

if start == "ja":
    print("mooi zo laten we beginnen met de eerste vraag. ")
else:
    print("oke doei")
#------------------------------------------------------------------
eerste_vraag = input("vind je de opleiding leuk? ")

if eerste_vraag == "ja":

    print("dat is mooi om te horen!")
else:
    print("dat is jammer. Je kan nog van opleiding veranderen.")
#-----------------------------------------------------------------
tweede_vraag = input("heb je al je werk af? ")

if tweede_vraag == "ja":
    print("goed zo je bent ook bijna klaar met de quiz!")
else:
    print("waarom ben je hier?! ga je werk maken!")
#-----------------------------------------------------------------
laaste_vraag = input("ben je trots op je zelf? ")

if laaste_vraag == "ja":
    print("ik ben ook trots op jouw")
else:
    print("ik ben ook teleurgesteld in je")

print("eind quiz")

