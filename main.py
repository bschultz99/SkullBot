from flask import Flask, request, Response
import os
from slackeventsapi import SlackEventAdapter
import slack
import ssl
import psycopg2

app = Flask(__name__)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
slack_event_adapter = SlackEventAdapter(os.getenv('SLACK_SIGNING_SECRET'),'/slack/events', app)
client = slack.WebClient(token=os.getenv('SLACK_BOT_TOKEN'), ssl=ssl_context)

HELP_MESSAGE= '''
THIS IS A TEST!
'''


@app.route('/help', methods=['POST'])
def helpform():
    """Help Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text=HELP_MESSAGE)
    return Response(), 200


if __name__ == '__main__':
    conn = psycopg2.connect(database=os.getenv("PGDATABASE"),
                        host=os.getenv("PGHOST"),
                        user=os.getenv("POSTGRES_USER"),
                        password=os.getenv("POSTGRES_PASSWORD"),
                        port=os.getenv("PGPORT"))
    #cursor = conn.cursor()
    #cursor.execute("ALTER TABLE users RENAME COLUMN first_name to name;")
    #print(cursor.fetchall())
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=8080))