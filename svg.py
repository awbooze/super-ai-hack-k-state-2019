from xml.dom import minidom



# doc = minidom.parse('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')  # parseString also exists

# path_strings = [path.getAttribute('id') for path in doc.getElementsByTagName('text')]



# textElements = doc.getElementsByTagName('text')



# for textElement in textElements:

#     # get tspan element and get room number, and print it

#     tspanElements = textElement.getElementsByTagName('tspan')

#     for tspanElement in tspanElements:

#         roomNumber = tspanElement.firstChild.nodeValue

#         print('Room number: ' + roomNumber)



#     # get transform attribute from text element

#     transformElement = textElement.getAttribute('transform')

#     #print(transformElement) # a string

#     pieces = transformElement.split(",")

#     print("x coord: " + pieces[4])

#     print("y coord: " + pieces[5].replace(")", ""))



# doc.unlink()

TRANSF_SCALE = 12

def clean_svg(svg):

    doc = minidom.parse(svg)  # parseString also exists

    path_strings = [path.getAttribute('id') for path in doc.getElementsByTagName('text')]

    textElements = doc.getElementsByTagName('text')



    for node in textElements:

        parent = node.parentNode

        parent.removeChild(node)



    doc.writexml(open('cleaned.svg', 'w'),

               indent="  ",

               addindent="  ",

               newl='\n')



    doc.unlink()


def get_relative_coord(transf_coord, min_transf, max_transf):
    transf_coord -= min_transf
    max_transf -= min_transf

    return 1 - transf_coord / max_transf

#def valid_room(roomName):
#    for(i in range(len(roomName) - 1)):



def map_rooms(svg):
    rooms = {}

    doc = minidom.parse(svg)  # parseString also exists

    print(doc.getElementsByTagName("height"))

    path_strings = [path.getAttribute('id') for path in doc.getElementsByTagName('text')]

    textElements = doc.getElementsByTagName('text')

    svg = doc.getElementsByTagName('svg')[0]

    height = int(svg.getAttribute('height'))

    width = int(svg.getAttribute('width'))



    min_transf_x = 0
    min_transf_y = 0

    max_transf_x = width * TRANSF_SCALE
    max_transf_y = height * TRANSF_SCALE




    for textElement in textElements:

        # get tspan element and get room number, and print it

        tspanElements = textElement.getElementsByTagName('tspan')

        for tspanElement in tspanElements:

            roomName = tspanElement.firstChild.nodeValue

            print('Room number: ' + roomName)



        # get transform attribute from text element

        transformElement = textElement.getAttribute('transform')

        #print(transformElement) # a string

        pieces = transformElement.split(",")

        transf_x = int(pieces[5].replace(")", ""))
        transf_y = int(pieces[4])

        relative_x = get_relative_coord(transf_x, min_transf_x, max_transf_x)
        relative_y = get_relative_coord(transf_y, min_transf_y, max_transf_y)

        #if(transf_x > 3500 and valid_room(roomName)):

        rooms[roomName] = (relative_x, relative_y)



    doc.unlink()



rooms = map_rooms('Cardwell Hall Floor 1.svg')

#clean_svg('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')