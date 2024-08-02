from slack_bolt import App
from modals import USER_PORTAL
import os, logging, psycopg2

logging.basicConfig(level=logging.DEBUG)


app = App(
    token = os.getenv('SLACK_BOT_TOKEN'),
    signing_secret = os.getenv('SLACK_SIGNING_SECRET'),
)

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


@app.command("/skull-help")
def helpform(body, ack, client, logger):
    """Help Slack Command"""
    logger.info(body)
    ack()
    res = client.views_open(trigger_id=body["trigger_id"], view=USER_PORTAL)
    logger.info(res)

@app.command("/user-portal")
def user_portal(body, ack, client, logger):
    """User Portal"""
    logger.info(body)
    ack()
    res = client.views_open(trigger_id=body["trigger_id"], view=USER_PORTAL)
    logger.info(res)

@app.view("user-portal-modal")
def view_submission(ack, body, client, logger):
    ack()
    logger.info(body["view"]["state"]["values"])
    # Extra Credit: Uncomment out this section
    # thank_you_channel = "your_channel_id"
    # user_text = body["view"]["state"]["values"]["my_block"]["my_action"]["value"]
    # client.chat_postMessage(channel=thank_you_channel, text=user_text)

@app.action("radio_buttons-action")
def buttons(ack, body, client, logger):
    ack()


@app.action("plain_text_input-action")
def plain_text(ack):
    ack()

@app.action("static_select-action")
def static_select(ack):
    ack()

@app.action("checkboxes-action")
def checkbox(ack):
    ack()

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
    app.start(3000)