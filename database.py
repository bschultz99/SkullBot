"""DATABASE"""

USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    slack_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    membership VARCHAR(255)
    );
CREATE TABLE IF NOT EXISTS takedowns (
    slack_id VARCHAR(255) PRIMARY KEY REFERENCES users(slack_id) ON DELETE CASCADE,
    used BOOLEAN DEFAULT FALSE,
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

SELECT_ALL_USERS = '''
SELECT name, slack_id FROM users;
'''

REMOVE_SELECTED_USER = '''
DELETE FROM users WHERE slack_id = %s;
'''

#Generate Takedowns
TAKEDOWNS_WEEKLY = '''
CREATE TABLE IF NOT EXISTS takedowns_weekly (
    slack_id VARCHAR(255) PRIMARY KEY REFERENCES users(slack_id) ON DELETE CASCADE,
    assignment VARCHAR(255)
);
'''

TAKEDOWN_MEMBER_COUNT = '''
SELECT COUNT(*) as total_entries FROM takedowns;
'''

TAKEDOWNS_INSERT_SLACK = '''
INSERT INTO takedowns_weekly (slack_id)
SELECT slack_id FROM users;
'''