from kivy.uix.popup import Popup
from kivy.uix.label import Label
from plyer import vibrator

def show_alert():
    alert_popup = Popup(title="Alert", content=Label(text="Maintain at least 6 feet distance!"), size_hint=(None, None), size=(400, 200))
    alert_popup.open()
    vibrate()

def vibrate():
    try:
        vibrator.vibrate(1)  # Vibrate for 1 second
    except NotImplementedError:
        print("Vibration not supported on this platform")
