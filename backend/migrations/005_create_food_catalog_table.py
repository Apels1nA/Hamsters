import peewee as pw


def migrate(migrator, database, fake=False, **kwargs):

    @migrator.create_model
    class FoodCatalog(pw.Model):
        name = pw.CharField()
        recovery_satiety = pw.IntegerField()
        price = pw.IntegerField()  
        

def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('food_catalog')