# src/coach.py
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from champions import (
    get_champion_plan,
    get_champion_quick_tip,
    normalize_champion_name,
    supported_champions,
)


@dataclass
class PlayerProfile:
    rank: str
    role: str
    champions: List[str]
    focus_champ: str
    struggle: str
    goal: str


def ask(prompt: str, valid: Optional[List[str]] = None) -> str:
    """
    Prompt until the user enters a non-empty answer.
    If `valid` is provided, enforce membership (case-insensitive).
    """
    while True:
        ans = input(prompt).strip()
        if not ans:
            print("Please enter something.\n")
            continue

        if valid:
            lowered = {v.lower(): v for v in valid}
            if ans.lower() not in lowered:
                print(f"Please choose one of: {', '.join(valid)}\n")
                continue
            return lowered[ans.lower()]

        return ans


def clean_champion_list(champs: List[str]) -> List[str]:
    """Normalize known ADC names while keeping unsupported names readable."""
    cleaned: List[str] = []
    for champ in champs:
        champ = champ.strip()
        if not champ:
            continue
        cleaned.append(normalize_champion_name(champ) or champ.title())
    return cleaned


def pick_focus_champ(champs: List[str]) -> str:
    """
    Let the user choose which champion to focus on today.
    Accepts either a number (1..N) or a champion name/alias.
    """
    champs = clean_champion_list(champs)

    if not champs:
        return ""

    if len(champs) == 1:
        return champs[0]

    print("\nWhich champion are you focusing on today?")
    for i, c in enumerate(champs, start=1):
        print(f"{i}) {c}")

    while True:
        choice = input("Type the number or champion name: ").strip()
        if not choice:
            print("Please enter a number or champion name.\n")
            continue

        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(champs):
                return champs[idx - 1]
            print("That number isn't in the list.\n")
            continue

        normalized_choice = normalize_champion_name(choice) or choice.title()
        for c in champs:
            if normalized_choice.lower() == c.lower():
                return c

        print("Please choose one of the listed champions.\n")


def build_profile() -> PlayerProfile:
    rank = ask("Rank (e.g., Bronze, Silver, Gold, Platinum, Emerald, Diamond): ")
    role = ask("Role (ADC, Top, Mid, Jungle, Support) [default ADC]: ").strip() or "ADC"

    print("\nSupported ADCs right now:", ", ".join(supported_champions()))
    champs_raw = ask("Top champs (comma-separated, e.g., Jhin, Kai'Sa, Ezreal): ")
    champs = clean_champion_list(champs_raw.split(","))

    focus_champ = pick_focus_champ(champs)

    struggle = ask(
        "\nBiggest struggle (laning / midgame / teamfights / consistency): ",
        valid=["laning", "midgame", "teamfights", "consistency"],
    )

    goal = ask(
        "Goal (fast / long-term): ",
        valid=["fast", "long-term"],
    )

    return PlayerProfile(
        rank=rank.strip().title(),
        role=role.strip().upper(),
        champions=champs,
        focus_champ=focus_champ,
        struggle=struggle,
        goal=goal,
    )


def rank_overlay(rank: str) -> str:
    r = rank.lower()
    if "platinum" in r or "emerald" in r or "diamond" in r:
        return (
            "As a higher-elo player, your biggest gains usually come from "
            "**discipline and tempo** (avoiding low-value fights, cleaner resets, and consistent decision-making)."
        )
    if "gold" in r or "silver" in r:
        return (
            "At this rank, you’ll climb fastest by tightening **fundamentals**: "
            "better deaths, better recalls, and fewer coinflip fights."
        )
    return (
        "Focus on **repeatable habits**: fewer deaths, clearer fight rules, and simple win conditions every game."
    )


