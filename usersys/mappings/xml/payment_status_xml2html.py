import bots.transform as transform


def main(inn, out):

    # Get the original payment id from the original message Id
    original_message_id = inn.get(
         {'BOTSID': 'Document'},
         {'BOTSID': 'CstmrPmtStsRpt'},
         {'BOTSID': 'OrgnlGrpInfAndSts', 'OrgnlMsgId': None})

    # transform.persist_add_update('message_lookup', 'MG12', 'USA65')
    # transform.persist_add_update('message_lookup', 'MG13', 'USA92')

    original_payment_id = transform.persist_lookup(
        'message_lookup', original_message_id)

    group_status = inn.get({'BOTSID': 'Document'},
                          {'BOTSID': 'CstmrPmtStsRpt'},
                          {'BOTSID': 'OrgnlGrpInfAndSts', 'GrpSts': None})
    out.data.header = {
        'payment_identifier': original_payment_id or original_message_id,
        'transaction_count': inn.get({'BOTSID': 'Document'},
                                     {'BOTSID': 'CstmrPmtStsRpt'},
                                     {'BOTSID': 'OrgnlGrpInfAndSts',
                                      'OrgnlNbOfTxs': None}),

        'status': transform.ccode('Payment Status', group_status, safe=True)
    }

    out.data.lines = []
    for pmt_inf in inn.getloop({'BOTSID': 'Document'},
                               {'BOTSID': 'CstmrPmtStsRpt'},
                               {'BOTSID': 'OrgnlPmtInfAndSts'}):

        for txn_inf in pmt_inf.getloop({'BOTSID': 'OrgnlPmtInfAndSts'},
                                       {'BOTSID': 'TxInfAndSts'}):

            status = txn_inf.get({'BOTSID': 'TxInfAndSts', 'TxSts': None})
            additional_status = txn_inf.get({'BOTSID': 'TxInfAndSts'},
                                            {'BOTSID': 'StsRsnInf'},
                                            {'BOTSID': 'Rsn', 'Cd': None})
            out.data.lines.append({
                'endtoend_identifier': txn_inf.get({'BOTSID': 'TxInfAndSts',
                                                    'OrgnlEndToEndId': None}),
                'status_identifier': txn_inf.get({'BOTSID': 'TxInfAndSts',
                                                  'StsId': None}),
                'status': transform.ccode('Payment Status', status),
                'additional_status_code': transform.ccode(
                    'Additional Payment Status', additional_status, safe=True),
                'additional_status_text': txn_inf.get({'BOTSID': 'TxInfAndSts'},
                                                      {'BOTSID': 'StsRsnInf',
                                                       'AddtlInf': None})
            })
