# HerbControl - Source
This directory contains all the source code for the project as well as the directory which holds the main components of the webpage. Please view the list below in order to understand the details of each file in this directory. 

# Information on Components
- AirTempHum.py -> this file controls the air temperature and humidity sensor. It is used in the Sensors.py file to obtain measurements and store them in the database.
- Database.py -> this file creates a connection with the sqlite database. It used when storing measurements in the database. 
- RealaySwitch.py -> This file uses the VoltageControl.py file to send current to the relay switch. This file is used in conjunction with crontab in order to automatically turn on and off the LED lights.
- Sensors.py -> This file controls the measurement taking of all sensors, inserting the data in the database and also sending out test messages in case in values are out of range. It works together with crontab in order to do this automatically.
- SoilMoisture.py -> This file takes the measurements from the soil moisture sensor.
- TextMessage.py -> This file sends out text messages to the user using the Twilio account.
- VoltageControl.py -> This file sends out High or Low voltage to port which the relay switch is connected to.
- Watchdog.py -> This file represents the watchdog and it shuts down the system and warns the user in case the Sensors.py file has not been executed.