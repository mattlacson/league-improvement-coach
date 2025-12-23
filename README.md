# League Improvement Coach Bot

A CLI chatbot designed to help League of Legends players improve through personalized, rank-aware, champion-specific coaching.  
Instead of dumping stats or generic tips, the bot focuses on habit-building, decision discipline, and actionable improvement plans.

## Problem

Many League of Legends tools focus heavily on statistics, builds, or raw data.
While useful, these tools often fail to address what actually holds players back:
poor decision-making, inconsistency, tilt, and not knowing what to focus on from game to game.

Players often leave a loss knowing they played badly, but not knowing *why* or *what to change next*.

## Solution

The League Improvement Coach Bot acts as a conversational improvement coach.
It asks players about their rank, role, champion pool, and current struggles,
then generates a focused improvement plan tailored to their context.

The goal is not to overwhelm the player, but to give them
2–3 clear rules to follow over their next set of games.

## Features

- Rank-aware coaching (advice adapts to player rank)
- Champion-specific guidance (currently Jhin, Vayne, and Jinx)
- User-selected focus champion
- “Next 10 Games” improvement plans
- Post-game reflection tool (`/review`)
- Persistent player profile (`/profile`)
- Re-runnable coaching plan (`/plan`)

## Sample Conversation (below)

=== League Improvement Coach Bot (CLI) ===

Rank (e.g., Bronze, Silver, Gold, Platinum, Emerald, Diamond): Platinum
Role (ADC, Top, Mid, Jungle, Support) [default ADC]: ADC

Supported champs right now: Jhin, Vayne, Jinx
Top champs (comma-separated, e.g., Jhin, Vayne, Jinx): Jhin, Vayne, Jinx

Which champion are you focusing on today?

Jhin

Vayne

Jinx
Type the number or champion name: Jhin

Biggest struggle (laning / midgame / teamfights / consistency): consistency
Goal (fast / long-term): fast

--- Personalized Plan for Platinum ADC ---

As a higher-elo player, your biggest gains usually come from discipline and tempo
(avoiding low-value fights, cleaner resets, and consistent decision-making).

Champion focus: Jhin

Identity: Tempo & precision — burst windows and spacing.
Win condition: Control tempo and punish mistakes; avoid extended DPS fights.

Next 10 Games Focus

If you miss a burst window, don’t force — reset and wait for the next one.

After every 4th shot, immediately reposition.

Track one engage threat and position around it every fight.

Fast climb note: Keep your champion pool small and avoid testing new champions in ranked.

Command (/profile, /plan, /review, /exit): /profile

=== Player Profile ===
Rank: Platinum
Role: ADC
Champion Pool: Jhin, Vayne, Jinx
Focus Champion: Jhin
Primary Struggle: Consistency
Goal Type: Fast Climb



## Tech Stack

- Language: Python
- Interface: Command-line (CLI)
- Architecture: Modular Python files with rule-based coaching templates
- Version Control: Git & GitHub

## Design Decisions

- Text-only interface was chosen to focus on logic, clarity, and coaching quality.
- Champion pool is intentionally limited to ensure advice is specific and meaningful.
- Coaching output prioritizes habits and rules over raw statistics.
- Rank-awareness is used to adjust expectations and advice tone.

## Limitations

- No live Riot API integration
- Limited champion pool
- Advice is based on coaching heuristics, not match history data

## Future Improvements

- Additional champions and roles
- Matchup-specific advice
- Session reset command
- Optional web-based interface
