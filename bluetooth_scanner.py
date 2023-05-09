import asyncio
import math
import requests
from bleak import BleakScanner
from datetime import datetime

def calculate_distance(rssi, tx_power):
    if rssi == 0:
        return -1.0

    ratio = rssi * 1.0 / tx_power
    if ratio < 1.0:
        return math.pow(ratio, 10)
    else:
        distance = 0.89976 * math.pow(ratio, 7.7095) + 0.111
        return distance

def get_device_type(device):
    if device is None:
        return 'Unknown'

    # Adjust according to your requirements
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
        # Look up the Bluetooth Company Identifier Codes
        company_name = get_company_name_by_id(key)
        if company_name:
            return company_name

    return 'Unknown'

def get_company_name_by_id(company_id):
    # Use the Bluetooth SIG API to get the company name by its identifier
    url = f'https://www.bluetooth.com/wp-json/wp/v2/company?per_page=1&search={company_id}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        if len(json_data) > 0:
            return json_data[0].get('title', {}).get('rendered', 'Unknown')

    return None

async def scan_bluetooth():
    scanner = BleakScanner()
    devices = await scanner.discover()
    return devices
