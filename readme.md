# Planning and Design Milestone

In this milestone, we have designed and planned the Social Distance Monitoring mobile application using the Kivy framework. The application aims to leverage Bluetooth technology to track and measure the proximity of individuals in various spaces, to help users adhere to social distancing guidelines and reduce the risk of virus transmission.

## Features

### Bluetooth Functionality
We will be using the PyBluez library to implement Bluetooth functionality in the app. The app will detect Bluetooth signals from nearby devices and store them for further processing.

### Signal Processing
The Numpy library will be used to process the Bluetooth signals and calculate the estimated distance between devices. We will apply a distance estimation algorithm that takes into account factors such as signal strength, noise, and interference to improve accuracy.

### Filtering
The application will allow users to filter devices based on several parameters, such as signal strength, device type, manufacturer, time, and custom tags or identifiers. This feature will enable users to focus on relevant devices and reduce noise in the data. We will implement the filtering system using a combination of PyBluez and Numpy libraries.

### Alerts
The application will alert users if they are closer than the recommended safe distance from another device. We will use customizable vibrations, sounds, and visual indicators to provide feedback to users. The alerts will be triggered based on the estimated distance between devices and will be adjustable based on user preferences.

### User Interface
We will create a user-friendly interface using the Kivy framework and PyCharm IDE. The interface will allow users to interact with the app's features, such as filtering, alerts, and device information. We will use a combination of buttons, sliders, and text inputs to provide a seamless user experience.

### Proximity Zones
The app will implement proximity zones (e.g., immediate, near, and far) based on the estimated distance between devices. Users can then choose to filter devices within specific proximity zones. We will implement this feature using a combination of PyBluez and Numpy libraries.

### Custom Device Name Filter
We will add a more sophisticated filtering system by allowing users to enter a custom device name filter in the app's UI. This feature will enable users to search for specific devices by name and further refine their filtering criteria.

## Libraries

We have chosen to use the following libraries for their efficiency, ease of use, and popularity in the Python community:

- Kivy - to create the UI and handle touch events
- PyBluez - to access Bluetooth functionality
- Numpy - to handle signal processing and data analysis

## Implementation

We plan to implement the application in several stages:

1. Design and develop the UI using Kivy and PyCharm IDE.
2. Integrate Bluetooth functionality using PyBluez.
3. Detect and store Bluetooth signals using Numpy.
4. Process and classify Bluetooth signals to estimate distance and detect proximity violations.
5. Implement filtering, proximity zones, and alerts based on the features mentioned above.
6. Test and debug the application on various devices with Bluetooth capabilities.

We aim to create a robust, accurate, and user-friendly application that promotes and monitors social distancing measures in public spaces. We will follow best practices in software development, such as testing and documentation, to ensure a high-quality outcome.
