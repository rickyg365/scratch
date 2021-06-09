from ppadb.client import Client

client = Client(host="127.0.0.1", port=5037)
devices = client.devices()

print(devices)
