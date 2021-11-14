import db


def write_user_to_the_db(user: dict):
    db.db[str(user['id'])] = user
    db.update_db()


def read_user_from_db(_id):
    return db.db[str(_id)]

