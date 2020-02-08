from app.models.user import User


class DatabaseMigration:

    def up(self):
        User().migrate()

    def down(self):
        User().drop()