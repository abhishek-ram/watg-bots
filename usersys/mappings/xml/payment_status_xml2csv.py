import bots.transform as transform


def main(inn, out):

    # Get the original payment id from the original message Id
    original_message_id = inn.get(
         {'BOTSID': 'Document'},
         {'BOTSID': 'CstmrPmtStsRpt'},
         {'BOTSID': 'OrgnlGrpInfAndSts', 'OrgnlMsgId': None})
    original_payment_id = transform.persist_lookup(
        'message_lookup', original_message_id)

    out.put({'BOTSID': 'Group',
             'payment_identifier': original_payment_id or original_message_id})

    out.put({'BOTSID': 'Group',
             'transaction_count': inn.get(
                 {'BOTSID': 'Document'},
                 {'BOTSID': 'CstmrPmtStsRpt'},
                 {'BOTSID': 'OrgnlGrpInfAndSts', 'OrgnlNbOfTxs': None})
             })

    out.put({'BOTSID': 'Group', 'status': inn.get(
                {'BOTSID': 'Document'},
                {'BOTSID': 'CstmrPmtStsRpt'},
                {'BOTSID': 'OrgnlGrpInfAndSts', 'GrpSts': None}
            )})

    for pmt_inf in inn.getloop({'BOTSID': 'Document'},
                               {'BOTSID': 'CstmrPmtStsRpt'},
                               {'BOTSID': 'OrgnlPmtInfAndSts'}):

        for txn_inf in pmt_inf.getloop({'BOTSID': 'OrgnlPmtInfAndSts'},
                                       {'BOTSID': 'TxInfAndSts'}):

            transaction = out.putloop({'BOTSID': 'Group'},
                                      {'BOTSID': 'Transaction'})

            transaction.put({
                'BOTSID': 'Transaction',
                'endtoend_identifier': txn_inf.get({'BOTSID': 'TxInfAndSts',
                                                    'OrgnlEndToEndId': None})
            })

            transaction.put({
                'BOTSID': 'Transaction',
                'status_identifier': txn_inf.get({'BOTSID': 'TxInfAndSts',
                                                  'StsId': None})
            })

            transaction.put({
                'BOTSID': 'Transaction',
                'status': txn_inf.get({'BOTSID': 'TxInfAndSts', 'TxSts': None})
            })
