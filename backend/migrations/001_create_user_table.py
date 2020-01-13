import peewee as pw


def migrate(migrator, database, fake=False, **kwargs):

    @migrator.create_model
    class User(pw.Model):
        email = pw.CharField(null=True)
        login = pw.CharField(null=True)
        password = pw.CharField(null=True)
        balance = pw.IntegerField(null=True)
        user_id = pw.IntegerField(null=True)
        


def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('user')