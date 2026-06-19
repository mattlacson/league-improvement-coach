from typing import Dict, List, Optional

# Coaching templates are grouped by ADC playstyle so adding more champions later is easy.
_FOCUS_TEMPLATES: Dict[str, Dict[str, List[str]]] = {
    "lane_bully": {
        "laning": [
            "Use your range/damage advantage to control the wave, not to take random all-ins.",
            "Trade when your support can follow or when enemy key cooldowns are down.",
            "Crash waves cleanly before recalling so you don’t throw your lane lead.",
        ],
        "midgame": [
            "Convert lane pressure into plates, dragons, and early rotations.",
            "Don’t wander alone just because you are ahead — protect your shutdown.",
            "Group when your pressure can help your team take an objective.",
        ],
        "teamfights": [
            "Start fights from max range and force enemies to walk into you.",
            "Track the one engage tool that can punish your forward positioning.",
            "Use your lead to hit safely, not to ego-frontline.",
        ],
        "consistency": [
            "A lead only matters if you keep it — avoid greedy deaths after winning lane.",
            "Reset after good plays instead of staying for one more wave with no vision.",
            "Play around cooldowns and wave state, not confidence alone.",
        ],
    },
    "poke_caster": {
        "laning": [
            "Use poke to create health leads before committing to trades.",
            "Keep enough mana/energy to escape or punish after poking.",
            "Don’t waste your main safety spell aggressively unless the fight is guaranteed.",
        ],
        "midgame": [
            "Set up around objectives early and poke before the fight starts.",
            "Play over walls and through chokes where your skillshots are harder to dodge.",
            "If your poke misses, reset the angle instead of forcing a bad fight.",
        ],
        "teamfights": [
            "Soften targets first, then commit only when someone is low or crowd controlled.",
            "Keep your escape tool available until major engage threats are used.",
            "Fight slowly — your value comes from repeated damage, not one desperate all-in.",
        ],
        "consistency": [
            "Missing poke is fine; dying after missing poke is the real mistake.",
            "Before stepping up, ask: who can instantly reach me?",
            "Take guaranteed damage windows instead of forcing highlight plays.",
        ],
    },
    "hypercarry": {
        "laning": [
            "Your first job is to leave lane playable — low deaths matter more than ego trades.",
            "Take short trades only when enemy cooldowns are down or your support creates space.",
            "Farm safely and avoid coinflip fights before your main item spikes.",
        ],
        "midgame": [
            "Catch safe waves and avoid walking into fog alone.",
            "Group for objectives only when you have space to deal damage.",
            "Do not trade your life for low-value kills — your scaling is worth more.",
        ],
        "teamfights": [
            "Hit the closest safe target until a better target walks into range.",
            "Wait for enemy engage tools before stepping forward.",
            "Once the fight is won, clean up — before that, survive first.",
        ],
        "consistency": [
            "If you are dying early, simplify the game: farm, scale, and stop forcing.",
            "Pick one threat before every fight and position around it.",
            "Your damage matters only if you are alive long enough to use it.",
        ],
    },
    "all_in": {
        "laning": [
            "Look for all-ins only when your support can follow and enemy cooldowns are missing.",
            "Avoid forcing before your champion has the damage or level spike to finish the fight.",
            "Short trades are okay, but don’t get baited into losing extended fights.",
        ],
        "midgame": [
            "Play around fog, flank angles, and teammates with crowd control.",
            "Don’t be the first person seen before an objective fight starts.",
            "Commit when the target is isolated or key defensive spells are down.",
        ],
        "teamfights": [
            "Wait for your entry window — going first usually gets you killed.",
            "Track exhaust, peel, and hard CC before using your dash/ultimate aggressively.",
            "Once you commit, finish the target quickly or reset the fight.",
        ],
        "consistency": [
            "Your champion rewards confidence, but only when the setup is real.",
            "If the fight requires three things to go perfectly, skip it.",
            "After a failed engage, stop chain-forcing and stabilize the next wave.",
        ],
    },
    "utility": {
        "laning": [
            "Use your utility to create safe trades instead of forcing pure damage checks.",
            "Track enemy engage range and keep the wave in a position you can play from.",
            "Punish mistakes with controlled trades, not panic all-ins.",
        ],
        "midgame": [
            "Set up vision and objective control before fighting.",
            "Use your utility to start or stop fights instead of chasing random kills.",
            "Rotate early so your team can play around your setup tools.",
        ],
        "teamfights": [
            "Play front-to-back and use your utility to control the fight pace.",
            "Save key tools for the biggest threat instead of using them instantly.",
            "If you can’t safely hit carries, hit the closest target and stay alive.",
        ],
        "consistency": [
            "You don’t need to carry every fight with damage — sometimes your setup wins it.",
            "Avoid low-value chases that remove your utility from the next objective.",
            "Before every fight, decide whether your job is engage, peel, or DPS.",
        ],
    },
    "self_peel": {
        "laning": [
            "Trade around your defensive tools and avoid fighting when they are down.",
            "Use wave control to force enemies into your best zone instead of chasing them.",
            "Don’t waste your escape/peel spell for minor damage.",
        ],
        "midgame": [
            "Take fights in areas where you can kite backward safely.",
            "Push waves before rotating so you don’t lose tempo for free.",
            "Stay near teammates who make your defensive tools harder to punish.",
        ],
        "teamfights": [
            "Let enemies come into you, then punish with your self-peel.",
            "Hold your defensive button for the real threat, not poke damage.",
            "Reposition after every cooldown cycle instead of standing still for DPS.",
        ],
        "consistency": [
            "Your safety tools are valuable because you save them — don’t spend them randomly.",
            "If you cannot name the engage threat, play farther back.",
            "Win through spacing and cooldown discipline, not panic reactions.",
        ],
    },
}

