from flask import Flask, jsonify, request, Response
import os
from slackeventsapi import SlackEventAdapter
from templates import *
import slack
import ssl
import requests
import json
import psycopg2

app = Flask(__name__)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],'/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'], ssl=ssl_context)

@app.route('/help', methods=['POST'])
def helpform():
    """Help Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text=HELP_MESSAGE)
    return Response(), 200

@app.route('/userform', methods=['POST'])
def userform():
    """Userform Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    user_name = client.users_info(user=user_id)['user']['real_name']
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=user_portal(user_name))
    return Response(), 200

@app.route('/adminform', methods=['POST'])
def adminform():
    """Adminform Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    user_name = client.users_info(user=user_id)['user']['real_name']
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=admin_portal(user_name))
    return Response(), 200


@app.route('/interactions', methods=['POST'])
def interactions():
    data = json.loads(request.form.get("payload"))
    user_id = data["user"]["id"]
    channel_id = data["container"]["channel_id"]
    reponse_url = data["response_url"]
    action = data["actions"][0]["action_id"]
    if action == "update_user_profile":
        client.chat_postEphemeral(reponse_url=reponse_url, channel=channel_id, user=user_id, blocks=USER_FORM)
    return Response(), 200

if __name__ == '__main__':
    conn = psycopg2.connect(database=os.getenv("DATABASE_PRIVATE_URL"),
                        host=os.getenv("PGHOST"),
                        user=os.getenv("POSTGRES_USER"),
                        password=os.getenv("POSTGRES_PASSWORD"),
                        port=os.getenv("PGPORT"))
    print(os.environ)
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))