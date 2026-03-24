# Auto Deploy Webhook 🚀

## Overview

A system that automatically updates a local repository when changes are pushed to GitHub using webhooks.

---

## Phase 1: Understanding Webhooks

* Learned how GitHub sends POST requests on code changes
* Understood event-driven automation

---

## Phase 2: Webhook Receiver

* Built a Flask server to receive webhook requests
* Created `/webhook` endpoint
* Verified using curl

---

## How to Run

```bash
python app.py
```

Test:

```bash
curl -X POST http://localhost:5000/webhook
```
