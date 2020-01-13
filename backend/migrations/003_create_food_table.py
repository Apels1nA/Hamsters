import peewee as pw


def migrate(migrator, database, fake=False, **kwargs):

    class User(pw.Model):
        pass

    @migrator.create_model
    class Food(pw.Model):
        name = pw.CharField()
        recovery_satiety = pw.IntegerField()
        user_id = pw.ForeignKeyField(User,backref='food')
        

def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('food')