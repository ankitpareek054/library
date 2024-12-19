import jwt
from instance.config import Config

# Generate a JWT token
token = jwt.encode({"user": "admin"}, Config.SECRET_KEY, algorithm="HS256")
print(token)