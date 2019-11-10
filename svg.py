from xml.dom import minidom

TRANSF_SCALE = 12


'''
Cleans an .SVG file by removing all text and then
attempting to remove as much as the surrounding bubble as possible
'''
def clean_svg(svg):
    # Removes all text
    doc = minidom.parse(svg)
    textElements = doc.getElementsByTagName('text')

    for node in textElements:
        parent = node.parentNode
        parent.removeChild(node)

    # Remove bubbles where the numbers go inside of
    # mostly works...
    # inside element g -> inside element path -> attribute = style
    gElements = doc.getElementsByTagName('g')
    for g in gElements:
        pathElements = g.getElementsByTagName('path')
        for path in pathElements:

            # test path.getAttribute('d') if it starts with 'm'
            if (path.getAttribute('style') == 'fill:none;stroke:#000000;stroke-width:6;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:10;stroke-dasharray:none;stroke-opacity:1'):
                pieces = path.getAttribute('d').split(' ')
                
                # m 6547,11818 v 230 (example)
                if (len(pieces) == 4 and ((pieces[2] == 'v')) or (pieces[2] == 'V')):
                    if (((int(pieces[3])) > -600 and (int(pieces[3]) < 600))
                    or (int(pieces[3])) > 7000 and (int(pieces[3]) < 10000)):
                        parent = path.parentNode # g
                        parent.removeChild(path) # remove child of g
                # M 0,-71.5 C 39.48836,-71.5 71.5,-39.48836 71.5,0 71.5,39.48836 39.48836,71.5 0,71.5 (example)
                elif (len(pieces) == 9):
                    if (pieces[0] == 'M' and pieces[2] == 'C'):
                        parent = path.parentNode # g
                        parent.removeChild(path) # remove child of g
            
    # Writes to a new SVG file
    doc.writexml(open('cleaned.svg', 'w'),
               indent="  ",
               addindent="  ",
               newl='\n')

    doc.unlink()


'''
HELPER FUNCTION:
Get the relative coordinates (percentages) of the room numbers
on the blueprint

max = height/width * TRANSF_CONST
min = 0 for now
'''
def get_relative_coord(transf_coord, min_transf, max_transf):
    transf_coord -= min_transf
    max_transf -= min_transf

    return 1 - transf_coord / max_transf


'''
Validates if a room number is actually a room number
(does it have numbers, is it the right length, etc)
'''
def valid_room(roomName):
    flag = True
    length = len(roomName)
    for i in range(length - 1):
        if not roomName[i].isdigit():
            flag = False
    if length < 2 or length > 4 or roomName[len(roomName) - 1] == '\'':
        flag = False

    return flag


'''
Maps the rooms and coordinates to a dictionary
and returns the dictionary
'''
def map_rooms(svg):
    rooms = {}

    doc = minidom.parse(svg)  # parseString also exists

    textElements = doc.getElementsByTagName('text')

    svg = doc.getElementsByTagName('svg')[0]

    height = int(svg.getAttribute('height'))

    width = int(svg.getAttribute('width'))

    min_transf_x = 0
    min_transf_y = 0

    max_transf_x = width * TRANSF_SCALE
    max_transf_y = height * TRANSF_SCALE

    for textElement in textElements:

        tspanElements = textElement.getElementsByTagName('tspan')
        for tspanElement in tspanElements:
            roomName = tspanElement.firstChild.nodeValue

        transformElement = textElement.getAttribute('transform')

        pieces = transformElement.split(",")

        transf_x = int(pieces[5].replace(")", ""))
        transf_y = int(pieces[4])

        relative_x = get_relative_coord(transf_x, min_transf_x, max_transf_x)
        relative_y = get_relative_coord(transf_y, min_transf_y, max_transf_y)

        if(valid_room(roomName)):
            rooms[roomName] = (relative_x, relative_y)
            #print(roomName)  # a string

    doc.unlink()
    return rooms

### TESTING PURPOSES
rooms = map_rooms('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')

for entry in rooms:
    print('Room number: ' + entry)
    print(rooms[entry])

#rooms = map_rooms('Cardwell Hall Floor 1.svg')

#clean_svg('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')