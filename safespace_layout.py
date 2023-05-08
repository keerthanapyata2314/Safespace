import asyncio
from datetime import datetime, timedelta
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import bluetooth_scanner
from alert_system import show_alert
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class FilterDialogContent(MDBoxLayout):
    pass


class SafeSpaceLayout(MDBoxLayout):
    error_label = ObjectProperty(None)

    scanning = False

    last_scan_time = None

    def start_stop_scanning(self):
        if self.scanning:
            self.scanning = False
            self.ids.status_label.text = "Status: Stopped"
        else:
            self.scanning = True
            self.ids.status_label.text = "Status: Scanning"
            Clock.schedule_interval(lambda dt: asyncio.run(self.scan_and_process_devices(dt)), 10)


    async def scan_and_process_devices(self, dt):
        if not self.scanning:
            return

        devices, error_message = await bluetooth_scanner.scan_bluetooth()

        if error_message:
            self.ids.error_label.text = error_message  # Update the text attribute
        else:
            self.ids.error_label.text = ''  # Clear the text attribute
            filtered_devices = []

            for device in devices:
                if not self.filter_device(device):
                    continue

                distance = bluetooth_scanner.calculate_distance(device.rssi, -59)

                if distance < 6:
                    show_alert()
                    self.ids.distance_label.text = f"Distance: {distance:.2f} feet"

                filtered_devices.append((device.name, distance))

            self.last_scan_time = datetime.now()



    def filter_device(self, device):

        return (

            self.filter_by_name(device) and

            self.filter_by_type(device) and

            self.filter_by_manufacturer(device) and

            self.filter_by_rssi(device) and

            self.filter_by_detection_time(device) and

            self.filter_by_connection_status(device) and

            self.filter_by_proximity_zone(device)

        )

    def filter_by_name(self, device):

        return not self.ids.device_name_input.text or self.ids.device_name_input.text.lower() in device.name.lower()

    def filter_by_type(self, device):

        device_type = bluetooth_scanner.get_device_type(device)

        return self.ids.device_type_spinner.text == "All" or device_type == self.ids.device_type_spinner.text

    def filter_by_manufacturer(self, device):

        manufacturer = bluetooth_scanner.get_device_manufacturer(device)

        return self.ids.device_manufacturer_spinner.text == "All" or manufacturer == self.ids.device_manufacturer_spinner.text

    def filter_by_rssi(self, device):

        return device.rssi >= self.ids.rssi_slider.value

    def filter_by_detection_time(self, device):

        if self.ids.detection_time_spinner.text == "All":

            return True

        detection_time_minutes = int(
            self.ids.detection_time_spinner.text.split(' ')[0])

        return not self.last_scan_time or datetime.now() - self.last_scan_time <= timedelta(minutes=detection_time_minutes)

    def filter_by_connection_status(self, device):

        if self.ids.connection_status_spinner.text == "All":

            return True

        return (

            (self.ids.connection_status_spinner.text == "Connected" and device.connected) or

            (self.ids.connection_status_spinner.text ==
             "Disconnected" and not device.connected)

        )

    def filter_by_proximity_zone(self, device):

        distance = bluetooth_scanner.calculate_distance(device.rssi, -59)

        if self.ids.proximity_zone_spinner.text == "All":

            return True

        return (

            (self.ids.proximity_zone_spinner.text == "Immediate" and distance <= 1) or

            (self.ids.proximity_zone_spinner.text == "Near" and 1 < distance <= 6) or

            (self.ids.proximity_zone_spinner.text == "Far" and distance > 6)

        )

    def open_nav_drawer(self):

        self.ids.nav_drawer.set_state("open")
   
    def show_filter_dialog(self):
        filter_dialog = MDDialog(
            title="Filter Settings",
            type="custom",
            content_cls=FilterDialogContent(),
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: filter_dialog.dismiss()),
                MDFlatButton(text="APPLY", on_release=lambda x: filter_dialog.dismiss()),
            ],
        )
        filter_dialog.open()

    
