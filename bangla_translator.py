banglaDictionary = {
    "we": "aamra",
    "come": "aao",
    "in": "o",
    "peace": "santi",
    "hello": "salam",
    "can": "farmu",
    "i": "ami",
    "borrow": "khorjo",
    "some": "toora",
    "rocket": "rocket",
    "fuel": "tel",
    "please": "fliz",
    "don't": "na",
    "shoot": "mar",
    "welcome": "salam",
    "our": "amrar",
    "new": "noya",
    "alien": "naga",
    "overlords": "baf"}
englishPhrase = input("Please enter an english word or phrase to translate.")
englishWords = englishPhrase.lower().split()
alienWords = []
for word in englishWords:
    if word.lower() in banglaDictionary:
        alienWords.append(banglaDictionary[word])
    else:
        alienWords.append(word)
print("In bangla, say:", " ".join(banglaWords))