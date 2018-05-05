class Probe():
    sampleID=0
    dateTime=""
    sourceCode=0
    latitude=0.0
    longitude=0.0
    altitude=0
    speed=0
    heading=0
    out = []


    def __init__(self, row):
        self.sampleID=int(row[0])
        self.dateTime=row[1]
        self.sourceCode=row[2]
        self.latitude=float(row[3])
        self.longitude=float(row[4])
        self.altitude=row[5]
        self.speed=row[6]
        self.heading=row[7]
        
