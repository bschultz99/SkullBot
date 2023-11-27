from flask import Flask, jsonify, request, Response
import os
from slackeventsapi import SlackEventAdapter
import slack
import ssl
import requests

app = Flask(__name__)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],'/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'], ssl=ssl_context)

@app.route('/index')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/help', methods=['POST'])
def helpform():
    """Help Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    HELP_MESSAGE = """Welcome to the ThetaBot. These are the following features:
1. /help - Gives information on how the slack commands work.
2. /user-form - Fill this out to update your name, membership, and takedown availability.
3. /cleanup-settings - ADMIN - Change cleanups settings i.e. membership, minimum people, etc.
4. /removeuser - ADMIN - Remove a user from the user, cleanups, and takedown database.
5. /generate-cleanup-database - ADMIN - Generate the cleanup database by adding the cleanups and setting default values to 0.
6. /generate-cleanups - ADMIN - Generates the weekly cleanups.
7. /generate-takedowns - ADMIN - Generates the weekly takedowns.
8. /display-takedowns - Display the takedown database.
9. /display-cleanups - Display the cleanups database.
10. /admin-form - ADMIN - Add admins to the system.
11. /fines-form - ADMIN- Submit fines for members.
12. /reconcilliation-form - ADMIN - Use to reconcille fines of members.
13. /display-fines - Display the fines database.
14. /display-reconcilliation - Display the reconcilliation Database.
15. /display-naughtylist - Displays the fines, reconcilliations, and how much members owe.
16. /end-semester - ADMIN - Restarts the semester.
"""
    client.chat_postEphemeral(channel=channel_id, user=user_id, text=HELP_MESSAGE)
    return Response(), 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))