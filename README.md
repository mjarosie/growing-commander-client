### Growing commander - client

This is the application for gathering the growing measurement using multiple sensor devices, 
aggregate them and send them to the [Growing Commander Server](https://github.com/mjarosie/growing-commander-server)
application trough available REST API.

### Setup and currently supported sensors

Application was tested on Raspberry Pi 3. Sensors connected to the device:

- AM2302 powered with 3.3V (GPIO 4)

### Running tests

In order to run tests:

``` python -m unittest discover ```
