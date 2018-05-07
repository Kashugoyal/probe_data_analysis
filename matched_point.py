import link_dist

class Matched_point():
    sampleID=0
    dateTime=""
    sourceCode=0
    latitude=0.0
    longitude=0.0
    altitude=0
    speed=0
    heading=0
    linkPVID=0
    direction=''
    distFromRef=0
    distFromLink=0

    def __init__(self,probe,lID,dir,dfromref,dfromlink):
        self.sampleID=probe.sampleID
        self.dateTime=probe.dateTime
        self.sourceCode=probe
        self.latitude=probe
        self.longitude=probe
        self.altitude=probe.altitude
        self.speed=probe.speed
        self.heading=probe.heading
        self.linkPVID=lID
        self.direction=dir
        self.distFromRef=dfromref
        self.distFromLink=dfromlink


