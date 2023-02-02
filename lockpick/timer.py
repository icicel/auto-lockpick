import datetime

def startTime():
    global tstart
    tstart = datetime.datetime.now()
def endTime():
    print((datetime.datetime.now() - tstart).total_seconds() * 1000)