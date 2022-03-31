<p align="center">
 
 <a href="https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot/" alt="LOGO" >
        <img src="https://user-images.githubusercontent.com/56127795/157863462-ecf46e40-76ed-44cf-8024-05c87066c636.png" /></a><br><br>
</p>

<div align="center">
    Built by:
        <a href="https://github.com/lea-s">Lea</a>,
        <a href="https://github.com/natibckr">Natascha</a>,
        <a href="https://github.com/fulachs">Felix</a>,
        <a href="https://github.com/nowo2000">Noah</a> and all
        <a href="https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot/graphs/contributors">contributors</a>
    
</div>

<br>

<p align="center">
 
 <a href="https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot/commits/main" alt="last commit">
        <img src="https://img.shields.io/github/last-commit/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot/main" /></a>
 <a href="https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot/issues" alt="issues">
        <img src="https://img.shields.io/github/issues/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot" /></a>
 <a href="https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot" alt="total lines">
        <img src="https://img.shields.io/tokei/lines/github/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot" /></a>
 <a href="https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot" alt="top language">
        <img src="https://img.shields.io/github/languages/top/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot" /></a>
</p>

---

- You are bored, then write to your [MOT](https://t.me/waseinbot) and he will help you pass the time by playing a game with you.
- Optionally expandable with more games and ways to pass the time.
- In addition, he can tell you a lot of information or pictures about different things to pass the time
- The focus is on a working mini-game, playable in Telegram with the bot. After that more modules (games or random facts) are planned.

# How to start your own MOT-Bot

Any further information how to run a MOT, can be found in our [Github Repository](https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot)


# Use this Python Package

- You can find our Python Package here: [MOT-Bot-Game Package](https://test.pypi.org/project/MOT-Bot-Games/)

- Our Package is based on the [Python Telegram Extension](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html). To use our Package you need to add each game into the "Commandhandler" in you `main.py` file. You need to import some of the Methods like following:

```python
# Imports for all Game Commands
from telegram.ext import CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

# Create the Updater and pass it your bot's token.
updater = Updater(API_KEY)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher
```

- After preparing your `main.py` you need to install our package:

```bash
pip install -i https://test.pypi.org/simple/ MOT-Bot-Games
```

- After installing and importing the package you can use the following commands to get started with the individual games:

Here is an example for Numbergame:

```python
from numbergame import numb, stopnumbergame, numbergame, newnum

dispatcher.add_handler(CommandHandler("numbergame", numbergame))
dispatcher.add_handler(CommandHandler("stopnumbergame", stopnumbergame))
dispatcher.add_handler(CommandHandler("numb", numb))
dispatcher.add_handler(CommandHandler("newnum", newnum))
```
All of oure games have specific methods you have to add to your Command Handler:


### Numbergame:

`numbergame`: start the game
`numb`: guess a number
`stopnumbergame`: stop a running game
`newnum`: set new numberrange

### Wordle

`wordle`: start the game
`guess`: guess a word
`stop`: stop a running game
`howto`: how to play wordle
`stats`: stats about all your wordle games

### TicTacToe

`tictactoe`: start the game
`pos`: to set your X
`stoptictactoe`: stop a running game

### Movie Guessing Game

Our Movie Game uses the Conversation Handler of telegram. To import the Handler use the following:

```python
movie_guessing_game = ConversationHandler(
       entry_points=[CommandHandler("movieguessinggame", movieguessinggame)],
       states={
       PLAYMODE: [MessageHandler(Filters.regex("^(Easy|Hard)$"), playmode)],
       GUESS: [MessageHandler(Filters.regex("^[\w*\s]*$"), movieguess)],
       },
       fallbacks=[CommandHandler("stopgame", stopgame)],
)

dispatcher.add_handler(movie_guessing_game)
dispatcher.add_handler(CommandHandler("stopgame", stopgame))
```

The Methods for the MovieGuessingGame are:

`movieguessinggame`: start the game
`stopgame`: stop a running game


- For more information, feel free to check out our [Wiki](https://github.com/NoWo2000/MOT-Multi-Functional-Bot/wiki).

# You need help or further information of this repo?

In case Commandos or other things are not clear, there is a detailed documentation of our repo under the Wiki tab.
Or if you have any other questions about technology decisions, or you have questions about tools or scaling the bot, check out the wiki page. [MOT-Bot Wiki](https://github.com/MOT-Multi-Functional-Bot/MOT-Multi-Functional-Bot/wiki)

