from slack_bolt import App
from slack_sdk.errors import SlackApiError
import os, logging, psycopg2
import pandas as pd
from modals import USER_PORTAL, ADMIN_PORTAL, REMOVE_USER, ADD_ADMIN_USER
from database import (USER_TABLE,
                      USER_INSERT,
                      SELECT_ALL_USERS,
                      REMOVE_SELECTED_USER,
                      TAKEDOWN_INSERT,
                      TAKEDOWNS_WEEKLY,
                      TAKEDOWN_MEMBER_COUNT,
                      TAKEDOWNS_SUM_COUNT,
                      TAKEDOWNS_ACTIVE_SELECT,
                      TAKEDOWNS_UPDATE_ASSIGNMENT,
                      TAKEDOWNS_ALL_SELECT,
                      TAKEDOWN_DISPLAY,
                      TAKEDOWNS_CHANNEL_INSERT,
                      TAKEDOWNS_SELECT_MEMBERS,
                      POSITIONS_SLACK_INSERT,
                      THETA_THREE_SELECT,
                      ADMIN_CHECK)

logging.basicConfig(level=logging.DEBUG)

app = App(
    token = os.getenv('SLACK_BOT_TOKEN'),
    signing_secret = os.getenv('SLACK_SIGNING_SECRET'),
)

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
    ack()
    logger.info(body)
    user_id = body['user_id']
    cursor.execute(ADMIN_CHECK, (user_id,))
    count = cursor.fetchone()[0]
    if count > 0:
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
    for _, value in body['view']['state']['values'].items():
        if 'null-action' in value:
            slack_id = value['null-action']['selected_option']['value']
    cursor.execute(REMOVE_SELECTED_USER, (slack_id,))
    conn.commit()

@app.view("add-admin-modal")
def add_admin_modal(ack, body, client, logger):
    ack()
    values = ()
    for _, value in body['view']['state']['values'].items():
        if 'null-action' in value:
            values += ((value['null-action']['selected_option']['value']),)
    cursor.execute(POSITIONS_SLACK_INSERT, values)
    conn.commit()

# Modal Response Ack
@app.action("null-action")
def buttons(ack):
    ack()

@app.action("add-admin")
def add_admin(ack, body, client, logger):
    ack()
    logger.info(body)
    view_id = body['container']['view_id']
    modal = ADD_ADMIN_USER.copy()
    cursor.execute(SELECT_ALL_USERS)
    modal["blocks"][0]["accessory"]["options"] = generate_options((cursor.fetchall()))
    client.views_update(view_id=view_id, view=str(modal))

#Display Remove Users Screen
@app.action("remove-user")
def remove_user_action(ack, body, client, logger):
    ack()
    logger.info(body)
    view_id = body['container']['view_id']
    cursor.execute(SELECT_ALL_USERS)
    modal = REMOVE_USER.copy()
    modal["blocks"][0]["accessory"]["options"] = generate_options((cursor.fetchall()))
    client.views_update(view_id=view_id, view=str(modal))

