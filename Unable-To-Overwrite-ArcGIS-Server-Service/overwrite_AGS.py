from xml.etree import ElementTree as et

xml_file = r"<path>\<to>\<the>\test_service_ForWeb.sddraft"
tree = et.parse(xml_file)

find = tree.find('Type').text = ('esriServiceDefinitionType_Replace')
tree.write(xml_file)