def general_adc_plan(struggle: str, goal: str) -> str:
    base = [
        "### Next 10 Games Focus (ADC)",
        "- Rule #1: If you die early, play the next 3 minutes **boring** (farm, stabilize, no hero plays).",
        "- Rule #2: Don’t fight unless you can answer: **Where is the enemy jungler?**",
        "- Rule #3: Before every fight, identify the 1 ability that can kill you and play around it.",
    ]
    if struggle == "consistency":
        base.append("- Tilt rule: after 2 frustrating games, take a 10-minute reset or stop queue.")
    if goal == "fast":
        base.append("- Fast climb tip: keep your champ pool small and spam comfort picks.")
    return "\n".join(base)


def generate_plan(profile: PlayerProfile) -> str:
    lines: List[str] = []
    lines.append(f"\n--- Personalized Plan for {profile.rank} {profile.role} ---\n")
    lines.append(rank_overlay(profile.rank))
    lines.append("")

    chosen = normalize_champion_name(profile.focus_champ or "")

    if not chosen:
        lines.append("No supported focus champion selected — here’s a general ADC plan:\n")
        lines.append(general_adc_plan(profile.struggle, profile.goal))
        return "\n".join(lines)

    lines.append(f"Champion focus: **{chosen}**\n")
    lines.append(get_champion_plan(chosen, profile.struggle, profile.goal))
    return "\n".join(lines)


def pick_from(prompt: str, options: List[str]) -> str:
    """Pick from a list via number or exact text."""
    print(prompt)
    for i, opt in enumerate(options, start=1):
        print(f"{i}) {opt}")
    while True:
        ans = input("Choose a number or type it: ").strip()
        if not ans:
            print("Please enter something.\n")
            continue
        if ans.isdigit():
            idx = int(ans)
            if 1 <= idx <= len(options):
                return options[idx - 1]
            print("That number isn't in the list.\n")
            continue
        for opt in options:
            if ans.lower() == opt.lower():
                return opt
        print("Please choose one of the listed options.\n")


def champ_review_tip(champ: str) -> str:
    return get_champion_quick_tip(champ)


def diagnose(death: str, phase: str, emotion: str) -> str:
    if emotion in ("tilted", "frustrated") and death in ("greed", "chase"):
        return (
            "This game likely slipped because frustration led to rushed decisions. "
            "Once that happened, small mistakes stacked into bigger losses."
        )

    if death == "gank":
        return (
            "You probably gave up tempo by not respecting jungle pressure. "
            "That usually turns a playable lane into a losing one very quickly."
        )

    if death == "positioning" and phase in ("midgame", "teamfights"):
        return (
            "You were likely positioned too aggressively before key threats were shown, "
            "which cost you fights before you could do meaningful damage."
        )

    if death == "trade":
        return (
            "You likely took trades outside your actual winning window "
            "(cooldowns, wave state, or item timing)."
        )

    return (
        "This loss was probably caused by a few small, avoidable mistakes rather than one big throw. "
        "Cleaning up those moments is where the improvement is."
    )


def review_rules(death: str, phase: str) -> List[str]:
    if death == "gank":
        return [
            "Assume the jungler is nearby until proven otherwise.",
            "If you don’t know where the jungler is, don’t trade.",
            "Ward earlier instead of reacting after you’ve already died.",
        ]

    if death == "positioning":
        return [
            "Stand farther back until engage tools are used.",
            "If you wouldn’t walk there without vision, don’t.",
            "Your damage doesn’t matter if you die first.",
        ]

    if death == "greed":
        return [
            "Stop staying for one more wave without information.",
            "After a kill, take something guaranteed and leave.",
            "Winning doesn’t require squeezing every advantage.",
        ]

    if death == "trade":
        return [
            "Only trade when you clearly win the exchange.",
            "If the wave is bad, fix the wave before fighting.",
            "Short trades > extended fights by default.",
        ]

    return [
        "Reduce unnecessary fights.",
        "Prioritize staying alive over forcing plays.",
        "Play the game state you have, not the one you want.",
    ]


def micro_drill(phase: str) -> str:
    drills = {
        "laning": "Drill (next 2 games): Track jungle start + respect gank timers. Call out where jungler is every 60 seconds.",
        "midgame": "Drill (next 2 games): Don’t show first to river. Rotate after pushing a wave and ping your path.",
        "teamfights": "Drill (next 2 games): Identify the 1 ability that kills you, then position ONLY around that threat.",
    }
    return drills.get(phase, "Drill (next 2 games): Pick one rule and follow it for the full match.")


