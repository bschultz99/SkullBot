from slack_bolt import App
from modals import USER_PORTAL
from database import USER_TABLE
import os, logging, psycopg2

logging.basicConfig(level=logging.DEBUG)

app = App(
    token = os.getenv('SLACK_BOT_TOKEN'),
    signing_secret = os.getenv('SLACK_SIGNING_SECRET'),
)

#@app.middleware
#def log_request(logger, body, next):
   # logger.debug(body)
   # next()

# Commands
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

# Modal View
@app.view("user-portal-modal")
def view_submission(ack, body, client, logger):
    ack()
    data = body["view"]["state"]["values"]
    input_keys = list(data)
    name = data[input_keys[0]]["null-action"]["value"]
    membership = data[input_keys[1]]["null-action"]["selected_option"]["value"]
    availability = data[input_keys[2]]["null-action"]["selected_options"]
    print(f"Name: {name}")
    print(f"Name: {membership}")
    print(f"Name: {availability}")


# Modal Reponse Ack
@app.action("null-action")
def buttons(ack):
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