def check_lang(text):
    en_alphabet = ''.join([chr(i) for i in range (ord('a'), ord('z') + 1)])
    ru_alphabet = ''.join([chr(i) for i in range (ord('а'), ord('я') + 1)])
    if text[0].lower() in en_alphabet: return en_alphabet
    if text[0].lower() in ru_alphabet: return ru_alphabet


txt = "my name is Python!"
code = txt.split()
alphabet = check_lang(txt)

count = 0
shift = []
for i in txt.split():
    count = 0
    for c in i:
        if c.isalpha(): count += 1
    shift.append(count)

for i in range (0, len(code)):
    solution = ""
    for char in code[i]:
        if not char.isalpha():
            solution += char
            continue
        shift_this_shit = (alphabet.find(char.lower()) + shift[i]) % len(alphabet)
        if char.isupper(): 
            solution += alphabet[shift_this_shit].upper()
        else:
            solution += alphabet[shift_this_shit]
    code[i] = solution
print(*code)