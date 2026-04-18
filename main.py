#Dictionary
translation = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ', 'f': '..-. ', 'g': '--. ', 'h': '.... ',
               'i': '.. ', 'j': '.--- ', 'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ', 'p': '.--. ',
               'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ', 'v': '...- ', 'w': '.-- ', 'x': '-..- ',
               'y': '-.-- ', 'z': '--.. ', '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ', '5': '..... ',
               '6': '-.... ', '7': '--... ', '8': '---.. ', '9': '----. ', '0': '----- ', '.': '.-.-.- ',
               ',': '--..-- ', ';': '-.-.-. ', ':': '---... ', '/': '-..-. ', ')': '-.--. ', '(': '-.--.- ',
               '!': '-.-.-- ', '?': '..--.. ', '_': '..--.- ', '"': '.-..-. ', "'": '.-..-. ', '&': '.-...  ',
               '-': '-....- ', '+': '.-.-. ', '=': '-...- ', '@': '.--.-. ', '$': '...-..- '}

#Userinput
#.lower() = Gross-, Kleinschreibung spielt keine Rolle
user_input = input("Please enter a sentence: ").lower()


#Userinput wird mit Dictionary abgeglichen

#zuerst leere Liste
result = ""

for letter in user_input:
    if letter in translation:
        result += translation[letter]
    elif letter == " ":
        result += "/ "
    else:
        print("Invalid character:", letter)

print(result)


#falls Leerzeichen nicht in Dictionary, wäre folgende Lösung richtig:
 #for letter in user_input:
    # if letter in translation:
    #     result += translation[letter] + " "
    # elif letter == " ":
    #     result += "/ "
    # else:
    #     print("Invalid character:", letter)
