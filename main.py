from flask import Flask
import os
from slackeventsapi import SlackEventAdapter
import slack
import ssl
import psycopg2

app = Flask(__name__)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
#slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],'/slack/events', app)
#client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'], ssl=ssl_context)

if __name__ == '__main__':
    #conn = psycopg2.connect(database=os.getenv("PGDATABASE"),
                        #host=os.getenv("PGHOST"),
                        #user=os.getenv("POSTGRES_USER"),
                        #password=os.getenv("POSTGRES_PASSWORD"),
                        #port=os.getenv("PGPORT"))
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM admin")
    #print(cursor.fetchall())
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=5000))