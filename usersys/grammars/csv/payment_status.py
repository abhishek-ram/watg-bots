from bots.botsconfig import *

syntax = {
    'noBOTSID': True,
    'field_sep': ',',
    'quote_char': '"',
    'merge': False
}

structure = [
    {ID: 'Group', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'Transaction', MIN: 0, MAX: 99999}
    ]}
]

recorddefs = {
    'Group': [
        ['BOTSID', 'M', 256, 'A'],
        ['payment_identifier', 'M', 256, 'AN'],
        ['transaction_count', 'M', 256, 'AN'],
        ['status', 'C', 256, 'AN'],
    ],
    'Transaction': [
        ['BOTSID', 'M', 256, 'A'],
        ['endtoend_identifier', 'M', 256, 'AN'],
        ['status_identifier', 'M', 256, 'AN'],
        ['status', 'M', 256, 'AN'],
        ['additional_status_code', 'C', 256, 'AN'],
        ['additional_status_text', 'C', 256, 'AN'],
    ]
}

