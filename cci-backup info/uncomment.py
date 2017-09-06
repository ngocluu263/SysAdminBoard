from xml.dom import minidom

doc = minidom.parse("xmlfile.xml")
for element in doc.getElementsByTagName('MyElementName'):
    if element.getAttribute('name') in ['AttrName1', 'AttrName2']:
        parentNode = element.parentNode
        parentNode.insertBefore(doc.createComment(element.toxml()), element)
        parentNode.removeChild(element)
f = open("xmlfile.xml", "w")
f.write(doc.toxml())
print doc.toxml()
f.close()