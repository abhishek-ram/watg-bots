import bots.transform as transform


def main(inn, out):
    out.put({'BOTSID': 'PST',
             'payment_identifier': inn.get(
                 {'BOTSID': 'Document'},
                 {'BOTSID': 'CstmrPmtStsRpt'},
                 {'BOTSID': 'OrgnlGrpInfAndSts', 'OrgnlMsgId': None})
             })

    out.put({'BOTSID': 'PST',
             'transaction_count': inn.get(
                 {'BOTSID': 'Document'},
                 {'BOTSID': 'CstmrPmtStsRpt'},
                 {'BOTSID': 'OrgnlGrpInfAndSts', 'OrgnlNbOfTxs': None})
             })

    out.put({'BOTSID': 'PST',
             'group_status': inn.get(
                 {'BOTSID': 'Document'},
                 {'BOTSID': 'CstmrPmtStsRpt'},
                 {'BOTSID': 'OrgnlGrpInfAndSts', 'GrpSts': None})
             })
