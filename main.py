from slack_bolt import App
from modals import USER_PORTAL, ADMIN_PORTAL, REMOVE_USER
from database import (USER_TABLE,
                      USER_INSERT,
                      SELECT_ALL_USERS,
                      REMOVE_SELECTED_USER,
                      TAKEDOWN_INSERT,
                      TAKEDOWNS_WEEKLY,
                      TAKEDOWNS_INSERT_SLACK,
                      TAKEDOWN_MEMBER_COUNT)
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


def generate_options(options):
    return [
        {"text": {"type": "plain_text", "text": option[0]}, "value": option[1]}
        for option in options
    ]

def takedown_availability(input):
    takedowns = [False] * 10
    takedowns_index = {
        'ML': 0,
        'MD': 1,
        'TL': 2,
        'TD': 3,
        'WL': 4,
        'WD': 5,
        'HL': 6,
        'HD': 7,
        'FL': 8,
        'FD': 9
    }
    for takedown in input:
        day = takedown['value']
        takedowns[takedowns_index[day]] = True
    return takedowns

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

@app.command("/admin-portal")
def admin_portal(body, ack, client, logger):
    """Admin Portal"""
    logger.info(body)
    ack()
    res = client.views_open(trigger_id=body["trigger_id"], view=ADMIN_PORTAL)
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
    takedowns = takedown_availability(availability)
    slack_id = body["user"]["id"]
    cursor.execute(USER_INSERT, (slack_id, name, membership))
    conn.commit()
    cursor.execute(TAKEDOWN_INSERT, (slack_id, *takedowns))
    conn.commit()

@app.view("admin-portal-modal")
def view_submission(ack, body, client, logger):
    ack()

@app.view("remove-user-modal")
def remove_user(ack, body, client, logger):
    ack()

# Modal Reponse Ack
@app.action("null-action")
def buttons(ack):
    ack()

#Display Remove Users Screen
@app.action("remove-user")
def remove_user_action(ack, body, client, logger):
    ack()
    logger.info(body)
    view_id = body['container']['view_id']
    cursor.execute(SELECT_ALL_USERS)
    modal = REMOVE_USER.copy()
    modal["blocks"][0]["accessory"]["options"] = generate_options((cursor.fetchall()))
    res = client.views_update(view_id=view_id, view=str(modal))
    slack_id = res['view']['blocks'][0]['accessory']['options'][0]['value']
    cursor.execute(REMOVE_SELECTED_USER, (slack_id,))
    conn.commit()

@app.action("insert-data")
def insert_data(ack, body, client, logger):
    ack()
    users = [('1','1', 'IH-2'),
             ('2','2', 'IH-2'),
             ('3','3', 'IH-2'),
             ('4','4', 'IH-2'),
             ('5','5', 'IH-2'),
             ('6','6', 'IH-2'),
             ('7','7', 'IH-2'),
             ('8','8', 'IH-2'),
             ('9','9', 'IH-2'),
             ('10','10', 'IH-2'),
             ('11','11', 'IH-2'),
             ('12','12', 'IH-2'),
             ('13','13', 'IH-2'),
             ('14','14', 'IH-2'),
             ('15','15', 'IH-2'),
             ('16','16', 'IH-2'),]
    takedowns = [('1', [True, False, True, False, True, False, True, False, False, False]),
                 ('2', [False, True, True, True, False, False, False, False, True, True]),
                 ('3', [True, False, False, False, False, False, False, True, False, False]),
                 ('4', [False, True, True, True, True, True, False, False, False, False]),
                 ('5', [True, False, True, False, True, False, True, False, True, False]),
                 ('6', [False, True, False, True, False, True, False, True, False, True]),
                 ('7', [True, False, False, False, False, False, False, False, False, False]),
                 ('8', [False, True, True, True, False, False, False, False, False, False]),
                 ('9', [False, False, False, False, True, True, True, False, False, False]),
                 ('10', [False, False, False, False, False, False, True, True, True, True]),
                 ('11', [True, False, True, False, True, False, False, False, False, True]),
                 ('12', [False, True, True, False, False, False, False, False, False, False]),
                 ('13', [False, True, False, True, False, True, False, True, True, True]),
                 ('14', [True, False, True, False, True, False, True, False, False, False]),
                 ('15', [False, True, False, False, True, False, False, False, False, False]),
                 ('16', [False, False, True, False, False, False, True, False, False, False]),
    ]
    for user in users:
        cursor.execute(USER_INSERT, user)
        conn.commit()
    for takedown in takedowns:
        cursor.execute(TAKEDOWN_INSERT, (takedown[0], *takedown[1]))
        conn.commit()

# Execute Takedown Generation
@app.action("generate-takedowns")
def generate_takedonws(ack, body, client, logger):
    ack()
    logger.info(body)
    view_id = body['container']['view_id']
    cursor.execute(TAKEDOWNS_WEEKLY)
    conn.commit()
    cursor.execute(TAKEDOWNS_INSERT_SLACK)
    conn.commit()
    cursor.execute(TAKEDOWN_MEMBER_COUNT)
    number_of_members = cursor.fetchone()[0]
    print(takedown_count)
    takedown_count = 0
    if number_of_members >= 11:
        takedown_count = 1
    elif number_of_members >= 21:
        takedown_count = 2
    print(takedown_count)



if __name__ == '__main__':
    conn = psycopg2.connect(database=os.getenv("PGDATABASE"),
                            host=os.getenv("PGHOST"),
                            user=os.getenv("POSTGRES_USER"),
                            password=os.getenv("POSTGRES_PASSWORD"),
                            port=os.getenv("PGPORT"))
    cursor = conn.cursor()
    cursor.execute(USER_TABLE)
    conn.commit()
    app.start(3000)