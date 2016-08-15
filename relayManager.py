# RelayManager
# shotmanager
#
# Sends a command to a relay attached to a serial port when camera is trigged (Also records locations to file).
#
# Created by George Raber 8/12/16
#  Copyright (c) 2016 The University of Southern Mississippi. All rights reserved.


#!/usr/bin/env python

import serial
import os
import glob
import time

LOG_DIR = '/log/rCam/'


def cSerial(seconds, sport):
    sport.write("relay on "+ str(0) + "\n\r")
    time.sleep(seconds)
    sport.write("relay off "+ str(0) + "\n\r")

class RelayManager():
        
        def __init__(self, shotmgr):
                # initialize shotmanager object
                self.shotmgr = shotmgr
                self.vehicle = self.shotmgr.vehicle
                self.sPort = None

                self.registerCallbacks()
                if not os.path.exists(LOG_DIR):
                     os.makedirs(LOG_DIR)

                self.dataFile = time.strftime("%Y%m%d-%H%M%S") + ".log"

                temp_list = glob.glob ('/dev/tty[A-Za-z]*')

                for t in temp_list:
                        if "ttyACM" in t:
                                self.sPort = serial.Serial(t, 19200, timeout=1)

        def registerCallbacks(self):
            self.vehicle.add_attribute_listener('mode', self.mode_callback) #register with vehicle class (dronekit)
            self.vehicle.add_message_listener('CAMERA_FEEDBACK', self.camera_feedback_callback) #register with vehicle class (dronekit)

        #Camera takes a picture and writes location out to text file.
        #The location is a little behind the picture, probably best to use mission planner to geotag anyway
        def camera_feedback_callback(self, vehicle, name, msg):
                self.logFile = open(LOG_DIR + self.dataFile, "a")
                
                if self.sPort == None:
                        print "No Serial Relay installed"
                else:
                        cSerial(0.25, self.sPort)
                #        p = Process(target=cSerial, args=(0.2, self.sPort))
                #        p.start()

                self.logFile.write(str(msg.time_usec) + "," + str(float(msg.lat) / 10000000.0) + "," + str(float(msg.lng) / 10000000.0) + "," + str(msg.alt_rel) + "\n")
                print msg.time_usec, msg.lat * 10000000, msg.lng * 10000000, msg.alt_rel
                self.logFile.flush()
                self.logFile.close()

        #Have Camera Take Picture on Mode Change
        #This helps in testing and also ensures camera does not fall asleep before timeing out
        #Also creates a picture at a known event in the log file incase camera clock is off
        def mode_callback(self, vehicle, name, mode):

                if self.sPort == None:
                        print "No Serial Relay installed"
                else:
                        cSerial(0.25, self.sPort)

                self.logFile = open(LOG_DIR + self.dataFile, "a")
                self.logFile.write(str(mode) + "\n")
                print mode
                self.logFile.flush()
                self.logFile.close()

