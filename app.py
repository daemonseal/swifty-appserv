import time
import ttn

print("Starting app...")

app_id = "swiflet-env-ctl"
access_key = "ttn-account-v2.K95QNh-Gfu05j6l6IkRglhgKUcFcnNiDYFbou3HOcrE"

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)

def connect_callback(res, client):
  if res:
    print("Connected to the broker")

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.set_connect_callback(connect_callback)

# Target device
dev_id = "rak-node02"
payload = {
  "led_state": "off",
  "counter": 1
}

mqtt_client.connect()

while True:
  mqtt_client.send(dev_id, payload, port=1)
  time.sleep(60)

mqtt_client.close()

# using application manager client
# app_client =  handler.application()
# my_app = app_client.get()
# print(my_app)
# my_devices = app_client.devices()
# print(my_devices)
