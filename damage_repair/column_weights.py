EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.25,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.25,
    },
    {
        'name': 'repair_from_datetime',
        'weight': 0.5,
    },
    {
        'name': 'repair_to_datetime',
        'weight': 0.5,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'worker_repair_name',
        'weight': 0.15,
        'levenshtein_threshold': 0.7
    },
    {
        'name': 'repair_way',
        'weight': 0.15,
        'levenshtein_threshold': 0.6
    },
]

ATTACHMENTS_WEIGHT = 0.1
