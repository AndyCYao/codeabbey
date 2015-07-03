'''key words in the dictionarys include

Direction words: north, south, east, west, down, up, left, right, back
Verbs: go, stop, kill, eat
Stop words: the, in, of, from, at, it
Nouns: door, bear, princess, cabinet
Numbers: any string of 0 through 9 characters

'''


# Andy's Version of Scan - im renaming this to scan obsolete for now

def scan_obsolete(phrase):
    '''Now you are ready to write your scanner.
    This scanner will take a string of raw input from a user
    and return a sentence that's composed of a list of tuples
    with the (TOKEN, WORD) pairings. If a word isn't part of
    the lexicon then it should still return the WORD
    but set the TOKEN to an error token.
    These error tokens will tell users they messed up
    '''

    # x = int(phrase)
    words = phrase.split()

    directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
    verbs = ["go", "stop", "kill", "eat"]
    stops = ["the", "in", "of", "from", "at", "it"]
    nouns = ["door", "bear", "princess", "cabinet"]
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sentence = []
    for i in range(len(words)):
        # print(words)
        clean_word = convert_number(words[i])
        if clean_word in directions:
            tup = ('direction', clean_word)
        elif clean_word in verbs:
            tup = ('verb', clean_word)
        elif clean_word in stops:
            tup = ('stop', clean_word)
        elif clean_word in nouns:
            tup = ('noun', clean_word)
        elif clean_word == "IsNum":
            tup = ('number', int(words[i]))
        else:
            tup = ('error', clean_word)
        sentence.append(tup)
    return(sentence)


def convert_number(s):
    try:
        int(s)
        return "IsNum"
    except Exception:
        return s

# print(scan("bear IAS princess"))
# end of line.

WORD_TYPES = {
    'verb': ['go', 'kill', 'eat'],
    'direction': ['north', 'south', 'east', 'west'],
    'noun': ['bear', 'princess'],
    'stop': ['the', 'in', 'of']
}

# invert the dictionary - need to look up how this is done.
VOCABULARY = {word: word_type for word_type, words in WORD_TYPES.items() for word in words}


def scan(sentence):
    '''this is the version of scan that uses dictionary correctly
    and is taken from this link http://codereview.stackexchange.com/questions/14238/lpthw-exercise-48-please-tear-this-to-pieces'''
    tokens = []
    for word in sentence.split():
        try:
            word_type = VOCABULARY[word]
        except KeyError:
            try:
                value = int(word)
            except:
                tokens.append(('error', word))
            else:
                tokens.append(('number', value))
        else:
            tokens.append((word_type, word))
    return tokens
