import jwt
import datetime
import environ

env = environ.Env()
environ.Env.read_env()

def create_token(user):
    # Définir les informations de l'utilisateur et la clé secrète

    user_id = user.id
    user_email = user.email
    secret_key = env('SECRET_KEY')

    # Créer le payload du JWT
    payload = {
        "user_id": user_id,
        "email": user_email,
        "exp": datetime.datetime.now(datetime.timezone.utc)
        + datetime.timedelta(hours=2),
    }

    print(payload)

    jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")
    return jwt_token.decode("utf-8")
