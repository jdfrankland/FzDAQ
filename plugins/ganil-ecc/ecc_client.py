##################################################
# file: ecc_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/bin/wsdl2py -s ecc.wsdl
# 
##################################################

from ecc_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class eccLocator:
    ecc_address = "http://localhost:8061"
    def geteccAddress(self):
        return eccLocator.ecc_address
    def getecc(self, url=None, **kw):
        return eccSOAP(url or eccLocator.ecc_address, **kw)

# Methods
class eccSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: ServerExit
    def ServerExit(self, request, **kw):
        if isinstance(request, ServerExit) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="ServerExit", **kw)
        # no output wsaction
        response = self.binding.Receive(Response.typecode)
        return response

    # op: GetConfigIDs
    def GetConfigIDs(self, request, **kw):
        if isinstance(request, GetConfigIDs) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="GetConfigIDs", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Describe
    def Describe(self, request, **kw):
        if isinstance(request, Describe) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Describe", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Prepare
    def Prepare(self, request, **kw):
        if isinstance(request, Prepare) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Prepare", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Configure
    def Configure(self, request, **kw):
        if isinstance(request, Configure) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Configure", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Start
    def Start(self, request, **kw):
        if isinstance(request, Start) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Start", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Stop
    def Stop(self, request, **kw):
        if isinstance(request, Stop) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Stop", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Pause
    def Pause(self, request, **kw):
        if isinstance(request, Pause) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Pause", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Resume
    def Resume(self, request, **kw):
        if isinstance(request, Resume) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Resume", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Breakup
    def Breakup(self, request, **kw):
        if isinstance(request, Breakup) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Breakup", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: Undo
    def Undo(self, request, **kw):
        if isinstance(request, Undo) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Undo", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

    # op: GetState
    def GetState(self, request, **kw):
        if isinstance(request, GetState) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="GetState", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseState.typecode)
        return response

    # op: Special
    def Special(self, request, **kw):
        if isinstance(request, Special) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="Special", **kw)
        # no output wsaction
        response = self.binding.Receive(ResponseText.typecode)
        return response

ServerExit = GED("urn:ecc", "ServerExit").pyclass

Response = GED("urn:ecc", "Response").pyclass

GetConfigIDs = GED("urn:ecc", "GetConfigIDs").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Describe = GED("urn:ecc", "Describe").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Prepare = GED("urn:ecc", "Prepare").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Configure = GED("urn:ecc", "Configure").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Start = GED("urn:ecc", "Start").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Stop = GED("urn:ecc", "Stop").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Pause = GED("urn:ecc", "Pause").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Resume = GED("urn:ecc", "Resume").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Breakup = GED("urn:ecc", "Breakup").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

Undo = GED("urn:ecc", "Undo").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass

GetState = GED("urn:ecc", "GetState").pyclass

ResponseState = GED("urn:ecc", "ResponseState").pyclass

Special = GED("urn:ecc", "Special").pyclass

ResponseText = GED("urn:ecc", "ResponseText").pyclass
