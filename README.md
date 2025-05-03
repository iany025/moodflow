# MoodFlow

MoodFlow is a lightweight, mood-based suggestion web app that helps users find healthy, uplifting, or calming activities based on how they're feeling. Whether you're bored, anxious, grateful, or curious, MoodFlow offers personalized prompts to support mental wellness.

Live app: [https://moodflow.onrender.com](https://moodflow.onrender.com)

Features
- 13 Moods Supported — From happy to overwhelmed to grateful, each mood offers 10 randomized, actionable suggestions.
-  Favorites System — Save any suggestion you like and revisit it later.
-  Suggestion History — See the last 5 activities you've received.
-  Clear Options — Instantly clear your history or favorites with confirmation.
-  Dark/Light Mode Toggle — Easy visual switching via localStorage.
-  Emoji-Enhanced Mood Display — Makes suggestions more fun and intuitive.
-  Fast and Responsive UI — Built using Flask, Jinja2, HTML/CSS, and JavaScript.

File Structure

moodflow/
├── app.py               # Main Flask application
├── moods.py             # Dictionary of mood-based suggestions + emojis
├── templates/
│   └── index.html       # Main HTML page using Jinja templating
├── static/
│   └── style.css        # Custom CSS for light/dark mode and layout
├── requirements.txt     # Python dependencies for deployment
├── Procfile             # Specifies how to run app in production (Render)


Created as a personal programming project for CS2104. Inspired by mental wellness design tools and micro self-care apps.
