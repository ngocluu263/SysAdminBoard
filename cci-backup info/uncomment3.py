from xml.dom import minidom
import xml.etree.ElementTree as ET

tree = ET.parse('xmlfile.xml')
root = tree.getroot()
for e in root.iter('tag_name'):
    e.text = "something else" # This works

xml = """\
<SystemConfiguration Model="PowerEdge R430" ServiceTag="3SYYT52" TimeStamp="Wed Sep  6 18:14:47 2017">
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
</SystemConfiguration>
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

# doc = minidom.parse("xmlfile.xml").documentElement
# print "000"
# for element in doc.getElementsByTagName('Component'):
#     print len(element.childNodes)
#     print "111"
#     for i in range(0, len(element.childNodes)):
#         nodes = element.childNodes[i].toxml()
#         # uncomment_node(nodes)
#         print nodes
#         # uncomment_node(nodes)

