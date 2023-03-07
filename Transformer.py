from lxml import etree

# Cargar archivo XML de entrada
input_xml = etree.parse("BNB_CF_Project_Output.xml")

# Cargar archivo XSLT de transformación
transform = etree.XSLT(etree.parse("BNB_Classes_Report_Cleaner.xslt"))

# Aplicar la transformación al archivo XML
output_xml = transform(input_xml)

# Escribir el resultado de la transformación en un archivo de salida
with open("resultado.xslt", "wb") as f:
    print(output_xml)
    save(output_xml)