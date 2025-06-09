def accept_condition(password):
    vowels = 'aeiou'
    has_vowel = False
    vowel_cnt = 0           # 모음 갯수
    consonant_cnt = 0       # 자음 갯수

    prev_char = '' 

    for i, ch in enumerate(password):
        if ch in vowels:
            has_vowel = True
            vowel_cnt += 1
            consonant_cnt = 0
        
        else:
            consonant_cnt += 1
            vowel_cnt = 0

        if vowel_cnt >= 3 or consonant_cnt >= 3:
            return False
        
        if i >= 1 and ch == prev_char:
            if ch not in ['e', 'o']:
                return False
        
        prev_char = ch
    
    return has_vowel



while True:
    password = str(input())
    
    if password == 'end':
        break

    if accept_condition(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
