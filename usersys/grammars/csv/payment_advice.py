from bots.botsconfig import *

syntax = { 
        #'charset'                  : 'uft-8', #character set is utf-8
    'noBOTSID'                 : True,
    #'skip_firstline'           : 1,
    'field_sep'                : ',',
    'quote_char'               : '"'
}

structure = [        
    {ID:'PMT',MIN:1,MAX:9999}
]
        

nextmessageblock = ({'BOTSID':'PMT','payment_identifier':None}) 

recorddefs = {
    'PMT':[
        ['BOTSID','M',3,'A'],
        ['hsbc_connect_id', 'M', 256, 'AN'],
        ['authorization_code', 'C', 256, 'AN'],
        ['payment_identifier', 'M', 256, 'AN'],
        ['endtoend_identifier', 'M', 256, 'AN'],
        ['payment_method', 'C', 256, 'AN'],
        ['payment_type', 'C', 256, 'AN'],
        ['payment_purpose', 'C', 256, 'AN'],
        ['requested_execution_date', 'C', 256, 'AN'],
        ['debtor_name', 'C', 256, 'AN'],
        ['debtor_id', 'C', 256, 'AN'],
        ['debtor_address_street', 'C', 256, 'AN'],
        ['debtor_address_building', 'C', 256, 'AN'],
        ['debtor_address_city', 'C', 256, 'AN'],
        ['debtor_address_state', 'C', 256, 'AN'],
        ['debtor_address_postal_code', 'C', 256, 'AN'],
        ['debtor_address_country', 'C', 256, 'AN'],
        ['debtor_iban', 'C', 256, 'AN'],
        ['debtor_domestic_accntnbr', 'C', 256, 'AN'],
        ['debtor_agent_bic', 'C', 256, 'AN'],
        ['debtor_agent_domestic_id', 'C', 256, 'AN'],
        ['debtor_agent_country', 'C', 256, 'AN'],
        ['creditor_name', 'C', 256, 'AN'],
        ['creditor_id', 'C', 256, 'AN'],
        ['creditor_address_street', 'C', 256, 'AN'],
        ['creditor_address_building', 'C', 256, 'AN'],
        ['creditor_address_city', 'C', 256, 'AN'],
        ['creditor_address_state', 'C', 256, 'AN'],
        ['creditor_address_postal_code', 'C', 256, 'AN'],
        ['creditor_address_country', 'C', 256, 'AN'],
        ['creditor_iban', 'C', 256, 'AN'],
        ['creditor_domestic_accntnbr', 'C', 256, 'AN'],
        ['creditor_agent_country', 'C', 256, 'AN'],
        ['creditor_account_currency', 'C', 256, 'AN'],
        ['creditor_agent_bic', 'C', 256, 'AN'],
        ['creditor_agent_domestic_id', 'C', 256, 'AN'],
        ['charge_bearer', 'C', 256, 'AN'],
        ['payment_amount', 'C', 256, 'R'],
        ['payment_currency', 'C', 256, 'AN'],
        ['check_number', 'C', 256, 'AN'],
        ['check_book_code', 'C', 256, 'AN'],
        ['remittance_recipients', 'C', 256, 'AN'],
        ['remittance_invoice_num', 'C', 256, 'AN'],
        ['remittance_invoice_date', 'C', 256, 'AN'],
        ['remittance_invoice_amount', 'C', 256, 'AN'],
        ['remittance_invoice_reference', 'C', 256, 'AN'],
        ['payment_purpose2', 'C', 256, 'AN'],
        ['remittance_unstructured', 'C', 105, 'AN'],
    ]
}

