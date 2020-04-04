from app.models import *
from app.utils.auth import hash_password
from app.utils.environment import get_env, Environment


def check_db():
    env = get_env()
    if env != Environment.PRODUCTION:
        build_db()


def build_db():
    db.drop_all()
    db.create_all()

    db.session.commit()
