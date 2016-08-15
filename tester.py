import relayManager
import dronekit


class ShotManager():
    def __init__(self):
        # see the shotlist in app/shots/shots.p
        print "init"

    def Start(self, vehicle):

        self.vehicle = vehicle
        # Initialize relayManager
        self.relayManager = relayManager.RelayManager(self)

target = 'udp:127.0.0.1:14551' #'tcp:127.0.0.1:5760'
print 'Connecting to ' + target + '...'
vehicle = dronekit.connect(target, wait_ready=True)


sm = ShotManager()

sm.Start(vehicle)
