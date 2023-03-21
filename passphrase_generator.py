from niceware import wordlist
import nltk
import secrets

# nltk.download('averaged_perceptron_tagger') # uncomment this if the nltk.pos_tag(phrases) throws an error

tagged_phrases = nltk.pos_tag(wordlist.WORD_LIST)
nouns = []
adjectives = []
adverbs = []
verbs = []
sentence_formats = ['NVN','JNV','RVN','NVR','VJN','NRV']

for word_tuple in tagged_phrases:
    word = word_tuple[0]
    match word_tuple[1][0]:
        case 'V':
            verbs.append(word)
        case 'J':
            adjectives.append(word)
        case 'N':
            nouns.append(word)
        case 'R':
            adverbs.append(word)

structure = secrets.choice(sentence_formats)
tokens = []
for character in structure:
    match character:
        case 'N':
            word = secrets.choice(nouns)
            if word[0] in 'aeiou':
                article = secrets.choice(['an ','the ', ''])
            else:
                article = secrets.choice(['a ','the ', ''])
            tokens.append('{0}{1}'.format(article, word))
        case 'J':
            tokens.append(secrets.choice(adjectives))
        case 'R':
            tokens.append(secrets.choice(adverbs))
        case 'V':
            tokens.append(secrets.choice(verbs))

passphrase = '{0} {1} {2}'.format(tokens[0], tokens[1], tokens[2])

print(passphrase)

