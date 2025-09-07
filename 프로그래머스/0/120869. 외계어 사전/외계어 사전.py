def solution(spell, dic):
    spell_set = set(spell)
    
    for item in dic:
        if set(item) == spell_set and len(item) == len(spell):
            return 1
    return 2
    