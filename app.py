from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Himanshu Chhokar",
    "role": "B.Tech CSE Student & Aspiring Software Engineer",
    "college": "Shri Vishwakarma Skill University, Palwal",
    "skills": ["Python", "Django REST Framework", "React.js", "JavaScript", "Git/GitHub", "Docker"],
    "github": "https://github.com/",
    "linkedin": "https://linkedin.com/",
}


@app.route("/")
def home():
    """Main page — renders the profile card."""
    return render_template("index.html", profile=PROFILE, year=datetime.now().year)


@app.route("/about")
def about():
    """A second page, to show basic routing inside the container."""
    return render_template("about.html")


@app.route("/api/status")
def status():
    """Health-check endpoint — useful for verifying the container is alive."""
    return jsonify({
        "status": "running",
        "message": "Task 1 - Dockerized Web Application is live!",
        "timestamp": datetime.utcnow().isoformat(),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
