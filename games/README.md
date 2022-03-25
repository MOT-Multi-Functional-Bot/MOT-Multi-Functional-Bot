<p align="center">
 
 <a href="https://github.com/NoWo2000/MOT-Multi-Functional-Bot/" alt="LOGO" >
        <img src="https://user-images.githubusercontent.com/56127795/157863462-ecf46e40-76ed-44cf-8024-05c87066c636.png" /></a><br><br>
</p>

<div align="center">
    Built by:
        <a href="https://github.com/lea-s">Lea</a>,
        <a href="https://github.com/natibckr">Natascha</a>,
        <a href="https://github.com/fulachs">Felix</a>,
        <a href="https://github.com/nowo2000">Noah</a> and all
        <a href="https://github.com/NoWo2000/MOT-Multi-Functional-Bot/graphs/contributors">contributors</a>
    
</div>

<br>

<p align="center">
 
 <a href="https://github.com/NoWo2000/MOT-Multi-Functional-Bot/commits/main" alt="last commit">
        <img src="https://img.shields.io/github/last-commit/NoWo2000/MOT-Multi-Functional-Bot/main" /></a>
 <a href="https://github.com/NoWo2000/MOT-Multi-Functional-Bot/issues" alt="issues">
        <img src="https://img.shields.io/github/issues/NoWo2000/MOT-Multi-Functional-Bot" /></a>
 <a href="https://github.com/NoWo2000/MOT-Multi-Functional-Bot" alt="total lines">
        <img src="https://img.shields.io/tokei/lines/github/NoWo2000/MOT-Multi-Functional-Bot" /></a>
 <a href="https://github.com/NoWo2000/MOT-Multi-Functional-Bot" alt="top language">
        <img src="https://img.shields.io/github/languages/top/NoWo2000/MOT-Multi-Functional-Bot" /></a>
</p>

---

- You are bored, then write to your [MOT](https://t.me/waseinbot) and he will help you pass the time by playing a game with you.
- Optionally expandable with more games and ways to pass the time.
- In addition, he can tell you a lot of information or pictures about different things to pass the time
- The focus is on a working mini-game, playable in Telegram with the bot. After that more modules (games or random facts) are planned.

# How to start your own MOT-Bot

You can run our bot directly in python or run it in a docker container!

## Use a docker container

- Clone the repository
- Rename the `conf.template.py` to `conf.py` and add your own API-Key.
  If you don't know how to do this open the `conf.template.py` and read the instructions.
- Run:

```bash
   docker-compose up -d
```

## Run it directly in python

Create your own MOT:

- Clone this repository
- Install all requirements:

```bash
pip3 install -r requirements.txt --upgrade
```

- Rename the `conf.template.py` to `conf.py` and add your personal API-Key.
  - If you don't know how to do this open the `conf.template.py` and read the instructions.
- To run the bot go to your console and type:

```bash
python3 main.py
```

- To get all the functionalities type `/help`. For further information visit the [MOT-Bot Wiki](https://github.com/NoWo2000/MOT-Multi-Functional-Bot/wiki) page.

# You need help or further information of this repo?

In case Commandos or other things are not clear, there is a detailed documentation of our repo under the Wiki tab.
Or if you have any other questions about technology decisions, or you have questions about tools or scaling the bot, check out the wiki page. [MOT-Bot Wiki](https://github.com/NoWo2000/MOT-Multi-Functional-Bot/wiki)

