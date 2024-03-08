morse_dict = {
    'a': '* ***',
    'b': '*** * * *',
    'c': '*** * *** *',
    'd': '*** * *',
    'e': '*',
    'f': '* * *** *',
    'g': '*** *** *',
    'h': '* * * *',
    'i': '* *',
    'j': '* *** *** ***',
    'k': '*** * ***',
    'l': '* *** * *',
    'm': '*** ***',
    'n': '*** *',
    'o': '*** *** ***',
    'p': '* *** *** *',
    'q': '*** *** * ***',
    'r': '* *** *',
    's': '* * *',
    't': '***',
    'u': '* * ***',
    'v': '* * * ***',
    'w': '* *** ***',
    'x': '*** * * ***',
    'y': '*** * *** ***',
    'z': '*** *** * *',
}

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
morse_num_list = []
dot = '* '
line = '*** '
for i in range(0, 10):
    if i <= 5:
        mos_string = dot*i+line*(5-i)
        morse_num_list.append(mos_string.strip())
    else:
        morse_string = line*(i-5)+dot*i
        morse_num_list.append(morse_string.strip())

morse_num_dict = dict(zip(num_list, morse_num_list))

morse_dict.update(morse_num_dict)

print("Morse Code Translater")
mode = input("to Morse code: input 1, to original string: input 2\n")
if mode == '1':
    user_input = input("Input your string: ")
    if user_input.isalnum():
        result = ''
        for ch in user_input:
            if ch == ' ':
                result += '     '
            else:
                result += morse_dict.get(ch) + '   '
        print(f'Translation result: {result}')
    else:
        print("You can only use alphabets and numbers")
elif mode == '2':
    user_input = input("Input your Morse Code(with *, *** and whitespace: ")
    letters = user_input.split('   ')
    result = ''
    for letter in letters:
        if letter not in morse_dict.values():
            print("Wrong Morse Code. Try Again")
            break
        else:
            result += [k for k, v in morse_dict.items() if v == letter][0]
    print(f"Translation result: {result}")
else:
    print("Wrong input. Please choose between 1 and 2.")