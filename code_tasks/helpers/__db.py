import json
import uuid
from random import randint


def db_mock_with_exception(data: bytes):
    if randint(0, 10) % randint(1, 3) == 0:
        raise BaseException
    return json.dumps({"id": str(uuid.uuid4()), "content": data.decode()})
