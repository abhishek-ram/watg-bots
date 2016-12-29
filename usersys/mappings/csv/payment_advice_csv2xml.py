import bots.transform as transform
import datetime
from decimal import Decimal, ROUND_HALF_UP


def main(inn, out):
    header_written = False
    pmt_inf = None
    e2e_id, cdt_info, cur = None, None, None
    for lin in inn.getloop({'BOTSID': 'PMT'}):
        if not header_written:
            # Set the botskey to the payment identifier
            doc_num = lin.get({'BOTSID': 'PMT', 'payment_identifier': None})
            inn.ta_info['botskey'] = out.ta_info['botskey'] = doc_num

            # Write the output document header
            out.put({'BOTSID': 'Document',
                     'Document__xmlns':
                         'urn:iso:std:iso:20022:tech:xsd:pain.001.001.03'})

            out.put({'BOTSID': 'Document',
                     'Document__xmlns:xsi':
                         'http://www.w3.org/2001/XMLSchema-instance'})

            out.put({'BOTSID': 'Document'},
                    {'BOTSID': 'CstmrCdtTrfInitn'},
                    {'BOTSID': 'GrpHdr',
                     'MsgId': 'MG%s' % transform.unique('Message Number')})

            out.put({'BOTSID': 'Document'},
                    {'BOTSID': 'CstmrCdtTrfInitn'},
                    {'BOTSID': 'GrpHdr',
                     'CreDtTm': datetime.datetime.now().strftime(
                         '%Y-%m-%dT%H:%M:%S')})

            out.put({'BOTSID': 'Document'},
                    {'BOTSID': 'CstmrCdtTrfInitn'},
                    {'BOTSID': 'GrpHdr'},
                    {'BOTSID': 'Authstn',
                     'Cd': lin.get({'BOTSID': 'PMT',
                                    'authorization_code': None})})

            out.put({'BOTSID': 'Document'},
                    {'BOTSID': 'CstmrCdtTrfInitn'},
                    {'BOTSID': 'GrpHdr'},
                    {'BOTSID': 'InitgPty'},
                    {'BOTSID': 'Id'},
                    {'BOTSID': 'OrgId'},
                    {'BOTSID': 'Othr',
                     'Id': lin.get({'BOTSID': 'PMT',
                                    'hsbc_connect_id': None})})

            # write the payment information header
            pmt_inf = out.putloop({'BOTSID': 'Document'},
                                  {'BOTSID': 'CstmrCdtTrfInitn'},
                                  {'BOTSID': 'PmtInf'})

            pmt_inf.put({'BOTSID': 'PmtInf', 'PmtInfId': doc_num})

            pmt_inf.put({'BOTSID': 'PmtInf',
                         'PmtMtd': lin.get({'BOTSID': 'PMT',
                                            'payment_method': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'PmtTpInf'},
                        {'BOTSID': 'SvcLvl',
                         'Cd': lin.get({'BOTSID': 'PMT',
                                        'payment_type': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'PmtTpInf'},
                        {'BOTSID': 'LclInstrm',
                         'Cd': lin.get({'BOTSID': 'PMT',
                                        'payment_purpose': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'ReqdExctnDt',
                         'BOTSCONTENT':
                             lin.get({'BOTSID': 'PMT',
                                      'requested_execution_date': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr',
                         'Nm': lin.get({'BOTSID': 'PMT',
                                        'debtor_name': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'Id'},
                        {'BOTSID': 'OrgId'},
                        {'BOTSID': 'Othr',
                         'Id': lin.get({'BOTSID': 'PMT',
                                        'debtor_id': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'PstlAdr',
                         'StrtNm': lin.get({'BOTSID': 'PMT',
                                            'debtor_address_street': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'PstlAdr',
                         'BldgNb': lin.get({'BOTSID': 'PMT',
                                            'debtor_address_building': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'PstlAdr',
                         'TwnNm': lin.get({'BOTSID': 'PMT',
                                           'debtor_address_city': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'PstlAdr',
                         'CtrySubDvsn': lin.get({'BOTSID': 'PMT',
                                                 'debtor_address_state': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'PstlAdr',
                         'PstCd': lin.get({'BOTSID': 'PMT',
                                           'debtor_address_postal_code': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'Dbtr'},
                        {'BOTSID': 'PstlAdr',
                         'Ctry': lin.get({'BOTSID': 'PMT',
                                          'debtor_address_country': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'DbtrAcct'},
                        {'BOTSID': 'Id',
                         'IBAN': lin.get({'BOTSID': 'PMT',
                                          'debtor_iban': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'DbtrAcct'},
                        {'BOTSID': 'Id'},
                        {'BOTSID': 'Othr',
                         'Id': lin.get({'BOTSID': 'PMT',
                                        'debtor_domestic_accntnbr': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'DbtrAgt'},
                        {'BOTSID': 'FinInstnId',
                         'BIC': lin.get({'BOTSID': 'PMT',
                                         'debtor_agent_bic': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'DbtrAgt'},
                        {'BOTSID': 'FinInstnId'},
                        {'BOTSID': 'ClrSysMmbId',
                         'MmbId': lin.get({'BOTSID': 'PMT',
                                           'debtor_agent_domestic_id': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'DbtrAgt'},
                        {'BOTSID': 'FinInstnId'},
                        {'BOTSID': 'PstlAdr',
                         'Ctry': lin.get({'BOTSID': 'PMT',
                                          'debtor_agent_country': None})})

            pmt_inf.put({'BOTSID': 'PmtInf'},
                        {'BOTSID': 'ChrgBr',
                         'BOTSCONTENT': lin.get({'BOTSID': 'PMT',
                                                 'charge_bearer': None})})
            header_written = True

        # Create a credit transfer information block for each line
        this_e2e_id = lin.get({'BOTSID': 'PMT', 'endtoend_identifier': None})
        # Create a new block only if this is the first line
        # for the credit transfer
        if e2e_id != this_e2e_id:
            cdt_info = pmt_inf.putloop({'BOTSID': 'PmtInf'},
                                       {'BOTSID': 'CdtTrfTxInf'})
            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'PmtId',
                          'InstrId': this_e2e_id,
                          'EndToEndId': this_e2e_id})
            rounded_amt = Decimal(
                lin.getdecimal({'BOTSID': 'PMT', 'payment_amount': None}).quantize(
                    Decimal('.01'), rounding=ROUND_HALF_UP))

            cur = lin.get({'BOTSID': 'PMT', 'payment_currency': None})
            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Amt',
                          'InstdAmt': rounded_amt,
                          'InstdAmt__Ccy': cur})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'ChqInstr',
                          'ChqNb': lin.get({'BOTSID': 'PMT',
                                             'check_number': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'ChqInstr',
                          'FrmsCd': lin.get({'BOTSID': 'PMT',
                                             'check_book_code': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr',
                          'Nm': lin.get({'BOTSID': 'PMT',
                                         'creditor_name': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr'},
                         {'BOTSID': 'PstlAdr',
                          'StrtNm': lin.get({'BOTSID': 'PMT',
                                             'creditor_address_street': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr'},
                         {'BOTSID': 'PstlAdr',
                          'BldgNb': lin.get({'BOTSID': 'PMT',
                                             'creditor_address_building': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr'},
                         {'BOTSID': 'PstlAdr',
                          'TwnNm': lin.get({'BOTSID': 'PMT',
                                            'creditor_address_city': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr'},
                         {'BOTSID': 'PstlAdr',
                          'CtrySubDvsn': lin.get({'BOTSID': 'PMT',
                                                  'creditor_address_state': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr'},
                         {'BOTSID': 'PstlAdr',
                          'PstCd': lin.get({'BOTSID': 'PMT',
                                            'creditor_address_postal_code': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Cdtr'},
                         {'BOTSID': 'PstlAdr',
                          'Ctry': lin.get({'BOTSID': 'PMT',
                                           'creditor_address_country': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'CdtrAcct'},
                         {'BOTSID': 'Id',
                          'IBAN': lin.get({'BOTSID': 'PMT',
                                           'creditor_iban': None})})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'CdtrAcct'},
                         {'BOTSID': 'Id'},
                         {'BOTSID': 'Othr',
                          'Id': lin.get({'BOTSID': 'PMT',
                                         'creditor_domestic_accntnbr': None})})

            creditor_agent_bic = lin.get({'BOTSID': 'PMT',
                                          'creditor_agent_bic': None})
            creditor_agent_did = lin.get({'BOTSID': 'PMT',
                                          'creditor_agent_domestic_id': None})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'CdtrAgt'},
                         {'BOTSID': 'FinInstnId',
                          'BIC': creditor_agent_bic})

            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'CdtrAgt'},
                         {'BOTSID': 'FinInstnId'},
                         {'BOTSID': 'ClrSysMmbId',
                          'MmbId': creditor_agent_did})

            if creditor_agent_did or creditor_agent_bic:
                cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                             {'BOTSID': 'CdtrAgt'},
                             {'BOTSID': 'FinInstnId'},
                             {'BOTSID': 'PstlAdr',
                              'Ctry': lin.get({'BOTSID': 'PMT',
                                               'creditor_agent_country': None})})

            # Map the transaction level payment purpose
            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'Purp',
                          'Cd': lin.get({'BOTSID': 'PMT',
                                         'payment_purpose2': None})})

            remittance_recipients = lin.get(
                {'BOTSID': 'PMT', 'remittance_recipients': None}) or ''

            for recipient in remittance_recipients.split('|'):
                if recipient:
                    cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                                 {'BOTSID': 'RltdRmtInf',
                                  'RmtLctnMtd': 'EMAL',
                                  'RmtLctnElctrncAdr': recipient})

            # Map the unstructured remittance information
            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'RmtInf',
                          'Ustrd': lin.get({'BOTSID': 'PMT', 'remittance_unstructured': None})})

            rmt_inv_num = lin.get(
                {'BOTSID': 'PMT', 'remittance_invoice_num': None})
            if rmt_inv_num:
                rmt_info = cdt_info.putloop({'BOTSID': 'CdtTrfTxInf'},
                                            {'BOTSID': 'RmtInf'},
                                            {'BOTSID': 'Strd'})
                rmt_info.put({'BOTSID': 'Strd'},
                             {'BOTSID': 'RfrdDocInf',
                              'Nb': rmt_inv_num})
                rmt_info.put({'BOTSID': 'Strd'},
                             {'BOTSID': 'RfrdDocInf',
                              'RltdDt': lin.get({'BOTSID': 'PMT',
                                                 'remittance_invoice_date': None})})

                rounded_amt = Decimal(
                    lin.getdecimal(
                        {'BOTSID': 'PMT',
                         'remittance_invoice_amount': None}).quantize(
                        Decimal('.01'), rounding=ROUND_HALF_UP))

                rmt_info.put({'BOTSID': 'Strd'},
                             {'BOTSID': 'RfrdDocAmt',
                              'DuePyblAmt__Ccy': cur,
                              'DuePyblAmt': rounded_amt})
                rmt_info.put({'BOTSID': 'Strd',
                              'AddtlRmtInf': lin.get({'BOTSID': 'PMT',
                                                      'remittance_invoice_reference': None})})

            e2e_id = this_e2e_id
        # For all subsequent lines write only the remittance information
        else:
            # Map the unstructured remittance information
            cdt_info.put({'BOTSID': 'CdtTrfTxInf'},
                         {'BOTSID': 'RmtInf',
                          'Ustrd': lin.get({'BOTSID': 'PMT', 'remittance_unstructured': None})})

            # Map the structured remittance information
            rmt_inv_num = lin.get(
                {'BOTSID': 'PMT', 'remittance_invoice_num': None})
            if rmt_inv_num:
                rmt_info = cdt_info.putloop({'BOTSID': 'CdtTrfTxInf'},
                                            {'BOTSID': 'RmtInf'},
                                            {'BOTSID': 'Strd'})
                rmt_info.put({'BOTSID': 'Strd'},
                             {'BOTSID': 'RfrdDocInf',
                              'Nb': rmt_inv_num})
                rmt_info.put({'BOTSID': 'Strd'},
                             {'BOTSID': 'RfrdDocInf',
                              'RltdDt': lin.get({'BOTSID': 'PMT',
                                                 'remittance_invoice_date': None})})

                rounded_amt = Decimal(
                    lin.getdecimal(
                        {'BOTSID': 'PMT',
                         'remittance_invoice_amount': None}).quantize(
                        Decimal('.01'), rounding=ROUND_HALF_UP))

                rmt_info.put({'BOTSID': 'Strd'},
                             {'BOTSID': 'RfrdDocAmt',
                              'DuePyblAmt__Ccy': cur,
                              'DuePyblAmt': rounded_amt})
                rmt_info.put({'BOTSID': 'Strd',
                              'AddtlRmtInf': lin.get({'BOTSID': 'PMT',
                                                      'remittance_invoice_reference': None})})

    out.put({'BOTSID': 'Document'},
            {'BOTSID': 'CstmrCdtTrfInitn'},
            {'BOTSID': 'GrpHdr'},
            {'BOTSID': 'NbOfTxs',
             'BOTSCONTENT':
                 pmt_inf.getcountoccurrences({'BOTSID': 'PmtInf'},
                                             {'BOTSID': 'CdtTrfTxInf'})})