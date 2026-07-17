def normalize_data(data):
    normalized_data = []
    for x in data:
        new_plural = ' '.join(x[2].split(' ')[:2]) if '#' in x[2] else x[2]
        if new_plural.startswith('-'):
            new_plural = '-'
        if new_plural in('(usually uncountable)', '(usually unCountable)', '(no plural form)', '(plural noun)'):
            new_plural = '-'
        if len(x[1].split(' '))>2: #Should be one case
            continue
        new_plural = new_plural.strip()
        new_line = [*x[0].split(' '), x[1], new_plural]
        normalized_data.append(new_line)
    return normalized_data

def purge_pure_duplicates(data):
    all_german_nouns = set()
    possible_plurals = []
    
    for x in data:
        if x[2] in all_german_nouns:
            continue
        all_german_nouns.add(x[2])
        possible_plurals.append(x)
    return possible_plurals