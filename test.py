def user_form(user_name):
    block = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Hello, {user_name}:"
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
    return block

print(user_form('Bryant'))