import subprocess, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
import requests, argparse
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])
from lxml import etree

#Define here the namespaces that your XML contains.
namespace = {
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'gml': 'http://www.opengis.net/gml'
}


#Parametrize the arguments using ArgParse
xml_or = argparse.ArgumentParser(description='This is a program to fill XML documents with GML coordinates')
xml_or.add_argument('--input_file', required=True, help='write --input_file followed with name of the XML.')
xml_or.add_argument('--input_url', required=True, help='write --input_url + the URL you want to grab de GML coordinates.')
xml_or.add_argument('--output_file', required=True, help='write --output_file followed with name of the output XML desired.')
arguments = xml_or.parse_args()



url = arguments.input_url


#Using etree to parse the XML doc and find what we want to replace.
tree = etree.parse(arguments.input_file)
posList = tree.xpath("//gml:posList[contains(text(), '-1 -1 -1 -1')]", namespaces=namespace)[0]
posList.text = requests.get(url).text.strip()
tree.write(arguments.output_file)
print('Your GMLs coordinates were successfully added to your new XML document.')

