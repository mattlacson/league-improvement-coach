from dataclasses import dataclass
from typing import List
from champions import get_champion_plan, supported_champions

@dataclass
class PlayerProfile:
    rank: str
    role: str
    champions: List[str]
    struggle: str
    goal: str

def ask(prompt: str, valid: List[str] | None = None) -> str:
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

def build_profile() -> PlayerProfile:
    rank = ask("Rank (e.g., Bronze, Silver, Gold, Platinum, Emerald, Diamond): ")
    role = ask("Role (ADC, Top, Mid, Jungle, Support) [default ADC]: ").strip() or "ADC"

    print("\nSupported champs right now:", ", ".join(supported_champions()))
    champs_raw = ask("Top champs (comma-separated, e.g., Jhin, Vayne, Jinx): ")
    champs = [c.strip().title() for c in champs_raw.split(",") if c.strip()]

    struggle = ask(
        "\nBiggest struggle (laning / midgame / teamfights / consistency): ",
        valid=["laning", "midgame", "teamfights", "consistency"]
    )

    goal = ask(
        "Goal (fast / long-term): ",
        valid=["fast", "long-term"]
    )

    return PlayerProfile(rank=rank.title(), role=role.upper(), champions=champs, struggle=struggle, goal=goal)

def rank_overlay(rank: str) -> str:
    r = rank.lower()
    if "platinum" in r or "emerald" in r or "diamond" in r:
        return ("As a higher-elo player, your biggest gains usually come from "
                "**discipline and tempo** (avoiding low-value fights, cleaner resets, and consistent decision-making).")
    if "gold" in r or "silver" in r:
        return ("At this rank, you’ll climb fastest by tightening **fundamentals**: "
                "better deaths, better recalls, and fewer coinflip fights.")
    return ("Focus on **repeatable habits**: fewer deaths, clearer fight rules, and simple win conditions every game.")

def generate_plan(profile: PlayerProfile) -> str:
    lines = []
    lines.append(f"\n--- Personalized Plan for {profile.rank} {profile.role} ---\n")
    lines.append(rank_overlay(profile.rank))
    lines.append("")

    chosen = None
    for c in profile.champions:
        if c.title() in supported_champions():
            chosen = c.title()
            break

    if chosen is None:
        lines.append("I don’t support your champs yet — but here’s a general ADC plan:\n")
        lines.append(general_adc_plan(profile.struggle, profile.goal))
        return "\n".join(lines)

    lines.append(f"Champion focus: **{chosen}**\n")
    lines.append(get_champion_plan(chosen, profile.struggle, profile.goal))
    lines.append("\nWant a quick post-game review? Type `/review` next.\n")
    return "\n".join(lines)

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

def post_game_review() -> str:
    print("\n--- Post-Game Review ---")
    champ = input("What champ did you play? ").strip().title()
    lane = input("How did lane go? (won / even / lost): ").strip().lower()
    death = input("What was your first death mainly due to? (gank / trade / positioning / greed / other): ").strip().lower()

    lesson = "One lesson for next game: "
    if death == "gank":
        lesson += "Track jungle start and respect common gank timers. Ward with a purpose, not randomly."
    elif death == "positioning":
        lesson += "Play one step farther back until key engage tools are used."
    elif death == "greed":
        lesson += "Take the safe reset. Don’t stay for one more wave if you don’t have vision."
    else:
        lesson += "Pick one repeatable rule (wave, ward timing, fight rule) and commit to it for 3 games."

    return f"\nChamp: {champ}\nLane: {lane}\nFirst death: {death}\n\n{lesson}\n"

def run_coach():
    profile = build_profile()
    print(generate_plan(profile))

    while True:
        cmd = input("Command (/review, /exit): ").strip().lower()
        if cmd in ("/exit", "exit", "quit", "/quit"):
            print("GG. See you next session.")
            break
        if cmd == "/review":
            print(post_game_review())
        else:
            print("Unknown command. Try /review or /exit.\n")
