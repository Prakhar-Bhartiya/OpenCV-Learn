import http.client
import xml.dom.minidom

HOST = ""
API_URL = "https://api.infinit.co.in/upi/2.0/ReqBalEnq/{version}/urn:txnid:{transaction}"


def do_request(xml_location):
    """HTTP XML Post request"""
    request = open(xml_location, "r").read()

    webservice = http.client.HTTPConnection(HOST)
    webservice.putrequest("POST", API_URL)
    webservice.putheader("Host", HOST)
    webservice.putheader("User-Agent", "Python post")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(request))
    webservice.endheaders()
    1

    webservice.send(request)

    statuscode, statusmessage, header = webservice.getreply()

    result = webservice.getfile().read()
    resultxml = xml.dom.minidom.parseString(result)

    print(statuscode, statusmessage, header)
    print(resultxml.toprettyxml())

    with open("output-%s" % xml_location, "w") as xmlfile:
        xmlfile.write(resultxml.toprettyxml())

do_request("C:\\Users\\91740\\Desktop\\voc.xml.xml")
