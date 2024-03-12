EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.15,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.2,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'from_location',
        'weight': 0.3,
        'levenshtein_threshold': 0.6
    },
    {
        'name': 'to_location',
        'weight': 0.3,
        'levenshtein_threshold': 0.6
    },
    {
        'name': 'person_name',
        'weight': 0.05,
        'levenshtein_threshold': 0.6
    },
]

ATTACHMENTS_WEIGHT = 0.05
