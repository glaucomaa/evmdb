import db


def write_user_to_the_db(user: dict):
    db.db[str(user['id'])] = user
    db.update_db()
    return 0,


def read_user_from_db(_id):
    if str(_id) in db.db:
        return 0, db.db[str(_id)]
    return 1,

