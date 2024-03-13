EQUALITY_COMPARISON_COLS = [
    {
        'name': 'project_id',
        'weight': 0.15,
    },
    {
        'name': 'date_of_expenses',
        'weight': 0.25,
    }
]

TEXT_COMPARISON_COLS = [
    {
        'name': 'material_from_location',
        'weight': 0.25,
        'levenshtein_threshold': 0.6
    },
    {
        'name': 'material_to_location',
        'weight': 0.25,
        'levenshtein_threshold': 0.6
    },
    {
        'name': 'transporter_name',
        'weight': 0.05,
        'levenshtein_threshold': 0.6
    },
    {
        'name': 'operator_name',
        'weight': 0.025,
        'levenshtein_threshold': 0.6
    },
]

ATTACHMENTS_WEIGHT = 0.025
