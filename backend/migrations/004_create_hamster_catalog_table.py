import peewee as pw


def migrate(migrator, database, fake=False, **kwargs):

    @migrator.create_model
    class HamsterCatalog(pw.Model):
        breed = pw.CharField()
        price = pw.IntegerField()  
        

def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('hamster_catalog')