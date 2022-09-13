
from base64 import b64encode

sonar_token = 'eace147bc3a2803105be594877292ea24668d44a'


def encode_token(sonar_token):
    print(sonar_token.encode("ascii"))
    print(b64encode(sonar_token.encode("ascii")))
    return b64encode(sonar_token.encode("ascii")).decode("ascii")


def encode_token_utf(sonar_token):
    print(sonar_token.encode())
    print(b64encode(sonar_token.encode()))
    return b64encode(bytes(sonar_token, 'UTF-8')).decode()


print(encode_token(sonar_token))
print(encode_token_utf(sonar_token))