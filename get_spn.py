def get_spn(toponym):
    lowerCorner = toponym['boundedBy']['Envelope']['lowerCorner'].split()
    upperCorner = toponym['boundedBy']['Envelope']['upperCorner'].split()
    delta_x = float(upperCorner[0]) - float(lowerCorner[0])
    delta_y = float(upperCorner[1]) - float(lowerCorner[1])
    return ",".join([str(delta_x), str(delta_y)])