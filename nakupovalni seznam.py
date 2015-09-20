# -*- coding: utf-8 -*-

__author__ = 'Tomaž'

nakupovalni_listek = []
def zagon():
    izbira = raw_input ("Ali zelite dodati kaksen izdelek na seznam?")
    if izbira == "da":
        novo()
    elif izbira == "ne":
        quit()
    else:
        izbira2 = raw_input("da/ne?")
        if izbira2 == "da":
            novo()
        elif izbira2 == "ne":
            quit()
def novo():
    izdelek = raw_input("Napisite izdelek, ki ga zelite dodati:")
    nakupovalni_listek.append(izdelek)
    dodatni_izdelek = raw_input("Ali zelite v seznam dodati se kaksen izdelek?")
    if dodatni_izdelek == "da":
        novo()
    elif dodatni_izdelek == "ne":
        print(nakupovalni_listek)
    else:
        izbira2 = raw_input("da/ne?")
        if izbira2 == "da":
            novo()
        elif izbira2 == "ne":
            quit()
zagon()
novo()

#izdelki_cene = {"mleko": 2.25, "kruh": 1.68, "jajca": 3.15, "sok": 1.22, "salama": 1.43, "jogurt": 2.87}

#izbira = raw_input("Izberi izdelek: ")

#if izbira in izdelki_cene.keys():
#    cena = izdelki_cene[izbira]
#    print "Cena izdelka je %s" % cena
#else:
#    print "Izdelka ni na zalogi."
