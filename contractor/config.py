PATH = 'D:\work\Sana\drda\odoodb'
print_separator = '\n------------------------------------------------------------------------------------\n\n'
FILTER_DATE = '2024-02-15'
COMPARE_WITH_RECORDS_CREATED_DAYS_BEFORE = 1
COMPARE_WITH_RECORDS_CREATED_DAYS_AFTER = 1
NORMALIZE_ARABIC_COLS = ['contractor_name', 'location']
COMPARE_WITH_LEVENSHTEIN = True
SIMILARITY_THRESHOLD = 0.05

SIMILARITY_LEVELS = {
    'high': 0.7,
    'mod': 0.4,
    'low': 0.1,
}
