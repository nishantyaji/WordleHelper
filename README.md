## What this program does

This is a rudimentary helper for Wordle game. (https://en.wikipedia.org/wiki/Wordle_(video_game))

While attempting the game/puzzle we come to know about some letters being present in the word but in wrong position - through the color coding of yellow for such letters. The letters that have been guessed in the correct position are graded in green color.

Using this information we can narrow down the possible combination of letters.

Suppose we are sure that the 2nd letter is E and the 4th letter is E. And we know that T is in the word but we guessed that the position was 5th letter - and our guess about the position was wrong even though the letter is the word (evidence in yellow colored cell)

We, can see, through either common sense or running in our mind that the answer fits into one of the formats

- T E _ E _
- _ E T E _

This rudimentary program automates the display of the possibilites but taking in the input about the letters, their correct position (for the green colored cells) or their wrong position (for the yellow colored cells).

## Usage

Bring up the program using the following command:

```
python CommandLine.py
```

There are 6 functionalities present

- SURE
- UNSURE
- REDUCE
- DISPLAY
- RESET
- QUIT/LOGOUT/EXIT

#SURE
When you are sure of a letter and its position, you enter the info through this command.
Suppose you are that E is the second letter and T is the third letter you enter the following in the console

```
sure E 1
sure T 2
```

Note that the position is always 1 less that order - i.e. the position is the array ordinal

#UNSURE
When you are sure of a letter but you got the position wrong, then you enter the info through this command.
Suppose you guessed G to be the first letter - but you got a yellow color cell for it then you enter the info as follows

```
unsure G 0
```

Note that the position is always 1 less that order - i.e. the position is the array ordinal

#REDUCE
You do this when you guessed a word correct and got position wrong and later you got the position correct for the same word. Suppose you guess Y as the first letter and you got the yellow colored cell - that indicates that Y is indeed in the word but the first letter is not its place. In a later attempt you guessed correctly that Y is in the last place.

Given that you entered unsure command before and sure command later, the unsure command is now obsolete and needs to be erased. So you use `reduce`
The sequence of commands will be

```
unsure Y 0
.
.
unsure Y 4
reduce
```

#DISPLAY
This command displays the possibilities given the info that you entered through '''sure''', '''uns
