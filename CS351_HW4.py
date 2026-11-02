#CS351 Homework 4
#Group: Duru Birinci and Jack Quizhpi
#Our assumptions are that the input is uppercase and that the ties in the counts are broken by alphabetical order, and only A-Z is what gets substituted
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T','U','V','W','X','Y','Z']
eng_freq = ['E','T','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']

freq_map = {} # dictionary to contain letter frequencies in ciphertext
key_map = {} # dicionary to contain potential substitution key for ciphertext

for item in alphabet:
    freq_map[item] = 0 # initialize each letter into the dictionary with value 0.



def get_frequency(text): # Function gets the frequencies of every letter in the cipher text
    for i in range(len(alphabet)):
        freq_map[alphabet[i]] = text.count(alphabet[i]) 


def create_mapping(sorted_map, eng_freq): #creates initial key using common english letters as substitutions
    index = 0
    for item in sorted_map:
        key_map[item] = eng_freq[index]
        index = index + 1
    print(key_map)

def decrypt_text(key_map, ciphertext): # decrypts the text using submitted key and returns results
    decryption = ""
    for char in ciphertext:
        if char in key_map:
            decryption = decryption + key_map[char]
        else:
            decryption = decryption + char
    return(decryption)

def swap_letters(letter1, letter2): # swaps the resulting letter from two different keys
        temp = key_map[letter1]
        key_map[letter1] = key_map[letter2]
        key_map[letter2] = temp

def manual_replace(ciphertext): # lets the user fix letters by hand until they are done
    while True:
        choice = input("swap a letter? (y/n): ")
        if choice.lower() != 'y':
            break
        cipher_letter = input("cipher letter: ").upper()
        plain_letter = input("change it to: ").upper()
        if cipher_letter not in alphabet or plain_letter not in alphabet:
            print("just one letter A-Z")
            continue
        for key, value in key_map.items(): # find the cipher letter that currently decrypts to plain_letter
            if value == plain_letter:
                swap_letters(cipher_letter, key) # swap so two cipher letters never decrypt to the same letter
                break
        print(decrypt_text(key_map, ciphertext))

def display_mapping(map): #displays a map (used for key, or letter frequency)
    print("-"*15)
    print("Key -> Value")
    print("-"*15)

    if isinstance(map['A'], int):
        for key, value in map.items():
            print(f"{key:<3}-> {value}")
    else:
        for key, value in sorted(map.items()):
            print(f"{key:<3}-> {value}")




ciphertext = input("Input Ciphertext: ")
# ciphertext = "IEWL,  WL P LJDRJI KJLLPXJ ." #encrypted text (test input)


# For testing purposes, decrypted message is: THIS IS A SECRET MESSAGE
get_frequency(ciphertext)
sorted_map = dict(sorted(freq_map.items(), key=lambda item: item [1], reverse=True))
create_mapping(sorted_map, eng_freq)
# real_key = {'P': 'A', 'Q': 'B', 'D': 'C', 'V': 'D', 'J': 'E', 'T': 'F', 'X': 'G', 'E': 'H', 
#             'W': 'I', 'H': 'J', 'F': 'K', 'G': 'L', 'K': 'M', 'N': 'N', 'A': 'O', 'B': 'P', 
#            'U': 'Q', 'R': 'R', 'L': 'S', 'I': 'T', 'M': 'U', 'Y': 'V', 'Z': 'W', 'S': 'X', 
#             'O': 'Y', 'C': 'Z'}
display_mapping(sorted_map)
# display_mapping(real_key)
#print(decrypt_text(real_key, ciphertext))

print(decrypt_text(key_map, ciphertext)) # partial decryption from frequency analysis
manual_replace(ciphertext)
print("final message: " + decrypt_text(key_map, ciphertext))


