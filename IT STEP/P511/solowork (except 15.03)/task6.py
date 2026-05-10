import random

def connect_to_server():
    if random.choice([True, False]):
        return "Connection OK"
    else:
        raise ConnectionError("Connection error")

try:
    status = connect_to_server()
    print(status)
except ConnectionError:
    print("Cant connect to server")
finally:
    print("operation ended")