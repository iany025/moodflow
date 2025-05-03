from flask import Flask, render_template, request, session, redirect, url_for
import random
from moods import mood_suggestions, mood_emojis
app = Flask(__name__)
app.secret_key = 'moodflow-secret'
@app.route("/", methods=["GET", "POST"])
def index():
    suggestion = None
    selected_mood = None
    emoji = None
 
    if request.method == "POST": 
        selected_mood = request.form.get("mood")
        if selected_mood in mood_suggestions:
            suggestion = random.choice(mood_suggestions[selected_mood])
            emoji = mood_emojis.get(selected_mood, "")

            history = session.get("history", [])
            history.append((selected_mood, suggestion))
            session["history"] = history

    return render_template("index.html", suggestion=suggestion, selected_mood=selected_mood, emoji=emoji, mood_suggestions=mood_suggestions)
@app.route("/favorite", methods=["POST"])
def favorite():
    mood = request.form.get("mood")
    suggestion = request.form.get("suggestion")
    favorites = session.get("favorites", [])
    if (mood, suggestion) not in favorites:
        favorites.append((mood, suggestion))
        session["favorites"] = favorites
    return redirect(url_for("index"))
@app.route("/clear_history")
def clear_history():
    session.pop("history", None)
    return redirect(url_for("index"))
@app.route("/clear_favorites")
def clear_favorites():
    session.pop("favorites", None)
    return redirect(url_for("index"))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)