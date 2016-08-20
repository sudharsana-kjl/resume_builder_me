import zipfile
import xml.etree.ElementTree as ET
import tempfile
import zipfile
import shutil
import os


def build(filename, name):
	shutil.copy("testfile.docx", filename + ".docx")
	full_file = filename + ".docx"
	z = zipfile.ZipFile(full_file)
	doc_xml = z.read('word/document.xml')
	tree = ET.fromstring(doc_xml)
	print ET.dump(tree)
	for node in list(tree.iter()):
		if "id" in node.attrib and node.attrib['id'] == "name":
			node.text = name
			break
	with


if __name__ == '__main__':
	build("test107113087", "Test name")
		