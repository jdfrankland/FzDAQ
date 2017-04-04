##################################################
# file: ecc_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      /usr/bin/wsdl2py -s ecc.wsdl
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from ecc_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
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


# Service Skeletons
class ecc(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_ServerExit(self, ps, **kw):
        request = ps.Parse(ServerExit.typecode)
        return request,Response()

    soapAction['ServerExit'] = 'soap_ServerExit'
    root[(ServerExit.typecode.nspname,ServerExit.typecode.pname)] = 'soap_ServerExit'

    def soap_GetConfigIDs(self, ps, **kw):
        request = ps.Parse(GetConfigIDs.typecode)
        return request,ResponseText()

    soapAction['GetConfigIDs'] = 'soap_GetConfigIDs'
    root[(GetConfigIDs.typecode.nspname,GetConfigIDs.typecode.pname)] = 'soap_GetConfigIDs'

    def soap_Describe(self, ps, **kw):
        request = ps.Parse(Describe.typecode)
        return request,ResponseText()

    soapAction['Describe'] = 'soap_Describe'
    root[(Describe.typecode.nspname,Describe.typecode.pname)] = 'soap_Describe'

    def soap_Prepare(self, ps, **kw):
        request = ps.Parse(Prepare.typecode)
        return request,ResponseText()

    soapAction['Prepare'] = 'soap_Prepare'
    root[(Prepare.typecode.nspname,Prepare.typecode.pname)] = 'soap_Prepare'

    def soap_Configure(self, ps, **kw):
        request = ps.Parse(Configure.typecode)
        return request,ResponseText()

    soapAction['Configure'] = 'soap_Configure'
    root[(Configure.typecode.nspname,Configure.typecode.pname)] = 'soap_Configure'

    def soap_Start(self, ps, **kw):
        request = ps.Parse(Start.typecode)
        return request,ResponseText()

    soapAction['Start'] = 'soap_Start'
    root[(Start.typecode.nspname,Start.typecode.pname)] = 'soap_Start'

    def soap_Stop(self, ps, **kw):
        request = ps.Parse(Stop.typecode)
        return request,ResponseText()

    soapAction['Stop'] = 'soap_Stop'
    root[(Stop.typecode.nspname,Stop.typecode.pname)] = 'soap_Stop'

    def soap_Pause(self, ps, **kw):
        request = ps.Parse(Pause.typecode)
        return request,ResponseText()

    soapAction['Pause'] = 'soap_Pause'
    root[(Pause.typecode.nspname,Pause.typecode.pname)] = 'soap_Pause'

    def soap_Resume(self, ps, **kw):
        request = ps.Parse(Resume.typecode)
        return request,ResponseText()

    soapAction['Resume'] = 'soap_Resume'
    root[(Resume.typecode.nspname,Resume.typecode.pname)] = 'soap_Resume'

    def soap_Breakup(self, ps, **kw):
        request = ps.Parse(Breakup.typecode)
        return request,ResponseText()

    soapAction['Breakup'] = 'soap_Breakup'
    root[(Breakup.typecode.nspname,Breakup.typecode.pname)] = 'soap_Breakup'

    def soap_Undo(self, ps, **kw):
        request = ps.Parse(Undo.typecode)
        return request,ResponseText()

    soapAction['Undo'] = 'soap_Undo'
    root[(Undo.typecode.nspname,Undo.typecode.pname)] = 'soap_Undo'

    def soap_GetState(self, ps, **kw):
        request = ps.Parse(GetState.typecode)
        return request,ResponseState()

    soapAction['GetState'] = 'soap_GetState'
    root[(GetState.typecode.nspname,GetState.typecode.pname)] = 'soap_GetState'

    def soap_Special(self, ps, **kw):
        request = ps.Parse(Special.typecode)
        return request,ResponseText()

    soapAction['Special'] = 'soap_Special'
    root[(Special.typecode.nspname,Special.typecode.pname)] = 'soap_Special'
