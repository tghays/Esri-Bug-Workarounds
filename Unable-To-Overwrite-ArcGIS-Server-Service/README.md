This script is a workaround for overwriting a service in ArcGIS Server using Python.  The associated bug is NIM094951: "Error 001398: Service name already exists" when publishing a service definition file to a non-root folder on ArcGIS for Server using UploadServiceDefinition_server.



The error occurs between the _ForWeb sddraft creation and the sddraft analysis, prior to staging and publishing the sd file.  The "Type" XML tag in the _ForWeb.sddraft file contains "esriServiceDefinitionType_New", but should be "esriServiceDefinitionType_Replace" instead.

This script simply parses the XML finding the "Type" tag, and replaces it with the correct text.
