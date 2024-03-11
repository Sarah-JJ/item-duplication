EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.2,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.25,
    },
    {
        'name': 'work_type_id',
        'weight': 0.1,
    },
    {
        'name': 'qty',
        'weight': 0.1,
    },
    {
        'name': 'total_amount',
        'weight': 0.1,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'contractor_name',
        'weight': 0.1,
        'levenshtein_threshold': 0.75
    },
    {
        'name': 'location',
        'weight': 0.05,
        'levenshtein_threshold': 0.75
    }
]

ATTACHMENTS_WEIGHT = 0.1
