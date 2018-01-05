import xml.dom.minidom as DOM
in_xml_file = r"<path>\<to>\<the>\portal_test_service.sddraft"
out_xml_file = r"<path>\<to>\<the>\portal_test_service_ForWeb.sddraft"

doc = DOM.parse(in_xml_file)
keys = doc.getElementsByTagName('Type')
key = keys[0]
key.firstChild.nodeValue = 'esriServiceDefinitionType_Replacement'

f = open(out_xml_file, 'w')
doc.writexml( f )
f.close()
