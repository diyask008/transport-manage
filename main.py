import time 
import random 
from azure.iot.device import IoTHubDeviceClient 
CONNECTION_STRING = " HostName=hostforiotproject.azure-devices.net;DeviceId=raspberry-pi
004;SharedAccessKey=qghd30aseqgh456sd" 
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING) 
def simulate_sensor_data(): 
    temperature = random.uniform(10.0, 40.0) 
    humidity = random.uniform(20.0, 80.0) 
    return {"temperature": temperature, "humidity": humidity} 
def preprocess_and_filter(data): 
    if data["temperature"] < 0 or data["temperature"] > 50: 
        return None 
    if data["humidity"] < 0 or data["humidity"] > 100: 
        return None 
    return data 

 
while True: 
    try: 
        sensor_data = simulate_sensor_data() 
        processed_data = preprocess_and_filter(sensor_data) 
        if processed_data: 
            message = str(processed_data) 
            client.send_message(message) 
            print(f"Message sent: {message}") 
        time.sleep(10)  
    except Exception as e: 
        print(f"Error: {str(e)}") 
client.shutdown() 
