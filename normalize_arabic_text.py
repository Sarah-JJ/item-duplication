
def normalize_arabic_text(text):

    characters = [
        ['آ', 'ا'],
        ['أ', 'ا'],
        ['إ', 'ا'],
        ['ء', 'ا'],
        ['ه', 'ة'],
        ['ئ', 'ي'],
        ['ؤ', 'و']
    ]

    for char in characters:
        replace_char = char[0]
        replace_with = char[1]

        text = text.replace(replace_char, replace_with)

    return text