_CHAMPIONS: Dict[str, Dict[str, object]] = {
    "Aphelios": {
        "archetype": "hypercarry",
        "identity": "Weapon planning & controlled DPS — strongest when gun combos match the fight.",
        "win_condition": "Manage weapon rotations, reach item spikes, and take structured objective fights.",
        "rule": "Check your next weapon combo before major fights and don’t force with a weak setup.",
        "mistakes": [
            "Fighting without knowing your current and next gun combo",
            "Standing too far forward because you have strong damage",
            "Taking random skirmishes before item spikes",
        ],
    },
    "Ashe": {
        "archetype": "utility",
        "identity": "Utility & control — slows, vision, and engage setup.",
        "win_condition": "Control fights with vision, arrows, and consistent front-to-back damage.",
        "rule": "Use Hawkshot/positioning to prevent surprises, then arrow only when your team can follow.",
        "mistakes": [
            "Facechecking instead of using vision tools",
            "Using arrow with no follow-up plan",
            "Standing still while trying to apply slows",
        ],
    },
    "Caitlyn": {
        "archetype": "lane_bully",
        "identity": "Range & lane control — pressure through spacing, traps, and tower threat.",
        "win_condition": "Win lane through range, crash waves, take plates, and control objective entrances.",
        "rule": "Use your range to pressure safely; don’t trade your shutdown for one extra plate.",
        "mistakes": [
            "Overextending after pushing without tracking jungle",
            "Placing traps randomly instead of around CC/chokes",
            "Forcing short-range fights where your range advantage disappears",
        ],
    },
    "Corki": {
        "archetype": "poke_caster",
        "identity": "Spell-based marksman — poke, burst windows, and midgame tempo.",
        "win_condition": "Farm safely, poke before fights, and commit only when enemies are softened.",
        "rule": "Poke first, then fight — don’t start extended fights before landing damage.",
        "mistakes": [
            "Forcing fights before poke connects",
            "Walking into short-range threats to land damage",
            "Using mobility forward without a clear escape path",
        ],
    },
    "Draven": {
        "archetype": "lane_bully",
        "identity": "Snowball & pressure — early damage, axe control, and lane dominance.",
        "win_condition": "Build a lane lead, cash in safely, and protect your shutdown.",
        "rule": "Win through clean pressure, not reckless axe-chasing.",
        "mistakes": [
            "Chasing axes into bad positions",
            "Taking ego fights when support/jungle cannot help",
            "Throwing a lead by staying too long after a win",
        ],
    },
    "Ezreal": {
        "archetype": "poke_caster",
        "identity": "Skillshot poke & safety — consistent damage from difficult angles.",
        "win_condition": "Land poke, stay safe with mobility, and take fights after enemies are low.",
        "rule": "Your E is insurance; don’t spend it forward unless the play is guaranteed.",
        "mistakes": [
            "Using E aggressively with no vision or backup",
            "Missing poke then walking up anyway",
            "Playing too passively and giving up free pressure",
        ],
    },
    "Jhin": {
        "archetype": "utility",
        "identity": "Tempo & precision — burst windows, spacing, and pick setup.",
        "win_condition": "Control tempo and punish mistakes; avoid extended DPS fights.",
        "rule": "After every 4th shot or burst window, reposition immediately.",
        "mistakes": [
            "Using 4th shot aggressively with no escape plan",
            "Standing too close after your burst",
            "Ulting too early instead of using R to close or finish fights",
        ],
    },
    "Jinx": {
        "archetype": "hypercarry",
        "identity": "Momentum & resets — first reset decides fights.",
        "win_condition": "Play safe until first reset, then take over with range and movement speed.",
        "rule": "Survive until the first reset; before that, do not stand too far forward.",
        "mistakes": [
            "Standing too far forward pre-reset",
            "Swapping to minigun too early",
            "Overchasing instead of taking objectives",
        ],
    },
    "Kai'Sa": {
        "archetype": "all_in",
        "identity": "Dive & isolation — burst windows, target access, and follow-up engage.",
        "win_condition": "Farm to spikes, follow crowd control, and assassinate isolated targets.",
        "rule": "Only use R when the target is isolated or your team can follow instantly.",
        "mistakes": [
            "Ulting into the enemy team without backup",
            "Forcing fights before evolve/item spikes",
            "Diving past peel before key cooldowns are used",
        ],
    },
    "Kalista": {
        "archetype": "lane_bully",
        "identity": "Lane tempo & objective control — mobility, Rend pressure, and early skirmishes.",
        "win_condition": "Win early fights, control dragons, and snowball before scaling ADCs take over.",
        "rule": "Use mobility to space, not to hop deeper into danger.",
        "mistakes": [
            "Forcing fights without support coordination",
            "Overcommitting because Rend stacks look tempting",
            "Letting the game stall without converting early pressure",
        ],
    },
    "Kog'Maw": {
        "archetype": "hypercarry",
        "identity": "Protected DPS — huge damage if kept alive.",
        "win_condition": "Scale safely, position behind peel, and melt frontlines in extended fights.",
        "rule": "Stay inside your team’s protection; your range means nothing if you are isolated.",
        "mistakes": [
            "Walking past peel to hit a better target",
            "Fighting when W or support protection is unavailable",
            "Chasing kills instead of staying in a safe DPS zone",
        ],
    },
    "Lucian": {
        "archetype": "lane_bully",
        "identity": "Burst trades & tempo — short cooldown windows and lane pressure.",
        "win_condition": "Win short trades, spike early, and convert pressure before late-game carries outscale.",
        "rule": "Dash with a plan: damage window, escape path, and support follow-up.",
        "mistakes": [
            "Dashing forward without tracking enemy engage",
            "Taking extended fights after your burst is gone",
            "Failing to convert early pressure into objectives",
        ],
    },
    "Miss Fortune": {
        "archetype": "utility",
        "identity": "Lane poke & teamfight ultimates — strong setup and objective fights.",
        "win_condition": "Use lane pressure to reach fights where Bullet Time can control space.",
        "rule": "Ult from a safe angle after crowd control or when enemies are already committed.",
        "mistakes": [
            "Using ultimate where enemies can instantly cancel it",
            "Standing still too long before the fight starts",
            "Overchasing when objectives are free",
        ],
    },
    "Nilah": {
        "archetype": "all_in",
        "identity": "Short-range scaling skirmisher — explosive fights with support setup.",
        "win_condition": "Survive early range disadvantage, then win grouped all-ins and skirmishes.",
        "rule": "Wait for setup; Nilah is strong when entering second, not when facechecking first.",
        "mistakes": [
            "Forcing early fights into range advantage",
            "Going in before support or cooldown setup",
            "Taking fights in open space where you get kited",
        ],
    },
    "Samira": {
        "archetype": "all_in",
        "identity": "Reset all-in carry — style stacks, cleanup, and snowball fights.",
        "win_condition": "Wait for crowd control, enter at the right time, and clean up with resets.",
        "rule": "Do not go first; enter after CC lands or enemy peel is used.",
        "mistakes": [
            "Dashing in before style/setup is ready",
            "Using W too early instead of blocking key spells",
            "Trying to 1v5 before enemies spend crowd control",
        ],
    },
    "Senna": {
        "archetype": "utility",
        "identity": "Scaling utility marksman — range, souls, poke, and global support.",
        "win_condition": "Scale through safe trades, collect souls without greed, and control fights from range.",
        "rule": "Collect souls only when it is safe; one greedy soul is not worth a death.",
        "mistakes": [
            "Walking into danger for souls",
            "Playing like a short-range DPS carry instead of a utility marksman",
            "Using root or ultimate without checking teammate follow-up",
        ],
    },
    "Sivir": {
        "archetype": "utility",
        "identity": "Waveclear & team tempo — safe scaling, spell shield, and engage speed.",
        "win_condition": "Clear waves, survive lane, and use ultimate to start or escape fights.",
        "rule": "Save spell shield for meaningful threats, not random poke.",
        "mistakes": [
            "Wasting spell shield before engage tools are used",
            "Standing too close despite having short range",
            "Using ultimate without a clear team decision",
        ],
    },
    "Smolder": {
        "archetype": "poke_caster",
        "identity": "Scaling spell marksman — stacks, poke, and late-game execution.",
        "win_condition": "Stack safely, avoid early deaths, and scale into objective fights.",
        "rule": "Do not die for stacks; consistent farming beats greedy stacking.",
        "mistakes": [
            "Trading health/life just to stack",
            "Fighting before meaningful scaling breakpoints",
            "Walking into fog to chase low-health targets",
        ],
    },
    "Tristana": {
        "archetype": "all_in",
        "identity": "Jump resets & tower pressure — explosive trades and objective snowballing.",
        "win_condition": "Punish cooldowns with all-ins, take towers quickly, and reset through fights.",
        "rule": "Jump in only when you know how you get out: kill reset, buffer, or teammate cover.",
        "mistakes": [
            "Jumping in without a reset path",
            "Forcing all-ins into bad wave states",
            "Using ultimate randomly instead of peeling or finishing",
        ],
    },
    "Twitch": {
        "archetype": "hypercarry",
        "identity": "Stealth tempo & ambush DPS — surprise angles and late-fight cleanup.",
        "win_condition": "Find safe flank timers, open after threats show, and shred grouped enemies.",
        "rule": "Open from stealth only when the fight is ready or the target cannot punish you.",
        "mistakes": [
            "Opening too early before teammates can follow",
            "Flanking through unwarded danger with no exit",
            "Chasing kills across fog instead of taking objectives",
        ],
    },
    "Varus": {
        "archetype": "poke_caster",
        "identity": "Poke, pick, and lane pressure — flexible damage with strong engage threat.",
        "win_condition": "Control space with poke and ultimate, then punish rooted or low-health targets.",
        "rule": "Use poke to create pressure first; use ultimate when your team can collapse.",
        "mistakes": [
            "Standing too close despite being immobile",
            "Using ultimate with no follow-up",
            "Forcing fights before landing poke or applying pressure",
        ],
    },
    "Vayne": {
        "archetype": "hypercarry",
        "identity": "Patience & punishment — survive early, take over later.",
        "win_condition": "Low-death lane, scale, slow fights, and punish overcommitment.",
        "rule": "Do not ego-check early; Vayne wins through patience and clean spacing.",
        "mistakes": [
            "Forcing trades early before spikes",
            "Using Q aggressively with no safety plan",
            "Using Condemn offensively when you need it for self-peel",
        ],
    },
    "Xayah": {
        "archetype": "self_peel",
        "identity": "Feather control & self-peel — punishes enemies who run into her zone.",
        "win_condition": "Control space with feathers, survive engage, and turn fights with root/ultimate.",
        "rule": "Let enemies enter your feathers; don’t chase fights away from your setup.",
        "mistakes": [
            "Using ultimate aggressively instead of saving it for danger",
            "Fighting away from feather setups",
            "Standing too close before enemy engage tools are used",
        ],
    },
    "Yunara": {
        "archetype": "hypercarry",
        "identity": "Classic marksman spacing — consistent autos, clean kiting, and disciplined positioning.",
        "win_condition": "Scale into fights, maintain spacing, and win through steady DPS instead of forced dives.",
        "rule": "Play like a traditional ADC: stay alive, kite backward, and deal damage over time.",
        "mistakes": [
            "Standing too far forward before the fight is committed",
            "Chasing instead of maintaining a safe DPS line",
            "Forcing trades without support or cooldown advantage",
        ],
    },
    "Zeri": {
        "archetype": "hypercarry",
        "identity": "Kiting & extended fights — mobility, spacing, and ramping damage.",
        "win_condition": "Survive the start of fights, use terrain well, and kite long enough to take over.",
        "rule": "Use mobility to maintain space, not to dash into the enemy team.",
        "mistakes": [
            "Using E forward with no escape plan",
            "Overchasing after getting movement speed",
            "Fighting in areas where you cannot use terrain safely",
        ],
    },
}


