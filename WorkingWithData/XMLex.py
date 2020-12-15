import xml.dom.minidom
import random

doc = xml.dom.minidom.parse("books.xml")
elements = doc.documentElement
bookList = elements.getElementsByTagName("book")

for book in bookList:
    price = book.getElementsByTagName("price")[0].childNodes[0]
    price.nodeValue = int(random.random()*10*100)/100

with open("books2.xml", "w") as xml_file:
    doc.writexml(xml_file)