@app.action("insert-data")
def insert_data(ack, body, client, logger):
    ack()
    users = [('1','1', 'IH-2'),
             ('2','2', 'IH-2'),
             ('3','3', 'IH-3'),
             ('4','4', 'IH-2'),
             ('5','5', 'IH-3'),
             ('6','6', 'IH-2'),
             ('7','7', 'IH-3'),
             ('8','8', 'IH-3'),
             ('9','9', 'IH-3'),
             ('10','10', 'IH-3'),
             ('11','11', 'IH-3'),
             ('12','12', 'NM'),
             ('13','13', 'NM'),
             ('14','14', 'TM'),
             ('15','15', 'TM'),
             ('16','16', 'NM'),]
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
def generate_takedowns(ack, body, client, logger):
    ack()
    logger.info(body)
    view_id = body['container']['view_id']
    cursor.execute(TAKEDOWNS_WEEKLY)
    conn.commit()
    cursor.execute(TAKEDOWN_MEMBER_COUNT)
    number_of_members = cursor.fetchone()[0]
    takedown_count = 0
    if number_of_members >= 11:
        takedown_count = 1
    elif number_of_members >= 21:
        takedown_count = 2
    cursor.execute(TAKEDOWNS_SUM_COUNT)
    sums = cursor.fetchone()
    takedowns_sums = {
        'monday_lunch': [sums[0], 0],
        'monday_dinner': [sums[1], 0],
        'tuesday_lunch': [sums[2], 0],
        'tuesday_dinner': [sums[3], 0],
        'wednesday_lunch': [sums[4], 0],
        'wednesday_dinner': [sums[5], 0],
        'thursday_lunch': [sums[6], 0],
        'thursday_dinner': [sums[7], 0],
        'friday_lunch': [sums[8], 0],
        'friday_dinner': [sums[9], 0]
    }
    for _ in range(10):
        min_key = min((key for key in takedowns_sums if takedowns_sums[key][1] == 0), key=lambda k: takedowns_sums[k][0])
        takedowns_sums[min_key][1] += 1
        cursor.execute(TAKEDOWNS_ACTIVE_SELECT.format(min_key))
        person = cursor.fetchone()
        cursor.execute(TAKEDOWNS_UPDATE_ASSIGNMENT, (person[0], min_key, min_key, person[0]))
        conn.commit()
    for x in range(takedown_count):
        for _ in range(10):
            min_key = min((key for key in takedowns_sums if takedowns_sums[key][1] == x+1), key=lambda k: takedowns_sums[k][0])
            takedowns_sums[min_key][1] += 1
            cursor.execute(TAKEDOWNS_ALL_SELECT.format(min_key))
            person = cursor.fetchone()
            cursor.execute(TAKEDOWNS_UPDATE_ASSIGNMENT, (person[0], min_key, min_key, person[0]))
            conn.commit()
    df = pd.read_sql_query(TAKEDOWN_DISPLAY, conn)
    df.to_csv('weekly_takedowns.csv', index=False)
    client.files_upload_v2(
        channel="C0684CN6V6U",
        file="weekly_takedowns.csv",
        title="Takedowns",
        initial_comment="Here are the assignments for this weeks takedowns:",
    )
    takedown_channels = {
        'monday_lunch': 'C05NUTE6HC4',
        'monday_dinner': 'C05P53KDX7B',
        'tuesday_lunch': 'C05NKQWH3HC',
        'tuesday_dinner': 'C05NKQWK7EJ',
        'wednesday_lunch': 'C05NKQWMEGN',
        'wednesday_dinner': 'C05NPGXSZL5',
        'thursday_lunch': 'C05P53KQTUH',
        'thursday_dinner': 'C05NKQWTQA2',
        'friday_lunch': 'C05PG5PPS2C',
        'friday_dinner': 'C05NSBGBHT5' 
    }
    cursor.execute(THETA_THREE_SELECT)
    theta_three = cursor.fetchone()[0]
    for takedown_slot, channel_id in takedown_channels.items():
        cursor.execute(TAKEDOWNS_CHANNEL_INSERT, (takedown_slot, channel_id))
        conn.commit()
        resp = client.conversations_members(channel = channel_id)
        for member in resp['members']:
            if member == 'U067TRDET4Z' or member == 'UCQMZA62E' or member == theta_three:
                print(member)
            else:
                client.conversations_kick(channel= channel_id, user=member)
        cursor.execute(TAKEDOWNS_SELECT_MEMBERS, (f"%{takedown_slot}%",))
        members = cursor.fetchall()
        for member in members:
            try:
                client.conversations_invite(channel = channel_id, users=member)
            except SlackApiError as e:
                print(e)
        try:
            client.conversations_invite(channel = channel_id, users=theta_three)
        except SlackApiError as e:
                print(e)
        client.chat_postMessage(channel=channel_id, text=f"Your takedown for the week is {takedown_slot}")
    client.views_update(
            view_id=view_id,
            view={
                "type": "modal",
                "title": {
                    "type": "plain_text",
                    "text": "Takedowns Generated"
                },
                "blocks": []
            }
        )


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