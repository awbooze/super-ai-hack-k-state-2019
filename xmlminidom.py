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

def find_rooms_and_coords(svg):
    doc = minidom.parse(svg)  # parseString also exists
    path_strings = [path.getAttribute('id') for path in doc.getElementsByTagName('text')]
    textElements = doc.getElementsByTagName('text')

    for textElement in textElements:
        # get tspan element and get room number, and print it
        tspanElements = textElement.getElementsByTagName('tspan')
        for tspanElement in tspanElements:
            roomNumber = tspanElement.firstChild.nodeValue
            print('Room number: ' + roomNumber)

        # get transform attribute from text element
        transformElement = textElement.getAttribute('transform')
        #print(transformElement) # a string
        pieces = transformElement.split(",")
        print("x coord: " + pieces[4])
        print("y coord: " + pieces[5].replace(")", ""))

    doc.unlink()

find_rooms_and_coords('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')
clean_svg('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')