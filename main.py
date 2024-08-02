from slack_bolt import App
import os, logging, slack, ssl, psycopg2
from slackeventsapi import SlackEventAdapter

logging.basicConfig(level=logging.DEBUG)

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

app = App(
    token = slack.WebClient(token=os.getenv('SLACK_BOT_TOKEN'), ssl=ssl_context)
    signing_secret = SlackEventAdapter(os.getenv('SLACK_SIGNING_SECRET'),'/slack/events', app)
)


HELP_MESSAGE= '''
THIS IS A TEST!
'''

VIEW = '''
{
	"type": "modal",
    "callback_id": "view-modal",
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": true
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": true
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": true
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Name",
				"emoji": true
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Section block with radio buttons"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 2",
							"emoji": true
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 3",
							"emoji": true
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Townsman",
							"emoji": true
						},
						"value": "value-2"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Cancel"
					},
					"style": "danger",
					"value": "click_me_123"
				}
			]
		}
	]
}
'''


USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    slack_id VARCHAR(255),
    name VARCHAR(255),
    membership VARCHAR(255)
    );
"""

@app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    next()


@app.command('/help')
def helpform(body, ack, client, logger):
    """Help Slack Command"""
    logger.info(body)
    ack()
    res = client.views_open(trigger_id=body["trigger_id"], view=VIEW)
    #client.chat_postEphemeral(channel=channel_id, user=user_id, text=HELP_MESSAGE)
    logger.info(res)

@app.view("view-modal")
def view_submission(ack, body, client, logger):
    ack()
    logger.info(body["view"]["state"]["values"])
    # Extra Credit: Uncomment out this section
    # thank_you_channel = "your_channel_id"
    # user_text = body["view"]["state"]["values"]["my_block"]["my_action"]["value"]
    # client.chat_postMessage(channel=thank_you_channel, text=user_text)

if __name__ == '__main__':
    conn = psycopg2.connect(database=os.getenv("PGDATABASE"),
                        host=os.getenv("PGHOST"),
                        user=os.getenv("POSTGRES_USER"),
                        password=os.getenv("POSTGRES_PASSWORD"),
                        port=os.getenv("PGPORT"))
    cursor = conn.cursor()
    cursor.execute(USER_TABLE)
    conn.commit()
    #print(cursor.fetchall())
    app.run(debug=True, host='0.0.0.0', port=os.getenv("PORT", default=8080))