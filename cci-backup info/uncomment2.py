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
    comment.parentNode.replaceChild(node, comment)
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

#doc = minidom.parse("xmlfile.xml")
# print "000"
for element in doc.getElementsByTagName('Attribute'):
    # print "111"
    print element.childNodes

    # if element.getAttribute('Name') in ['SpanDepth', 'StripeSize']:
    #     print "222"
    #     print element[0]

print comment.toxml()
uncomment_node(comment)
print 'uncomment_node():\n'
print doc.toxml()