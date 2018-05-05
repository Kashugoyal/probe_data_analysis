import node

class Link():
    linkPVID=0#A
    refNodeID=0#B
    nrefNodeID=0#C
    length=0.0#D
    functionalClass=0#E
    directionOfTravel=''#F
    speedCategory=0#G
    fromRefSpeedLimit=0#H
    toRefSpeedLimit=0#I
    fromRefNumLanes=0#J
    toRefNumLanes=0#k
    multiDigitized=''#L
    urban=''#M
    timeZone=0#N
    shapeInfo=""#O
    curvatureInfo=""#P
    slopeInfo=""#Q

    reference_node=None
    shape_points = []
    non_reference_node=None


    def __init__(self, row):
        self.linkPVID=row[0]
        self.refNodeID=row[2]
        self.nrefNodeID=row[3]
        self.length=row[4]
        self.functionalClass=row[5]
        self.directionOfTravel=row[6]
        self.speedCategory=row[7]
        self.fromRefSpeedLimit=row[8]
        self.toRefSpeedLimit=row[9]
        self.fromRefNumLanes=row[10]
        self.toRefNumLanes=row[11]
        self.multiDigitized=row[12]
        self.urban=row[13]
        self.timeZone=row[14]
        self.shapeInfo=row[15]
        self.curvatureInfo=row[16]
        self.slopeInfo=row[17]

    def read_slopeInfo(self):
        data=self.slopeInfo.split('|')
        self.reference_node = node.Node(data[0])

        self.non_reference_node = node.Node(data[len(data)-1])
        for i in range(1,len(data)-2):
            obj_node=node.Node(data[i])
            self.shape_points.append(obj_node)

