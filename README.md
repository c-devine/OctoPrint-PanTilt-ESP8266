# OctoPrint-PanTilt-ESP8266

This plugin extends the plugin controls developed by [Salandora](https://github.com/Salandora/OctoPrint-PanTilt) and adds support
for a simple and low cost 2 axis gimbal bracket.  The plugin uses the web cam controls (added through the Octoprint-PanTilt plugin) located on the
control tab.

This implementation uses a ESP-8266 development board as the controller for the gimbal.  The ESP8266
is controlled over wifi, and powered through the USB port. This plugin has had very limited testing!!

## Setup

First, the base Octoprint-PanTilt plugin needs to be installed from here:
https://github.com/c-devine/OctoPrint-PanTilt/archive/command-handler.zip

see [command-handler topic](https://github.com/c-devine/OctoPrint-PanTilt/tree/command-handler)

Then install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/c-devine/OctoPrint-PanTilt-ESP8266/archive/master.zip


## Video

[![PanTilt ESP8266 Video](https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266/snapshots/assets/img/youtube-8266.png?raw=true)](https://www.youtube.com/watch?v=sj92Br_dFW8 "PanTilt-ESP8266")


## Hardware

The 2 axis servo gimbals can be found on ebay and other [online](https://www.google.com/search?q=ebay+Servo+Mount+bracket+pan+tilt+with+servos&oq=ebay+Servo+Mount+bracket+pan+tilt+with+servos)
 locations.  [ESP8266 development boards](https://www.google.com/search?q=NodeMcu+Lua+WIFI+development+board&oq=NodeMcu+Lua+WIFI+development+board&aqs=chrome..69i57j0l5.1282j0j8&sourceid=chrome&ie=UTF-8) are also pretty easy to find.

3D Printed Part: [C270 Camera Mount Block](https://www.thingiverse.com/thing:2409919)

<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-Nano/snapshots/assets/img/pantilt.png?raw=true" width="320" height="240">
<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-Nano/snapshots/assets/img/webcam.png?raw=true" width="320" height="240">



## Firmware

The [Firmware](https://github.com/c-devine/OctoPrint-PanTilt-ESP8266-Firmware) is located here: https://github.com/c-devine/OctoPrint-PanTilt-ESP8266-Firmware.


## Configuration

### Setup ESP8266
After installing the firmware, the ESP8266 should start up in AP mode - look for the network "wifipantiltAP" and connect to the access point to configure the hostname and other parameters.

<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266/snapshots/assets/img/wifipantiltAP.png?raw=true">

Once connected, you need to add the local network ssid and password, as well as set the host name for the device, in this case "wifipantilt" or another hostname.
Open a web browser and connect to http://192.168.4.1/setup and configure the local network and hostname.


<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266/snapshots/assets/img/wifipantiltAP-setup.png?raw=true">


You can test connection to the network by connecting to it in a web-browser http://your-host-name


<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266/snapshots/assets/img/wifipantilt-hello.png?raw=true" >

### Setup PanTilt Plugin

<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266/snapshots/assets/img/pantilt-plugin-settings.png?raw=true" >

### Setup ESP8266 Plugin

<img src="https://raw.githubusercontent.com/c-devine/OctoPrint-PanTilt-ESP8266/snapshots/assets/img/esp8266-plugin-settings.png?raw=true" >




