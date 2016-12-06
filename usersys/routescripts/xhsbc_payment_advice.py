import bots.preprocess as preprocess
import bots.botslib as botslib
import bots.botsglobal as botsglobal
from bots.botsconfig import *
from lxml import objectify, etree


def preoutcommunication(routedict,*args,**kwargs):
    preprocess.postprocess(routedict, sort_xml)


def sort_xml(ta_from,endstatus,*args,**kwargs):
    try:
        # copy ta for postprocessing, open the files
        ta_to = ta_from.copyta(status=endstatus)
        infile = botslib.opendata(ta_from.filename,'r')
        tofile = botslib.opendata(str(ta_to.idta),'wb')

        inxml = objectify.fromstring(infile.read())

        # Fix the position of tags in the GrpHdr
        no_of_trans = inxml.CstmrCdtTrfInitn.GrpHdr.find(
            './{urn:iso:std:iso:20022:tech:xsd:pain.001.001.03}NbOfTxs')
        auth_stn = inxml.CstmrCdtTrfInitn.GrpHdr.find(
            './{urn:iso:std:iso:20022:tech:xsd:pain.001.001.03}Authstn')
        inxml.CstmrCdtTrfInitn.GrpHdr.remove(no_of_trans)
        inxml.CstmrCdtTrfInitn.GrpHdr.insert(
            inxml.CstmrCdtTrfInitn.GrpHdr.index(auth_stn) + 1, no_of_trans)

        # Fix the position of tags in the PmtInf
        req_exec_date = inxml.CstmrCdtTrfInitn.PmtInf.find(
            './{urn:iso:std:iso:20022:tech:xsd:pain.001.001.03}ReqdExctnDt')
        pmt_tp_inf = inxml.CstmrCdtTrfInitn.PmtInf.find(
            './{urn:iso:std:iso:20022:tech:xsd:pain.001.001.03}PmtTpInf')
        inxml.CstmrCdtTrfInitn.PmtInf.remove(req_exec_date)
        inxml.CstmrCdtTrfInitn.PmtInf.insert(
            inxml.CstmrCdtTrfInitn.PmtInf.index(pmt_tp_inf) + 1, req_exec_date)

        tofile.write(etree.tostring(
            inxml, pretty_print=True, xml_declaration=True, encoding='utf-8'))

        # close files and update outmessage transaction with ta_info
        infile.close()
        tofile.close()
        ta_to.update(statust=OK, filename=str(ta_to.idta))
    except:
        txt = botslib.txtexc()
        botsglobal.logger.error(
            u'split_lines postprocess failed. Error:\n%s' % txt)
        raise botslib.OutMessageError(
            u'split_lines postprocess failed. Error:\n%s' % txt)