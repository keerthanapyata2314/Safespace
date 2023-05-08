import asyncio
import math
import requests
from bleak import BleakScanner, BleakError
from datetime import datetime

def calculate_distance(rssi, tx_power):
    if rssi == 0:
        return -1.0
    ratio = rssi * 1.0 / tx_power
    if ratio < 1.0:
        return math.pow(ratio, 10)
    else:
        distance = (0.89976) * math.pow(ratio, 7.7095) + 0.111
        return distance

def get_device_type(device):
    if device is None:
        return 'Unknown'

    device_type_mapping = {
        'phone': 'Smartphone',
        'watch': 'Wearable',
        'beacon': 'Beacon'
    }

    for keyword, device_type in device_type_mapping.items():
        if device.name and keyword.lower() in device.name.lower():
            return device_type

    return 'Unknown'

def get_device_manufacturer(device):
    manufacturer_data = device.metadata.get('manufacturer_data', {})

    for key in manufacturer_data:
        company_name = get_company_name_by_id_with_error_handling(key)
        if company_name:
            return company_name

    return 'Unknown'

def get_company_name_by_id(company_id):
    url = f'https://www.bluetooth.com/wp-json/wp/v2/company?per_page=1&search={company_id}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        if len(json_data) > 0:
            return json_data[0].get('title', {}).get('rendered', 'Unknown')

    return None

def get_company_name_by_id_with_error_handling(company_id):
    try:
        return get_company_name_by_id(company_id)
    except Exception as e:
        print(f"Error getting company name by ID: {e}")
        return None

async def scan_bluetooth():

    devices = []
    error_message = None

    try:
        scanner = BleakScanner()
    except BleakError as e:
        print(f"Error: {e}")
        error_message = str(e)
        return devices, error_message

    devices = await scanner.discover()
    return devices, error_message

