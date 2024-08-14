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
    takedown_count BOOLEAN DEFAULT FALSE,
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
INSERT INTO takedowns(slack_id) VALUES (%s);
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