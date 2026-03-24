# Auto Deploy Webhook 🚀
# Auto Deploy Webhook 🚀

## Overview

Auto Deploy Webhook is a real-time automation system that updates a local repository whenever changes are pushed to GitHub.

It uses webhooks to trigger a Flask server, which then executes a `git pull` to keep the system in sync automatically.

---

## Features

* Real-time GitHub webhook integration
* Automated `git pull` execution
* Flask-based webhook receiver
* Event-driven architecture
* Local-to-public tunneling using ngrok

---

## Tech Stack

* Python
* Flask
* Git
* ngrok

---

## Architecture

```text
GitHub Push
     ↓
Webhook (POST request)
     ↓
Flask Server (/webhook)
     ↓
subprocess → git pull
     ↓
Local repository updated
```

---

## Project Phases

### Phase 1: Webhook Fundamentals

* Understood event-driven triggers
* Learned GitHub webhook behavior

### Phase 2: Webhook Receiver

* Built Flask server
* Created `/webhook` endpoint
* Tested using curl

### Phase 3: Automation

* Integrated subprocess
* Executed `git pull` on trigger

### Phase 4: Real Integration

* Exposed local server using ngrok
* Connected GitHub webhook
* Achieved real-time auto deployment

---

## How to Run

### Start Flask Server

```bash
python app.py
```

### Start ngrok

```bash
ngrok http 5000
```

### Configure GitHub Webhook

* URL: `https://<ngrok-url>/webhook`
* Method: POST

---

## Example Output

```text
Webhook received! Pulling latest changes...
Already up to date.
```

---

## Key Learnings

* Webhook-based event systems
* HTTP request handling
* Automation using subprocess
* Real-time deployment concepts

---

## Future Improvements

* Add webhook security (secret validation)
* Dockerize the service
* Add logging system
* Deploy on cloud server

---
