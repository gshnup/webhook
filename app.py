from flask import Flask, request
import subprocess

app = Flask(__name__)

REPO_PATH = "/root/projects/watchdawg"   # ⚠️ your repo path

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook received! Pulling latest changes...")

    result = subprocess.run(
        ["git", "-C", REPO_PATH, "pull"],
        capture_output=True,
        text=True
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    return "Updated", 200


if __name__ == '__main__':
    app.run(port=5000)
