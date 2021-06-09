import pickle


class Immobile():
    def __init__(self, id, prezzo, proprietario, indirizzo, citta):
        self.id = id
        self.prezzo = prezzo
        self.proprietario = proprietario
        self.indirizzo = indirizzo
        self.citta = citta
    

    def modifica_prezzo(self,newprezzo):
        self.prezzo = newprezzo
        print("Il prezzo è stato modificato")


    def stampa(self):
        print(" L'Immobile: %s \n Indirizzo: %s , %s \n prezzo: %s \n Proprietario: %s \n "%(self.id,self.citta,self.indirizzo,self.prezzo,self.proprietario))

class Catalogo():

    def __init__(self, nome):
        self.nome = nome
        self.file = self.nome + '.p'
        self.immobili = []

    def aggiungi_immobile(self,immobile):
        self.immobili.append(immobile)
        print("Immobile aggiunto con successo!")

    def cancella_immobile(self,immobile):
        if immobile in self.immobili:
            self.immobili.remove(immobile)
            print("immobile rimosso")
        else:
            print("L'immobile non esiste")


    def cerca_immobile(self,proprietario):
        print("Il proprietario cercato possiede i seguenti immobili: \n")
        for immobile in self.immobili:
            if immobile.proprietario == proprietario:
                immobile.stampa()


    def stampa_catalogo(self):
        for immobile in self.immobili:
            immobile.stampa()

    def leggi(self):
        with open(self.file, 'rb') as file:
            self.immobili = pickle.load(file)
        print("Caricamento effettuato!")


    def salva(self):
        with open(self.file, 'wb') as file:
            pickle.dump(self.immobili, file)
        print("Salvataggio effettuato!")

'''
myImmobile = Immobile(1,500,"Pietro","via Roma,4","Grosseto")
myImmobile2 = Immobile(2,700,"Marco","via Roma, 55","Grosseto")
myImmobile4 = Immobile(4,500,"Pietro","via Roma,4222","Grosseto")
myImmobile3 = Immobile(3,600,"Carlo","via Roma,66","Grosseto")
myImmobile.stampa()
myImmobile.modifica_prezzo(600)
myImmobile.stampa()

myCatalogo = Catalogo("Villa")
myCatalogo.aggiungi_immobile(myImmobile)
myCatalogo.aggiungi_immobile(myImmobile2)
myCatalogo.aggiungi_immobile(myImmobile3)
myCatalogo.aggiungi_immobile(myImmobile4)
myCatalogo.stampa_catalogo()

myCatalogo.cancella_immobile(myImmobile)

myCatalogo.stampa_catalogo()

myCatalogo.cerca_immobile("Pietro")

myCatalogo.salva()
 ''' 


CatalogoSalvato = Catalogo("Villa")
CatalogoSalvato.leggi()
CatalogoSalvato.stampa_catalogo()