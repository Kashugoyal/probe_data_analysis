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
    shape_points = [] #includes the nodes also
    non_reference_node=None


    def __init__(self, row):
        self.linkPVID=row[0]
        self.refNodeID=row[1]
        self.nrefNodeID=row[2]
        self.length=float(row[3])
        self.functionalClass=row[4]
        self.directionOfTravel=row[5]
        self.speedCategory=row[6]
        self.fromRefSpeedLimit=row[7]
        self.toRefSpeedLimit=row[8]
        self.fromRefNumLanes=row[9]
        self.toRefNumLanes=row[10]
        self.multiDigitized=row[11]
        self.urban=row[12]
        self.timeZone=row[13]
        self.shapeInfo=row[14]
        if len(row)>15:
            self.curvatureInfo=row[15]
        if len(row)>16:
            self.slopeInfo=row[16]
        self.shape_points=[]

        self.read_shapeInfo()

    def read_shapeInfo(self):
        data=self.shapeInfo.split('|')
        self.reference_node = node.Node(data[0])

        self.non_reference_node = node.Node(data[len(data)-1])
        for item in data:
            obj_node=node.Node(item)
            self.shape_points.append(obj_node)

