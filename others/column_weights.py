EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.2,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.25,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'others_name',
        'weight': 0.2,
        'levenshtein_threshold': 0.7
    },
    {
        'name': 'description_of_case',
        'weight': 0.2,
        'levenshtein_threshold': 0.6
    },
    {
        'name': 'amount',
        'weight': 0.05,
        'levenshtein_threshold': 0.8
    },
]

ATTACHMENTS_WEIGHT = 0.1
