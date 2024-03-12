EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.05,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.1,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'equipment_type',
        'weight': 0.1,
        'levenshtein_threshold': 0.5
    },
    {
        'name': 'location',
        'weight': 0.1,
        'levenshtein_threshold': 0.5
    },
    {
        'name': 'rental_shop',
        'weight': 0.3,
        'levenshtein_threshold': 0.5
    },
    {
        'name': 'from_location',
        'weight': 0.1,
        'levenshtein_threshold': 0.5
    },
    {
        'name': 'to_location',
        'weight': 0.1,
        'levenshtein_threshold': 0.5
    }
]

ATTACHMENTS_WEIGHT = 0.15
