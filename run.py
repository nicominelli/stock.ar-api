from app import create_app
from app.utils.environment import get_env

app = create_app(get_env())
