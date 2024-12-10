# check collision
def getDistance(obj1, obj2):
    distance = ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
    return distance 