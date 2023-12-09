"""Templates used for the slack messages"""
def user_portal(user_name):
    block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Hello, {user_name}"
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
						"text": "Update User Profile"
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
    return block

USER_FORM = [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Full Name"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a status"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 2"
						},
						"value": "value-IH2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 3"
						},
						"value": "value-IH3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Townsman"
						},
						"value": "value-TM"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "New Member"
						},
						"value": "value-NM"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Membership"
			}
		},
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please Enter Your Takedown Availability."
			},
			"accessory": {
				"type": "checkboxes",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Monday Lunch"
						},
						"value": "value-ML"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Monday Dinner"
						},
						"value": "value-MD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tuesday Lunch"
						},
						"value": "value-TL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tuesday Dinner"
						},
						"value": "value-TD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wednesday Lunch"
						},
						"value": "value-WL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wednesday Dinner"
						},
						"value": "value-WD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thursday Lunch"
						},
						"value": "value-RL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thursday Dinner"
						},
						"value": "value-RD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Friday Lunch"
						},
						"value": "value-FL"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Friday Dinner"
						},
						"value": "value-FD"
					}
				],
				"action_id": "takedowns-action"
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Submit"
					},
					"value": "takedowns-submit",
					"action_id": "actionId-usersubmit"
				}
			]
		}
	]

def admin_portal(user_name):
    block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Hello, {user_name}"
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
						"text": "Admin"
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
						"text": "Missed Responsibilities"
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
						"text": "Takedowns"
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
						"text": "Cleanups"
					},
					"value": "close_window",
					"action_id": "close_window"
				}
			]
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
						"text": "Close"
					},
					"value": "close_window",
					"action_id": "close_window"
				}
			]
		}
	]
    return block

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