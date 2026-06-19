# League Improvement Coach Bot

A Python command-line coaching bot designed to help League of Legends ADC players improve through personalized, rank-aware, and champion-specific advice.

The project currently focuses on the ADC role, but it is designed to be expandable so future versions can support other roles such as Top, Jungle, Mid, and Support.

Instead of focusing only on statistics, builds, or raw match data, this bot focuses on practical improvement habits such as better positioning, smarter fights, tilt control, consistency, and post-game reflection.

## Problem

Many League of Legends tools focus heavily on stats, champion builds, or match history. While useful, those tools do not always explain what a player should actually focus on improving in their next few games.

Players often know they played badly after a loss, but they may not know whether the problem came from laning, midgame decisions, teamfighting, positioning, greed, tilt, or poor consistency.

## Solution

League Improvement Coach Bot acts as a lightweight improvement coach for ADC players. It asks for the player's rank, role, champion pool, focus champion, biggest gameplay struggle, and improvement goal. Based on those answers, it generates a focused improvement plan with simple rules to follow over the next 10 games.

The goal is to give players clear, actionable advice instead of overwhelming them with too much information.

## Features

* Rank-aware coaching based on player skill level
* Champion-specific coaching for ADC champions
* User-selected focus champion
* Personalized “Next 10 Games” improvement plans
* Post-game review tool with structured reflection questions
* Persistent session profile using `/profile`
* Re-runnable coaching plan using `/plan`
* Session reset using `/reset`
* Fallback general ADC plan for unsupported inputs
* Handles common champion nicknames and alternate spellings

## Supported Champions

The bot currently supports coaching plans for ADC champions such as:

* Aphelios
* Ashe
* Caitlyn
* Corki
* Draven
* Ezreal
* Jhin
* Jinx
* Kai'Sa
* Kalista
* Kog'Maw
* Lucian
* Miss Fortune
* Nilah
* Samira
* Senna
* Sivir
* Smolder
* Tristana
* Twitch
* Varus
* Vayne
* Xayah
* Yunara
* Zeri

Each champion includes coaching advice based on their identity, win condition, common mistakes, and focus areas such as laning, midgame, teamfights, and consistency.

## Tech Stack

* **Language:** Python
* **Interface:** Command-Line Interface
* **Architecture:** Modular Python files
* **Core Concepts:** Data structures, input validation, conditional logic, reusable functions, and rule-based coaching templates
* **Version Control:** Git and GitHub

## Project Structure

```text
league-improvement-coach/
│
├── src/
│   ├── main.py
│   ├── coach.py
│   └── champions.py
│
└── README.md
```

## How It Works

1. The user enters their rank, role, champion pool, focus champion, biggest struggle, and improvement goal.
2. The program creates a player profile from the user's answers.
3. The bot applies rank-aware coaching logic based on the player's rank.
4. If the selected champion is supported, the bot generates champion-specific advice.
5. The user can review their profile, repeat their plan, complete a post-game review, reset the session, or exit the program.

## Example Commands

```text
/profile
```

Displays the current player profile.

```text
/plan
```

Shows the current personalized improvement plan again.

```text
/review
```

Starts a post-game review that helps diagnose what went wrong and gives the player a rule to focus on next game.

```text
/reset
```

Resets the current session and creates a new player profile.

```text
/exit
```

Ends the program.

## Example Output

```text
--- Personalized Plan for Platinum ADC ---

As a higher-elo player, your biggest gains usually come from discipline and tempo.

Champion focus: Jhin

Identity: Tempo & precision — burst windows and spacing.
Win condition: Control tempo and punish mistakes; avoid extended DPS fights.

Common mistakes to avoid:
- Using 4th shot aggressively with no escape plan
- Standing too close after your burst
- Ulting too early instead of using R to close or finish fights

Next 10 Games Focus:
- If you miss a burst window, don’t force — reset and wait for the next one.
- Play fights slower and value staying alive over highlight plays.
- Track one key threat and position around it.
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/mattlacson/league-improvement-coach
```

Move into the project folder:

```bash
cd league-improvement-coach
```

Run the program:

```bash
python src/main.py
```

If that does not work, try:

```bash
python3 src/main.py
```

## Design Decisions

* A command-line interface was used to keep the project focused on logic, structure, and coaching quality.
* The project uses rule-based coaching templates instead of machine learning so the advice stays simple and predictable.
* ADC was chosen as the main role focus to keep the advice specific and useful.
* Champion advice is separated into reusable data structures to make it easier to add or update champions.
* Post-game reflection was added to help users turn losses into specific improvement goals.

## Limitations

* No live Riot API integration
* No real match history analysis
* Advice is based on rule-based coaching logic instead of player statistics
* The app currently runs only through the command line
* Coaching is focused mainly on ADC gameplay

## Future Improvements

* Add support for other roles such as Top, Jungle, Mid, and Support
* Create role-specific coaching plans for wave management, jungle pathing, roaming, vision control, objective setup, and teamfight responsibilities
* Add more champions for each role
* Add Riot API integration for match-history-based recommendations
* Save player profiles between sessions
* Track improvement goals across multiple games
* Add matchup-specific advice
* Build a web interface using Flask, Django, or React
* Add a simple database for storing player reviews and improvement history
