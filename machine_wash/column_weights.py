EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.2,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.2,
    },
    {
        'name': 'wash_date',
        'weight': 0.4,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'machine_wash_tag',
        'weight': 0.1,
        'levenshtein_threshold': 1
    },
    {
        'name': 'machine_location',
        'weight': 0.1,
        'levenshtein_threshold': 0.6
    }
]

ATTACHMENTS_WEIGHT = 0