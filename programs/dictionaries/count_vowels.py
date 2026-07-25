text=input("enter the sentence: ")
vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
        }
for ch in text:
    if ch in vowels:
        vowels[ch]+=1
print(vowels)