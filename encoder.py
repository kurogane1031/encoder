#!/usr/bin/env python3

import serial
import numpy
usb_port = '/dev/ttyUSB0'
baud_rate = 115200

if __name__ == "__main__":
    try:
        ser = serial.Serial(usb_port, baud_rate)
        print(f'{ser.name} successfully initialized')
    except:
        print(f'{usb_port} not found. Please CHMOD to others.')
    while True:
        raw_arduino_data = ser.readline()
        ser.flush()
        # print(raw_arduino_data)
        try:
            raw_arduino_data = int(raw_arduino_data[0:len(raw_arduino_data) - 2], 10)
            revolution = raw_arduino_data / 1440.0 # kaiten pulse = 360 count = 360 * 4 = 1440 (1 pulse = 4 count)
            velocity_ms = round(revolution * 2.0 * 0.125 * numpy.pi, 3) * 100.0
            velocity_kmh = round(revolution * 2.0 * 0.125 * numpy.pi * 3.6, 3) * 100.0
            print(f'rev : {revolution:.3f}, m/s : {velocity_ms:.3f}, km/h : {velocity_kmh:.3f}')
        except:
            pass
