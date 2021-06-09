import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('immobili.db')
curs = conn.cursor()

try:
    curs.execute("DROP table immobile")
    curs.execute("DROP table catalogo")
except:
    pass


curs.execute("CREATE table immobile (riferimento char(30), proprietario char(30), indirizzo char(30), citta char(30), prezzo int, catalogo char(30))")

class Immobile():
    def __init__(self, riferimento, prezzo, proprietario, indirizzo, citta):
        self.riferimento = riferimento
        self.prezzo = prezzo
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.citta = citta
    

    def modifica_prezzo(self,newprezzo):
        self.prezzo = newprezzo
        print("Il prezzo è stato modificato")


    def stampa(self):
        print(" L'Immobile: %s \n Indirizzo: %s , %s \n prezzo: %s \n Proprietario: %s \n "%(self.riferimento,self.citta,self.indirizzo,self.prezzo,self.proprietario))


class Catalogo():

    def __init__(self, nome, cursore):
        self.nome = nome
        self.cursore = cursore
        self.immobili = []

    def aggiungi_immobile(self,immobile):
        self.immobili.append(immobile)
        row = (immobile.riferimento, immobile.proprietario, immobile.indirizzo,immobile.citta, immobile.prezzo, self.nome)
        self.cursore.execute("insert into immobile values(?, ?, ?, ?, ?, ?)",row)
        print("Immobile aggiunto con successo!")

    def cancella_immobile(self,immobile):
        if immobile in self.immobili:
            self.immobili.remove(immobile)
            self.cursore.execute("delete from immobile where riferimento = ?",(immobile.riferimento,))
            print("immobile rimosso")
        else:
            print("L'immobile non esiste")


    def cerca_immobile(self,proprietario):
        print("Il proprietario cercato possiede i seguenti immobili: \n")
        for immobile in self.immobili:
            if immobile.proprietario == proprietario:
                immobile.stampa()
        
        print("dal database:")
        self.cursore.execute("SELECT * FROM immobile WHERE proprietario = ?",(immobile.proprietario,))
        for row in self.cursore.fetchall():
            print(row)

    def modifica_prezzo(self, newprezzo, riferimento):
        self.cursore.execute("UPDATE immobile SET prezzo = ? WHERE riferimento = ?",(newprezzo, riferimento))
        print("prezzo aggiornato")

    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa()


myImmobile = Immobile(1,500,"Pietro","via Roma,4","Grosseto")
myImmobile2 = Immobile(2,700,"Marco","via Roma, 55","Grosseto")
myImmobile4 = Immobile(4,500,"Pietro","via Roma,4222","Grosseto")
myImmobile3 = Immobile(3,600,"Carlo","via Roma,66","Grosseto")
myImmobile.stampa()
myImmobile.modifica_prezzo(600)
myImmobile.stampa()

myCatalogo = Catalogo("Villa",curs)
myCatalogo.aggiungi_immobile(myImmobile)
myCatalogo.aggiungi_immobile(myImmobile2)
myCatalogo.aggiungi_immobile(myImmobile3)
myCatalogo.aggiungi_immobile(myImmobile4)
myCatalogo.stampa_catalogo()

myCatalogo.cancella_immobile(myImmobile)

myCatalogo.stampa_catalogo()

myCatalogo.cerca_immobile("Pietro")


conn.commit()
conn.close()