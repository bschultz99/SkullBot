"""Templates used for the slack messages"""
USER_PORTAL = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hello, INSER_NAME_HERE,"
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
						"text": "User Account Information"
					},
					"value": "user_account_information",
					"action_id": "user_account_information"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Update User Profil"
					},
					"value": "update_user_profile",
					"action_id": "update_user_profile"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Display Information"
					},
					"value": "display_information",
					"action_id": "display_information"
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Close Window"
					},
					"value": "close_window",
					"action_id": "close_window"
				}
			]
		}
	]
HELP_MESSAGE = """Welcome to the ThetaBot. These are the following features:
1. /help - Gives information on how the slack commands work.
2. /user-form - Fill this out to update your name, membership, and takedown availability.
3. /cleanup-settings - ADMIN - Change cleanups settings i.e. membership, minimum people, etc.
4. /removeuser - ADMIN - Remove a user from the user, cleanups, and takedown database.
5. /generate-cleanup-database - ADMIN - Generate the cleanup database by adding the cleanups and setting default values to 0.
6. /generate-cleanups - ADMIN - Generates the weekly cleanups.
7. /generate-takedowns - ADMIN - Generates the weekly takedowns.
8. /display-takedowns - Display the takedown database.
9. /display-cleanups - Display the cleanups database.
10. /admin-form - ADMIN - Add admins to the system.
11. /fines-form - ADMIN- Submit fines for members.
12. /reconcilliation-form - ADMIN - Use to reconcille fines of members.
13. /display-fines - Display the fines database.
14. /display-reconcilliation - Display the reconcilliation Database.
15. /display-naughtylist - Displays the fines, reconcilliations, and how much members owe.
16. /end-semester - ADMIN - Restarts the semester.
"""