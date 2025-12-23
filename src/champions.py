from typing import List

_CHAMPIONS = {
    "Jhin": {
        "identity": "Tempo & precision — burst windows and spacing.",
        "win_condition": "Control tempo and punish mistakes; avoid extended DPS fights.",
        "mistakes": [
            "Using 4th shot aggressively with no escape plan",
            "Standing too close after your burst",
            "Ulting too early instead of using R to close or finish fights",
        ],
        "focus": {
            "laning": [
                "Trade on your 4th shot + ability window, then **reposition**.",
                "Don’t walk up without knowing enemy engage threat range.",
                "Use wave control to create safe poke windows, not all-ins.",
            ],
            "midgame": [
                "Rotate early and play around objectives from safe angles.",
                "Use traps to control chokes and protect your flanks.",
                "Ult to start picks only when your team can follow immediately.",
            ],
            "teamfights": [
                "Enter late: let frontline/CC start, then burst targets that step up.",
                "After every burst window, reset your spacing.",
                "R is strongest as a finisher or to force retreats.",
            ],
            "consistency": [
                "If you miss a window, don’t force — reset and wait for the next one.",
                "Play fights slower and value staying alive over highlight plays.",
                "Track 1 key threat (flash engage/hook) and position around it.",
            ],
        },
    },
    "Vayne": {
        "identity": "Patience & punishment — survive early, take over later.",
        "win_condition": "Low-death lane → scale → slow fights → punish overcommitment.",
        "mistakes": [
            "Forcing trades early before spikes",
            "Using Q aggressively with no safety plan",
            "Using condemn offensively when you need it for self-peel",
        ],
        "focus": {
            "laning": [
                "Your goal is **low deaths**, not lane dominance.",
                "Take short trades only when enemy cooldowns are down.",
                "Save E for peel unless you’re 100% sure it’s a kill.",
            ],
            "midgame": [
                "Farm safely and avoid random skirmishes without vision.",
                "Only commit when key CC is used or you have space to kite.",
                "Side waves when safe — Vayne loves consistent gold.",
            ],
            "teamfights": [
                "Hit closest target until someone mispositions.",
                "Ult to outplay engage, not to chase.",
                "Play around invis timing: reposition, don’t tunnel on one target.",
            ],
            "consistency": [
                "Set a rule: if behind, no risky fights — only guaranteed farm.",
                "Don’t ego-check; Vayne wins by patience.",
                "After a bad death, play 3 minutes boring and stabilize.",
            ],
        },
    },
    "Jinx": {
        "identity": "Momentum & resets — first reset decides fights.",
        "win_condition": "Play safe until first reset → then take over with range + speed.",
        "mistakes": [
            "Standing too far forward pre-reset",
            "Swapping to minigun too early",
            "Overchasing instead of taking objectives",
        ],
        "focus": {
            "laning": [
                "Use rockets to farm/poke safely; don’t coinflip early.",
                "Play around support CC windows, not random trades.",
                "Reset on good timings — don’t stay for one more wave without vision.",
            ],
            "midgame": [
                "Your job is safe DPS and wave clear — don’t facecheck.",
                "Play fights where you have space (open lanes), not tight chokes.",
                "Use R to finish low targets or snipe objective fights.",
            ],
            "teamfights": [
                "Start rockets. First reset > everything.",
                "After reset, step forward and clean up — don’t drift sideways.",
                "If divers exist, position around peel and keep distance until threats show.",
            ],
            "consistency": [
                "If you’re not getting resets, you’re probably too far forward too early.",
                "Don’t chase kills across fog — take towers/objectives.",
                "Pick 1 rule: ‘No facecheck without vision’ and follow it every game.",
            ],
        },
    },
}

def supported_champions() -> List[str]:
    return list(_CHAMPIONS.keys())

def get_champion_plan(champ: str, struggle: str, goal: str) -> str:
    data = _CHAMPIONS[champ]
    struggle = struggle.lower()

    focus_lines = data["focus"].get(struggle, data["focus"]["consistency"])
    mistakes = "\n".join([f"- {m}" for m in data["mistakes"]])

    goal_line = ""
    if goal == "fast":
        goal_line = "\n**Fast climb note:** Spam comfort picks, avoid testing new champs in ranked, and keep your rules simple."
    else:
        goal_line = "\n**Long-term note:** Track your focus rule for 10 games and write one sentence after each match."

    return (
        f"**Identity:** {data['identity']}\n"
        f"**Win condition:** {data['win_condition']}\n\n"
        f"### Common mistakes to avoid\n{mistakes}\n\n"
        f"### Next 10 Games Focus ({champ} + {struggle})\n"
        + "\n".join([f"- {x}" for x in focus_lines])
        + goal_line
    )

