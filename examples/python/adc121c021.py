#!/usr/bin/python
# Author: Zion Orent <zorent@ics.com>
# Copyright (c) 2015 Intel Corporation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_adc121c021 as upmAdc121c021

def main():
    # Instantiate an ADC121C021 on I2C bus 0
    busID = upmAdc121c021.ADC121C021_I2C_BUS
    I2CAddr = upmAdc121c021.ADC121C021_DEFAULT_I2C_ADDR

    myAnalogDigitalConv = upmAdc121c021.ADC121C021(busID, I2CAddr)

    ## Exit handlers ##
    # This stops python from printing a stacktrace when you hit control-C
    def SIGINTHandler(signum, frame):
        raise SystemExit

    # This lets you run code on exit,
    # including functions from myAnalogDigitalConv
    def exitHandler():
        print("Exiting")
        sys.exit(0)

    # Register exit handlers
    atexit.register(exitHandler)
    signal.signal(signal.SIGINT, SIGINTHandler)

    # get the data every 50 milliseconds
    while(1):
        val = myAnalogDigitalConv.value()
        voltsVal = myAnalogDigitalConv.valueToVolts(val)
        print("ADC value: %s Volts = %s" % (val, voltsVal))
        time.sleep(.05)

if __name__ == '__main__':
    main()
