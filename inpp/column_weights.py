EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.2,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.4,
    },
    {
        'name': 'date_of_work',
        'weight': 0.1,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'responsible_contractor_name',
        'weight': 0.2,
        'levenshtein_threshold': 0.7
    },
    {
        'name': 'supervisor_name',
        'weight': 0.1,
        'levenshtein_threshold': 0.7
    }
]

ATTACHMENTS_WEIGHT = 0.1
