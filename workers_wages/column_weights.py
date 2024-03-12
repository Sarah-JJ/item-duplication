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
        'name': 'work_type_id',
        'weight': 0.02,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'worker_name',
        'weight': 0.4,
        'levenshtein_threshold': 0.75
    },
    {
        'name': 'wages_location',
        'weight': 0.05,
        'levenshtein_threshold': 0.75
    }
]

ATTACHMENTS_WEIGHT = 0.03
