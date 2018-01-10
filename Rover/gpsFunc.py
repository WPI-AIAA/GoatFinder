# I used the adafruit tutorial found here: https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all#using-your-gps
#Essentially install gpsd, edit some boot files and go

import gps

# Run this once before reading for the GPS for the first time
def initGPS():
    # Listen on port 2947 (gpsd) of localhost
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

# Get lat and long with readGPS().get('latitude') readGPS().get('longitude')
def readGPS():
    try:
    	report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print report
        if report['class'] == 'TPV':
            if hasattr(report, 'latitude'):
                if hasattr(report, 'longitude'):
                    lat = report.latitude
                    lon = report.longitude
                    return {'latitude':lat, 'longitude':lon}
    except KeyError:
		pass
    """except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "GPSD has terminated""""