def detect_tilt(text: str) -> bool:
    tilt_keywords = [
        "tilt", "tilted", "frustrated", "annoyed",
        "angry", "unplayable", "inting",
        "always", "never", "can’t win", "can't win"
    ]
    text = text.lower()
    return any(word in text for word in tilt_keywords)


def post_game_review() -> str:
    print("\n--- Post-Game Review ---")

    champ = input("What champ did you play? ").strip()
    champ = normalize_champion_name(champ) or champ.title()

    phase = pick_from(
        "\nWhere did the game start going wrong?",
        ["laning", "midgame", "teamfights"]
    )

    death = pick_from(
        "\nWhat caused your FIRST death mainly?",
        ["gank", "trade", "positioning", "greed", "other"]
    )

    emotion = pick_from(
        "\nHow did you feel during the game?",
        ["calm", "focused", "frustrated", "tilted", "tired"]
    )

    tilt_detected = emotion in ("frustrated", "tilted", "tired")

    one_good = input("\nOne thing you did well (short): ").strip()
    one_fix = input("One thing you want to improve next game (short): ").strip()

    diag = diagnose(death, phase, emotion)
    rules = review_rules(death, phase)
    drill = micro_drill(phase)
    champ_tip = champ_review_tip(champ)

    tilt_line = ""
    if tilt_detected:
        tilt_line = (
            "\nHonest note: This game sounded mentally draining. "
            "If you’re not feeling reset, taking a short break before queueing again "
            "will probably save you LP.\n"
        )

    return (
        f"\n=== Post-Game Reality Check ===\n"
        f"Champion: {champ}\n"
        f"Problem phase: {phase}\n"
        f"First death cause: {death}\n"
        f"Mental state: {emotion}\n\n"
        f"Diagnosis: {diag}\n\n"
        f"Your rule for next game: {rules[0]}\n\n"
        f"Fix plan (next 1–3 games):\n"
        f"- {rules[0]}\n"
        f"- {rules[1]}\n"
        f"- {rules[2]}\n\n"
        f"{drill}\n"
        f"{champ_tip}\n\n"
        f"You did well: {one_good or '—'}\n"
        f"Next improvement: {one_fix or '—'}\n"
        f"{tilt_line}"
    )


def format_profile(profile: PlayerProfile) -> str:
    champs = ", ".join(c for c in profile.champions) if profile.champions else "None"

    rank = profile.rank.title()
    role = profile.role.upper()
    focus = normalize_champion_name(profile.focus_champ) or profile.focus_champ.title() if profile.focus_champ else "None"
    struggle = profile.struggle.replace("_", " ").title()
    goal = "Fast Climb" if profile.goal == "fast" else "Long-Term Improvement"

    return (
        "\n=== Player Profile ===\n"
        f"Rank: {rank}\n"
        f"Role: {role}\n"
        f"Champion Pool: {champs}\n"
        f"Focus Champion: {focus}\n"
        f"Primary Struggle: {struggle}\n"
        f"Goal Type: {goal}\n"
    )


def run_coach():
    profile = build_profile()

    last_plan = generate_plan(profile)
    print(last_plan)

    while True:
        cmd = input("Command (/profile, /plan, /review, /reset, /exit): ").strip().lower()

        if cmd in ("/exit", "exit", "quit", "/quit"):
            print("GG. See you next session.")
            break

        if cmd == "/review":
            print(post_game_review())
            continue

        if cmd == "/profile":
            print(format_profile(profile))
            continue

        if cmd == "/plan":
            print(last_plan)
            continue

        if cmd == "/reset":
            print("\nResetting session...\n")
            profile = build_profile()
            last_plan = generate_plan(profile)
            print(last_plan)
            continue

        print("Unknown command. Try /profile, /plan, /review, /reset, or /exit.\n")
