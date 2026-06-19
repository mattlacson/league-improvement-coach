from flask import Flask, render_template, request, session, redirect, url_for

from coach import (
    PlayerProfile,
    generate_plan,
    diagnose,
    review_rules,
    micro_drill,
    champ_review_tip,
)
from champions import supported_champions


app = Flask(__name__)

# Needed so Flask can remember the last generated plan during the session.
# This is okay for local development.
app.secret_key = "dev-secret-key"


def clean_output(text: str) -> str:
    """
    Cleans simple markdown-style formatting from the CLI output
    so it looks better on the web page.
    """
    if not text:
        return ""

    return (
        text.replace("**", "")
            .replace("### ", "")
            .replace("`", "")
    )


@app.route("/", methods=["GET", "POST"])
def index():
    plan = None
    profile_data = None

    if request.method == "POST":
        rank = request.form.get("rank", "").strip().title()
        role = request.form.get("role", "ADC").strip().upper()
        champions_raw = request.form.get("champions", "").strip()
        focus_champ = request.form.get("focus_champ", "").strip().title()
        struggle = request.form.get("struggle", "consistency").strip().lower()
        goal = request.form.get("goal", "fast").strip().lower()

        champions = [
            champ.strip().title()
            for champ in champions_raw.split(",")
            if champ.strip()
        ]

        profile = PlayerProfile(
            rank=rank,
            role=role,
            champions=champions,
            focus_champ=focus_champ,
            struggle=struggle,
            goal=goal,
        )

        plan = clean_output(generate_plan(profile))

        profile_data = {
            "rank": rank,
            "role": role,
            "champions": champions_raw,
            "focus_champ": focus_champ,
            "struggle": struggle,
            "goal": goal,
        }

        session["last_plan"] = plan
        session["profile_data"] = profile_data

    else:
        plan = session.get("last_plan")
        profile_data = session.get("profile_data")

    return render_template(
        "index.html",
        plan=plan,
        review=None,
        profile_data=profile_data,
        supported_champs=supported_champions(),
    )


@app.route("/review", methods=["POST"])
def review():
    champ = request.form.get("review_champ", "").strip().title()
    phase = request.form.get("phase", "laning").strip().lower()
    death = request.form.get("death", "other").strip().lower()
    emotion = request.form.get("emotion", "calm").strip().lower()
    one_good = request.form.get("one_good", "").strip()
    one_fix = request.form.get("one_fix", "").strip()

    diagnosis = diagnose(death, phase, emotion)
    rules = review_rules(death, phase)
    drill = micro_drill(phase)
    champ_tip = champ_review_tip(champ)

    tilt_line = ""
    if emotion in ("frustrated", "tilted", "tired"):
        tilt_line = (
            "\n\nHonest note: This game sounded mentally draining. "
            "If you are not feeling reset, take a short break before queueing again."
        )

    review_result = (
        f"Champion: {champ}\n"
        f"Problem phase: {phase}\n"
        f"First death cause: {death}\n"
        f"Mental state: {emotion}\n\n"
        f"Diagnosis: {diagnosis}\n\n"
        f"Your rule for next game: {rules[0]}\n\n"
        f"Fix plan:\n"
        f"- {rules[0]}\n"
        f"- {rules[1]}\n"
        f"- {rules[2]}\n\n"
        f"{drill}\n"
        f"{champ_tip}\n\n"
        f"You did well: {one_good or '—'}\n"
        f"Next improvement: {one_fix or '—'}"
        f"{tilt_line}"
    )

    return render_template(
        "index.html",
        plan=session.get("last_plan"),
        review=clean_output(review_result),
        profile_data=session.get("profile_data"),
        supported_champs=supported_champions(),
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
