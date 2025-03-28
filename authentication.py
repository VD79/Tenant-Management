from itsdangerous import URLSafeTimedSerializer

SECRET_KEY = "your_secret_key"
serializer = URLSafeTimedSerializer(SECRET_KEY)

def create_session_token(data: dict):
    return serializer.dumps(data)

def verify_session_token(token: str):
    try:
        return serializer.loads(token, max_age=600)  # Token valid for 10 min
    except:
        return None