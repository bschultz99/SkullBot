"""DATABASE"""

USER_TABLE = """
CREATE TABLE users (
    slack_id VARCHAR(255),
    name VARCHAR(255),
    membership VARCHAR(255)
    );
"""

USER_INSERT = '''
INSERT INTO users (slack_id, name, membership)
VALUES ("{}", "{}", "{}")
ON CONFLICT (slack_id)
DO UPDATE SET name = excluded.name,
              membership = excluded.membership;
'''