# League Improvement Coach Bot

A Python command-line coaching tool designed to help League of Legends players improve through personalized, rank-aware, and champion-specific advice.

Instead of focusing on raw statistics, builds, or match history data, the bot helps players build better in-game habits through simple improvement rules, focused practice goals, and post-game reflection.

## Problem

Many League of Legends tools focus heavily on statistics, champion builds, or performance data. While useful, those tools do not always explain *why* a player is struggling or what they should focus on in their next few games.

Players often know they made mistakes after a loss, but they may not know whether the issue came from laning, midgame decisions, teamfight positioning, tilt, greed, or poor consistency.

## Solution

League Improvement Coach Bot acts as a lightweight improvement coach. It asks the player for their rank, role, champion pool, focus champion, biggest struggle, and improvement goal. Based on those inputs, it generates a focused coaching plan with clear rules to follow over the next set of games.

The goal is to keep the advice simple and actionable rather than overwhelming the player with too much information.

## Features

* Rank-aware coaching based on player skill level
* Champion-specific coaching for Jhin, Vayne, and Jinx
* User-selected focus champion
* Personalized “Next 10 Games” improvement plans
* Post-game review tool using structured reflection questions
* Persistent session profile with `/profile`
* Re-runnable improvement plan with `/plan`
* Session reset command with `/reset`
* Fallback general ADC plan for unsupported champions

## Tech Stack

* **Language:** Python
* **Interface:** Command-line Interface (CLI)
* **Architecture:** Modular Python files
* **Core Concepts:** Data structures, input validation, conditional logic, reusable functions, rule-based recommendation templates
* **Version Control:** Git and GitHub

## How It Works

1. The user enters their rank, role, champion pool, focus champion, biggest struggle, and improvement goal.
2. The bot builds a player profile from the user’s answers.
3. The bot applies rank-aware coaching logic to adjust the tone and focus of the advice.
4. If the selected champion is supported, the bot generates champion-specific advice.
5. The user can review their profile, regenerate their plan, reset the session, or complete a post-game review.

## Supported Champions

* Jhin
* Vayne
* Jinx

Each champion has its own coaching profile, including identity, win condition, common mistakes, and focus rules for laning, midgame, teamfights, and consistency.

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

Starts a post-game reflection that helps diagnose what went wrong and gives rules for the next game.

```text
/reset
```

Clears the current session and builds a new player profile.

```text
/exit
```

Ends the program.

## Design Decisions

* A text-only CLI interface was used to keep the project focused on logic, structure, and coaching quality.
* The champion pool was intentionally limited so the advice could be more specific and meaningful.
* The bot prioritizes practical decision-making rules over raw statistics.
* Rank-aware coaching was added to make the advice feel more personalized.
* Post-game reflection was included to help users turn losses into specific improvement goals.

## Limitations

* No live Riot API integration
* Limited champion and role coverage
* Advice is based on rule-based coaching heuristics, not real match history data
* The app currently runs only through the command line

## Future Improvements

* Add more champions and roles
* Add matchup-specific advice
* Save player profiles between sessions
* Add match-history integration using the Riot API
* Build a web interface with Flask, Django, or React
* Add a simple database for tracking player improvement over multiple games
