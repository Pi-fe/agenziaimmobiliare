import peewee


db = peewee.SqliteDatabase("immobili_peewee.db")


class CatalogoImm(peewee.Model):
    riferimento = peewee.CharField()
    proprietario = peewee.CharField()
    indirizzo = peewee.CharField()
    citta = peewee.CharField()
    prezzo = peewee.IntegerField()
    catalogo = peewee.CharField()

    class Meta:
        database = db
        db_table = 'immobili'

CatalogoImm.create_table(CatalogoImm)

casa1 = CatalogoImm.create(riferimento ="1A", proprietario = "Pietro", indirizzo =  "via roma 3", citta=  "Grosseto", prezzo = 300, catalogo = "Ville")


casa1.save()

immobili = CatalogoImm.select()

for immobile in immobili:
    print(immobile.riferimento, immobile.proprietario)
