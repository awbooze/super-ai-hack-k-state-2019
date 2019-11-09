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
Finds the rooms and coordinates (for now) of all text in SVG aka rooms...
'''
def find_rooms_and_coords(svg):
    doc = minidom.parse(svg)  # parseString also exists
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

#find_rooms_and_coords('Durland-Rathbone-Fiedler-Engineering Hall-Floor3.svg')
clean_svg('Durland-Rathbone-Fiedler-Engineering Hall-Floor1.svg')

print("it worked")
