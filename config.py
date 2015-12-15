# These values control the probaability of adding various punctuation while encrypting a file, as percentages.
com = 0.08 # commas
per = 0.08 # periods, questionmarks, and exclamation points

punc = ['?!.', [2, 1, 10]] # probability distribution for ?, ! and . as integers. If you want to add another sentence ending puntuation mark, place it in the string and add a corresponding integer to the array.

# this is the default dictionary for conversion
defaultdict = 'wordsEn.txt'

# set wether or not to show debug messages
debug = True

# set the default output filename
output = 'out.txt'

# set wether or not to allow overwriting files
overwrite = False
