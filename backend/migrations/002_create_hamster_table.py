import peewee as pw


def migrate(migrator, database, fake=False, **kwargs):

    class User(pw.Model):
        pass

    @migrator.create_model
    class Hamster(pw.Model):
        name = pw.CharField()
        gender = pw.CharField()
        color = pw.CharField()
        breed = pw.CharField()
        satiety = pw.IntegerField()
        user_id = pw.ForeignKeyField(User,backref='hamster')
        

def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('hamster')