def _key(name: str) -> str:
    return "".join(ch for ch in name.lower() if ch.isalnum())


_ALIASES: Dict[str, str] = {}
for _champion_name in _CHAMPIONS:
    _ALIASES[_key(_champion_name)] = _champion_name

_ALIASES.update({
    "kaisa": "Kai'Sa",
    "kaisai": "Kai'Sa",
    "kogmaw": "Kog'Maw",
    "kog": "Kog'Maw",
    "mf": "Miss Fortune",
    "missfortune": "Miss Fortune",
    "aphel": "Aphelios",
    "aph": "Aphelios",
    "cait": "Caitlyn",
    "trist": "Tristana",
    "twitchadc": "Twitch",
})


def normalize_champion_name(champ: str) -> Optional[str]:
    """Return the canonical champion name, or None if it is unsupported."""
    return _ALIASES.get(_key(champ))


def supported_champions() -> List[str]:
    return list(_CHAMPIONS.keys())


def get_champion_quick_tip(champ: str) -> str:
    canonical = normalize_champion_name(champ)
    if not canonical:
        return "Reminder: staying alive is almost always more valuable than forcing damage."

    data = _CHAMPIONS[canonical]
    return f"{canonical} reminder: {data['rule']}"


def get_champion_plan(champ: str, struggle: str, goal: str) -> str:
    canonical = normalize_champion_name(champ)
    if not canonical:
        raise KeyError(f"Unsupported champion: {champ}")

    data = _CHAMPIONS[canonical]
    struggle = struggle.lower()
    template = _FOCUS_TEMPLATES[str(data["archetype"])]

    focus_lines = template.get(struggle, template["consistency"])
    mistakes = "\n".join([f"- {m}" for m in data["mistakes"]])

    if goal == "fast":
        goal_line = "\n**Fast climb note:** Spam comfort picks, avoid testing new champs in ranked, and keep your rules simple."
    else:
        goal_line = "\n**Long-term note:** Track your focus rule for 10 games and write one sentence after each match."

    return (
        f"**Identity:** {data['identity']}\n"
        f"**Win condition:** {data['win_condition']}\n"
        f"**Main rule:** {data['rule']}\n\n"
        f"### Common mistakes to avoid\n{mistakes}\n\n"
        f"### Next 10 Games Focus ({canonical} + {struggle})\n"
        + "\n".join([f"- {x}" for x in focus_lines])
        + goal_line
    )
