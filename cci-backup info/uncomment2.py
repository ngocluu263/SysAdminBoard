from xml.dom import minidom

xml = """\
<?xml version="1.0" ?>
<Component FQDD="Disk.Virtual.0:RAID.Integrated.1-1">
<Attribute Name="RAIDaction">CreateAuto</Attribute>
<Attribute Name="LockStatus">Unlocked</Attribute>
<Attribute Name="RAIDinitOperation">None</Attribute>
<!-- <Attribute Name="T10PIStatus">Disabled</Attribute> -->
<Attribute Name="DiskCachePolicy">Default</Attribute>
<Attribute Name="RAIDdefaultWritePolicy">WriteBack</Attribute>
<Attribute Name="RAIDdefaultReadPolicy">ReadAhead</Attribute>
<Attribute Name="Name">Virtual Disk 0</Attribute>
<Attribute Name="Size">107374182400</Attribute>
<Attribute Name="StripeSize">128</Attribute>
<!-- <Attribute Name="SpanDepth">1</Attribute> -->
<!-- <Attribute Name="SpanLength">2</Attribute> -->
<Attribute Name="RAIDTypes">RAID 1</Attribute>
<!-- <Attribute Name="IncludedPhysicalDiskID">Disk.Bay.0:Enclosure.Internal.0-1:RAID.Integrated.1-1</Attribute> -->
</Component>
"""

xml2 = """\
<target depends="create-build-dir" name="build-Folio">
   <property name="project.name" value="Folio"/>
   <ant antfile="build.xml" dir="Folio/FolioUI" inheritall="false" target="package"/>
   <ant antfile="build.xml" dir="Folio/Folio" inheritall="false" target="package"/>
</target>
"""


def comment_node(node):
    comment = node.ownerDocument.createComment(node.toxml())
    node.parentNode.replaceChild(comment, node)
    return comment


def uncomment_node(comment):
    node = minidom.parseString(comment.data).firstChild
    print comment.data
    print node.toxml()
    comment.parentNode.replaceChild(node, comment)
    print node.toxml()
    return node

# doc = minidom.parseString(xml).documentElement
#
# print doc.toxml()
#
# comment_node(doc.getElementsByTagName('Attribute')[-1])
#
# xml = doc.toxml()
#
# print 'comment_node():\n'
# print xml

doc = minidom.parseString(xml).documentElement
#print doc.toxml()
#comment = doc.lastChild.previousSibling
comment = doc.lastChild.previousSibling

# doc = minidom.parse("xmlfile.xml")
print "000"
for element in doc.getElementsByTagName('Component'):
    print len(element.childNodes)
    print "111"
    for i in range(0,len(element.childNodes)):
        nodes = element.childNodes[i]
        uncomment_node(nodes)
        print nodes
        # uncomment_node(nodes)
        # print doc.toxml()

    # if element.getAttribute('Name') in ['SpanDepth', 'StripeSize']:
    #     print "222"
    #     print element[0]


print comment.toxml()
uncomment_node(comment)
print 'uncomment_node():\n'
# print doc.toxml()


# xmldoc = minidom.parse('xmlfile.xml')
# root = xmldoc.getElementsByTagName('Component')
# for nodes in root:
#     for node in nodes.childNodes:
#         for x in node.childNodes:
#             print node.childNodes[0]