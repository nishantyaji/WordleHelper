## What this program does

This is a rudimentary helper for Wordle game. (https://en.wikipedia.org/wiki/Wordle_(video_game))

While attempting the game/puzzle you come to know about some letters being present in the word but in wrong position - through the color coding of yellow for such letters. The letters that have been guessed in the correct position are graded in green color.

Using this information you can narrow down the possible combination of letters.

Suppose you are sure that the 2nd letter is E and the 4th letter is E. And you know that T is in the word but you guessed wrong that the position was the 5th letter - this correctness in the letter but wrongness in the position is evidenced in yellow colored cell encompassing the letter.

For this case mentioned in the above para, you can see, through either common sense or jogging your mind, that the answer fits into one of the formats:

- T E _ E _
- _ E T E _

This rudimentary program automates the display of such possibilites by taking in the input about the letters, with their correct position (for the green colored cells) or their wrong position (for the yellow colored cells).

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

### SURE

When you are sure of a letter and its position, you enter the info through this command.
Suppose you are that E is the second letter and T is the third letter you enter the following in the console

```
sure E 1
sure T 2
```

Note that the position is always 1 less than the counting order - i.e. the position is equal to the array ordinal

### UNSURE

When you are sure of a letter but you got the position wrong, then you enter the info through this command.
Suppose you guessed G to be the first letter - but you got a yellow color cell for it then you enter the info as follows

```
unsure G 0
```

Note that the position is always 1 less that order - i.e. the position is the array ordinal

### REDUCE

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

### DISPLAY

This command displays the possibilities given the info that you entered through `sure`, `unsure` and `reduce`.
Suppose you entered the following through CLI

```
unsure n 0
unsure e 1
unsure u 3
```

Then the ``display` command would result in the following being printed to the console

```
display
U N E _ _
U _ E N _
U N _ E _
U _ N E _
E U N _ _
E U _ N _
_ U E N _
_ U N E _
E N _ _ U
E _ N _ U
E _ _ N U
_ N E _ U
_ _ E N U
_ N _ E U
_ _ N E U
```

### RESET

Reset wipes any input that you had given and starts afresh - blank slate is what you get.
You can start afresh your approach to a problem or switch to another problem swimmingly through this command.
Usage is

```
reset
```

### QUIT/LOGOUT/EXIT

Typing the following will let you out of this kiddish program.
Usage

```
quit
```

or

```
logout
```

or

```
exit
```
