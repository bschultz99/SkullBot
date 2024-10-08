"""DATABASE"""

USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    slack_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    membership VARCHAR(255)
    );
CREATE TABLE IF NOT EXISTS takedowns (
    slack_id VARCHAR(255) PRIMARY KEY REFERENCES users(slack_id) ON DELETE CASCADE,
    takedown_count INTEGER DEFAULT 0,
    monday_lunch BOOLEAN DEFAULT FALSE,
    monday_dinner BOOLEAN DEFAULT FALSE,
    tuesday_lunch BOOLEAN DEFAULT FALSE,
    tuesday_dinner BOOLEAN DEFAULT FALSE,
    wednesday_lunch BOOLEAN DEFAULT FALSE,
    wednesday_dinner BOOLEAN DEFAULT FALSE,
    thursday_lunch BOOLEAN DEFAULT FALSE,
    thursday_dinner BOOLEAN DEFAULT FALSE,
    friday_lunch BOOLEAN DEFAULT FALSE,
    friday_dinner BOOLEAN DEFAULT FALSE
    );
CREATE TABLE IF NOT EXISTS takedown_channels (
    takedown_slot VARCHAR(255) PRIMARY KEY,
    channel_id VARCHAR(255)
    );
CREATE TABLE IF NOT EXISTS cleanup_channels (
    cleanup VARCHAR(255) PRIMARY KEY,
    channel_id VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS positions (
    position VARCHAR(255) PRIMARY KEY,
    slack_id VARCHAR(255)
    ); 
CREATE TABLE IF NOT EXISTS cleanups (
    slack_id VARCHAR(255) PRIMARY KEY REFERENCES users(slack_id) ON DELETE CASCADE,
    used BOOLEAN DEFAULT FALSE,
    disabled BOOLEAN DEFAULT FALSE,
    captain BOOLEAN DEFAULT FALSE,
    captain_count INTEGER DEFAULT 0,
    kitchen INTEGER DEFAULT 0,
    zero_deck INTEGER DEFAULT 0,
    first_deck INTEGER DEFAULT 0,
    bathrooms INTEGER DEFAULT 0,
    stairs_halls_brojo_brolo INTEGER DEFAULT 0,
    deck_brush INTEGER DEFAULT 0
);
"""

TAKEDOWN_INSERT = '''
INSERT INTO takedowns(slack_id,
                        monday_lunch,
                        monday_dinner,
                        tuesday_lunch,
                        tuesday_dinner,
                        wednesday_lunch,
                        wednesday_dinner,
                        thursday_lunch,
                        thursday_dinner,
                        friday_lunch,
                        friday_dinner) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s ,%s)
ON CONFLICT (slack_id)
DO UPDATE SET monday_lunch = excluded.monday_lunch,
              monday_dinner = excluded.monday_dinner,
              tuesday_lunch = excluded.tuesday_lunch,
              tuesday_dinner = excluded.tuesday_dinner,
              wednesday_lunch = excluded.wednesday_lunch,
              wednesday_dinner = excluded.wednesday_dinner,
              thursday_lunch = excluded.thursday_lunch,
              thursday_dinner = excluded.thursday_dinner,
              friday_lunch = excluded.friday_lunch,
              friday_dinner = excluded.friday_dinner;
'''

USER_INSERT = '''
INSERT INTO users (slack_id, name, membership)
VALUES (%s, %s, %s)
ON CONFLICT (slack_id)
DO UPDATE SET name = excluded.name,
              membership = excluded.membership;
'''

CLEANUPS_INSERT = '''
INSERT INTO cleanups(slack_id, captain)
VALUES (%s, %s)
ON CONFLICT (slack_id)
DO UPDATE SET captain = excluded.captain;
'''

SELECT_ALL_USERS = '''
SELECT name, slack_id FROM users;
'''

REMOVE_SELECTED_USER = '''
DELETE FROM users WHERE slack_id = %s;
'''

#Generate Takedowns
TAKEDOWNS_WEEKLY = '''
DROP TABLE IF EXISTS takedowns_weekly;
CREATE TABLE IF NOT EXISTS takedowns_weekly (
    slack_id VARCHAR(255) PRIMARY KEY REFERENCES users(slack_id) ON DELETE CASCADE,
    assignment VARCHAR(255) DEFAULT ''
);
INSERT INTO takedowns_weekly (slack_id)
SELECT slack_id FROM users;
'''

TAKEDOWNS_ACTIVE_SELECT = '''
SELECT takedowns.* 
FROM takedowns 
INNER JOIN users
ON users.slack_id = takedowns.slack_id
WHERE users.membership != 'NM'
AND takedowns.{} = TRUE
ORDER BY takedowns.takedown_count;
'''

TAKEDOWNS_ALL_SELECT = '''
SELECT takedowns.* 
FROM takedowns 
INNER JOIN users
ON users.slack_id = takedowns.slack_id
WHERE takedowns.{} = TRUE
ORDER BY takedowns.takedown_count;
'''

TAKEDOWN_MEMBER_COUNT = '''
SELECT COUNT(*) as total_entries FROM takedowns;
'''

TAKEDOWNS_SUM_COUNT = '''
SELECT
    SUM(CASE WHEN monday_lunch THEN 1 ELSE 0 END) AS monday_lunch_count,
    SUM(CASE WHEN monday_dinner THEN 1 ELSE 0 END) AS monday_dinner_count,
    SUM(CASE WHEN tuesday_lunch THEN 1 ELSE 0 END) AS tuesday_lunch_count,
    SUM(CASE WHEN tuesday_dinner THEN 1 ELSE 0 END) AS tuesday_dinner_count,
    SUM(CASE WHEN wednesday_lunch THEN 1 ELSE 0 END) AS wednesday_lunch_count,
    SUM(CASE WHEN wednesday_dinner THEN 1 ELSE 0 END) AS wednesday_dinner_count,
    SUM(CASE WHEN thursday_lunch THEN 1 ELSE 0 END) AS thursday_lunch_count,
    SUM(CASE WHEN thursday_dinner THEN 1 ELSE 0 END) AS thursday_dinner_count,
    SUM(CASE WHEN friday_lunch THEN 1 ELSE 0 END) AS friday_lunch_count,
    SUM(CASE WHEN friday_dinner THEN 1 ELSE 0 END) AS friday_dinner_count
FROM takedowns;
'''

TAKEDOWNS_UPDATE_ASSIGNMENT = '''
UPDATE takedowns 
SET takedown_count = takedown_count + 1
WHERE slack_id = %s;
UPDATE takedowns_weekly
SET assignment = CASE
WHEN assignment = '' THEN %s
ELSE assignment || ',' || %s
END
WHERE slack_id = %s;
'''

TAKEDOWN_DISPLAY = '''
SELECT users.name, takedowns_weekly.assignment
FROM takedowns_weekly
INNER JOIN users
ON users.slack_id = takedowns_weekly.slack_id;
'''

TAKEDOWNS_CHANNEL_INSERT = '''
INSERT INTO takedown_channels (takedown_slot, channel_id)
VALUES (%s, %s)
ON CONFLICT (takedown_slot) DO UPDATE
SET channel_id = EXCLUDED.channel_id;
'''

TAKEDOWNS_SELECT_MEMBERS = '''
SELECT users.slack_id 
FROM users
LEFT JOIN takedowns_weekly
ON users.slack_id = takedowns_weekly.slack_id
WHERE takedowns_weekly.assignment LIKE %s;
'''

THETA_ONE_SELECT = '''
SELECT slack_id
FROM positions
WHERE position = 'Theta-1';
'''

#Generate Cleanups
CLEANUPS_WEEKLY = '''
DROP TABLE IF EXISTS cleanups_weekly;
CREATE TABLE IF NOT EXISTS cleanups_weekly (
    slack_id VARCHAR(255) PRIMARY KEY REFERENCES users(slack_id) ON DELETE CASCADE,
    captain BOOLEAN DEFAULT False,
    assignment VARCHAR(255) DEFAULT ''
);
INSERT INTO cleanups_weekly (slack_id)
SELECT slack_id FROM users;
'''
CAPTAIN_SELECT = '''
SELECT slack_id
FROM cleanups
WHERE captain = true
AND used = false
AND disabled = false
ORDER BY {}, captain_count;
'''

CAPTAIN_UPDATE = '''
UPDATE cleanups
SET used = true,
captain_count = captain_count + 1,
{} = {} + 1
WHERE slack_id = '{}';
UPDATE cleanups_weekly
SET captain = true,
assignment = '{}'
WHERE slack_id = '{}';
'''
CLEANUPS_ASSIGN = '''
UPDATE cleanups
SET used = true,
{} = {} + 1
WHERE slack_id = '{}';
UPDATE cleanups_weekly
SET assignment = '{}'
WHERE slack_id = '{}';
'''

CLEANUPS_SELECT = '''
SELECT slack_id
FROM cleanups
WHERE used = false
AND disabled = false
ORDER BY {};
'''

CLEANUPS_RESET = '''
UPDATE cleanups
SET used = false;
'''

CLEANUPS_DISPLAY = '''
SELECT users.name, cleanups_weekly.captain, cleanups_weekly.assignment
FROM cleanups_weekly
INNER JOIN users
ON users.slack_id = cleanups_weekly.slack_id
ORDER BY assignment, captain DESC;
'''

THETA_THREE_SELECT = '''
SELECT slack_id
FROM positions
WHERE position = 'Theta-3';
'''

CLEANUPS_SELECT_MEMBERS = '''
SELECT users.slack_id 
FROM users
LEFT JOIN cleanups_weekly
ON users.slack_id = cleanups_weekly.slack_id
WHERE cleanups_weekly.assignment = %s;
'''

CLEANUPS_REMAINING_COUNT = '''
SELECT COUNT(*) FROM cleanups
WHERE used = false
AND disabled = false;
'''

CLEANUPS_REMAINING = '''
SELECT slack_id
FROM cleanups
WHERE used = false
AND disabled = false;
ORDER BY {};
'''

#Toggle
CLEANUPS_CAPTAIN_SELECT = '''
SELECT users.name, users.slack_id
FROM users
LEFT JOIN cleanups
on users.slack_id = cleanups.slack_id;
'''
CLEANUPS_CAPTAIN_UPDATE = '''
UPDATE cleanups
SET captain = NOT captain
WHERE slack_id = %s;
'''

CLEANUPS_TOGGLE_UPDATE = '''
UPDATE cleanups
SET disabled = NOT disabled
WHERE slack_id = %s;
'''

# ADMIN PORTAL

POSITIONS_SLACK_INSERT = '''
INSERT INTO positions(slack_id, position)
VALUES (%s, %s)
ON CONFLICT (position) DO UPDATE
SET slack_id = EXCLUDED.slack_id;  
'''

ADMIN_CHECK = '''
SELECT count(*) FROM positions
WHERE slack_id = %s;
'''

# Display Takedowns
TAKEDOWN_DATABASE = '''
SELECT users.name, takedowns.*
FROM users
LEFT JOIN takedowns
on users.slack_id = takedowns.slack_id;
'''

CLEANUP_DATABASE = '''
SELECT users.name, cleanups.*
FROM users
LEFT JOIN cleanups
on users.slack_id = cleanups.slack_id;
'''