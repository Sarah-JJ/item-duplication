CHECK_FOR_EQUALITY_COLS = [
    {
        'name': 'project_id',
        'contribution': 0.2,
    },
    {
        'name': 'date_of_expenses',
        'contribution': 0.25,
    },
    {
        'name': 'work_type_id',
        'contribution': 0.1,
    },
    {
        'name': 'qty',
        'contribution': 0.1,
    },
    {
        'name': 'total_amount',
        'contribution': 0.1,
    }
]

TEXT_COLS = [
    {
        'name': 'contractor_name',
        'contribution': 0.1,
        'levenshtein_threshold': 0.75
    },
    {
        'name': 'location',
        'contribution': 0.05,
        'levenshtein_threshold': 0.75
    }
]

ATTACHMENTS_WEIGHT = 0.1
