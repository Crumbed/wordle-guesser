# Wordle Algorithm

Everything you need to know will be found here.

## How do I run it?

1.  Make sure you have pyhton 3 or newer installed.
2.  Download `wordle_algorithm.py` and `weighted_records.csv` (make sure they are in the same folder).
3.  Install dataclasses library. Type:

        pip install dataclasses

After that: 4. Go to the file directory of `wordle_algorithm.py`. Ex:

    	C:\Desktop\Wordle-Guesser

5.  Open cmd and type:

        cd C:\Desktop\Wordle-Guesser
        python wordle_algorithm.py

and hit enter.

## How do I use it?

1.  You will be prompted with with a choice:

        (1) Input your own guess
        (2) Use recommended guess

2.  Then the program will display something like this:

        ---------------------------------------
        Guess: 1, salet
        ---------------------------------------
        Enter 'END' to stop the program and log your score.
        Enter the output of salet (gray: b, yellow: y, green: g):

3.  In this example you would enter `salet` into wordle. And enter the information wordle gives you. Ex:

        Enter the output of salet (gray: b, yellow: y, green: g): bgyyb

4.  Then the program will display a string with the positions of the known letters followed by a list a the most likely guesses.

        Known letter possitions: -a---
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        Top picks based on probability:
        large: 78.9352
        early: 77.8138
        lance: 76.8212
        cable: 50.1691
        fable: 46.9729
        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

5.  And repeat! Remember to type `end` in the output line to stop the program.

# How does it work?

## The algorithm

1. Well first the program opens and reads the `weighted_records.csv` file that the `dataStorage.py` script generates. (see more about that script below)

2. Then the program asks the user if they want to use a custom answer or the recommended answer, then runs a function called `getNextGuess`.
