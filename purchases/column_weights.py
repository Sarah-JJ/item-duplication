EQUALITY_COMPARISON_COLS = [
    {
        'name': 'receipts_number',
        'weight': 0.4,
    },
    {
        'name': 'purchase_date',
        'weight': 0.15,
    },
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'seller_name',
        'weight': 0.25,
        'levenshtein_threshold': 0.75
    },
    {
        'name': 'phone_number_note',
        'weight': 0.1,
        'levenshtein_threshold': 0.65
    }
]

ATTACHMENTS_WEIGHT = 0.1
