# readable-nicephrases
niceware passphrases made into english sentences

This notebook is my attempt to build a passphrase generator to assist people in creating more secure yet memorable passwords, inspired by the following xkcd comic: https://xkcd.com/936/

The struture of this generator is (i believe) relatively straightforward:

1. Generate a pool of possible words
2. Use a natural language model to associate each word with a different part of speech (noun, verb, adjective, adverb, etc)
3. Create a list of possible combinations that sound like reasonable sentences (e.g. subject verb object, subject modifier verb, etc)

I don't recommend this method for generating every password you use (and if the whole FIDO/Passkey thing works out, we won't need this at all in the future), as a password manager will take care of that a LOT better than your brain, but for situations where a password manager cannot or should not be used this is in my opinion a valid solution. At the very least, it might help us get our parents to stop using "PetName1234!" for all of their accounts!

Niceware is set to the maximum bit value to generate the largest pool of words possible, but you're welcome to reduce it if there are any performance issues on your end. The minimum recommended value is 6, which will provide 3 words. 
