import subprocess

# !!!!!READ ME!!!!!
# !!!!!READ ME!!!!!
# !!!!!READ ME!!!!!
# This program will not work unless nltk is installed.
# The nltk module does a very nice job in separating the sentences properly.
# The preferred method to install nltk would be to do a pip install.
# Go to your python terminal and type in the command as follows:
# pip install nltk


# Once nltk is installed, just run the function with its correct filename.
# The correct filename for this program was 'Hounds.txt'


# If you do not know how to pip install, run the function install found in this script.
# Do this by removing the # in front of the install function
# The program is set up to install nltk and then run the counter function
# It should work upon running.
# Again, the preferred method of installation for nltk is by using the pip install terminal command,


# This function should work, at least it worked for me.
# This is just the back up installation function
def install(name):
    subprocess.call(['pip', 'install', name])
    import nltk.data
    nltk.download('punkt')


def da_counter(filename):
    # These are just the modules/downloads we need for nltk
    import nltk.data
    nltk.download('punkt')

    # Variables for keep tracking of the total number of sentences that are
    # positive, negative, and neutral
    fin_pos_counter = 0
    fin_neg_counter = 0
    fin_neutral_counter = 0

    # Opens the Positive.txt file than sets all the words to a list which will than be compared
    with open("PositiveSentimentWords.txt", 'r') as f:
        pos_main = f.read()
        pos_main = pos_main.split('\n')

    # OPens the Negative.txt file than sets all the words to a list which will than be compared
    with open('NegativeSentimentWords.txt', 'r') as f:
        neg_main = f.read()
        neg_main = neg_main.split('\n')

    # tokenizer will split our sentences
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # Here we open the filename (Hounds) and start to remove symbols
    # that would interfere with checking the word of the sentence with
    # the words in the lists. Example: Happy, != Happy
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()
        text = text.replace(',', '')
        text = text.replace("'", '')
        text = text.replace('"', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        text = text.replace('[', '')
        text = text.replace(']', '')
        text = text.replace(':', '')
        text = text.replace(';', '')
        text = text.replace("'s", '')

    # Here nltk comes into play, first we separate all of the sentences
    # with new lines and a couple of dashes
    # From there we remove punctuation to prevent cases like happy! != happy
    # Then we make a giant list of all the sentences by splitting on the dashes and newlines that we joined on
    # and call that list full
    x = '\n-----\n'.join(tokenizer.tokenize(text))
    x = x.replace('.', '')
    x = x.replace('?', '')
    x = x.replace('!', '')
    full = x.split('\n-----\n')

    # Here is where the script counts the words in the book (list)
    # It starts by setting the pos and negative counter to zero
    # Then we split the words in the sentence by spaces and iterate
    # When checking the word, if the word is in a corresponding pos/neg list
    # the counter increases
    # When we reach the end of the sentence the script checks which was the greater counter pos or neg
    # than adds that sentence to the final count of positive, negative, or neutral sentences.
    for sentence in full:
        pos_counter = 0
        neg_counter = 0
        for word in sentence.split():
            if word in pos_main:
                pos_counter += 1
            elif word in neg_main:
                neg_counter += 1
        if pos_counter > neg_counter:
            fin_pos_counter += 1
        elif pos_counter < neg_counter:
            fin_neg_counter += 1
        else:
            fin_neutral_counter += 1
    print('Positive: %i \nNegative: %i \nNeutral: %i' % (fin_pos_counter, fin_neg_counter, fin_neutral_counter))


# Delete the # infront of install, if you want to use it.
# install('nltk')

# There's a print statement at the end of the function, so just run it as is.
# You  may see some text about nltk_data in red, just ignore it.
# Use da_counter on your filepath/filename

da_counter('Hounds.txt')
