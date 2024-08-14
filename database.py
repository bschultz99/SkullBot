"""DATABASE"""

USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    slack_id VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    membership VARCHAR(255)
    );
"""

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