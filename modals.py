"""MODAL VIEWS"""

USER_PORTAL = {
	"type": "modal",
	"callback_id": "user-portal-modal",
	"title": {
		"type": "plain_text",
		"text": "User Portal"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel"
	},
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Fill out the following to update your user information.\nBe sure to click submit to make sure the info saves."
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "null-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Name"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Membership Status"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 2"
						},
						"value": "IH2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "In-House 3"
						},
						"value": "IH3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Townsman"
						},
						"value": "TM"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "New Member"
						},
						"value": "NM"
					}
				],
				"action_id": "null-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Membership"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "checkboxes",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Monday Lunch"
						},
						"value": "ML"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": "Monday Dinner"
						},
						"value": "MD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tuesday Lunch"
						},
						"value": "TL"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": "Tuesday Dinner"
						},
						"value": "TD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wednesday Lunch"
						},
						"value": "WL"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": "Wednesday Dinner"
						},
						"value": "WD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thursday Lunch"
						},
						"value": "HL"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": "Thursday Dinner"
						},
						"value": "HD"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Friday Lunch"
						},
						"value": "FL"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": "Friday Dinner"
						},
						"value": "FD"
					}
				],
				"action_id": "null-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Takedown Availability"
			}
		}
	]
}

ADMIN_PORTAL = {
	"title": {
		"type": "plain_text",
		"text": "Admin Portal"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"type": "modal",
	"callback_id": "admin-portal-modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel"
	},
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hello, if you have any questions please reach out to Bryant. He would prefer to be bugged than for something to break."
			}
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Remove A User"
					},
					"value": "remove-user",
					"action_id": "remove-user"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Generate Takedowns"
					},
					"value": "generate-takedowns",
					"action_id": "generate-takedowns"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Insert data"
					},
					"value": "insert-data",
					"action_id": "insert-data"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Add admin"
					},
					"value": "add-admin",
					"action_id": "add-admin"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Generate Cleanups"
					},
					"value": "generate-cleanups",
					"action_id": "generate-cleanups"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Enable/Disable Cleanup Member"
					},
					"value": "toggle-cleanup",
					"action_id": "toggle-cleanup"
				},
                {
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Enable/Disable Cleanup Captain"
					},
					"value": "toggle-captain",
					"action_id": "toggle-captain"
				}
			]
		}
	]
}

REMOVE_USER = {
	"title": {
		"type": "plain_text",
		"text": "Remove User Portal"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"type": "modal",
	"callback_id": "remove-user-modal",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please pick a member to remove from the system:"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user"
				},
				"options": [],
				"action_id": "null-action"
			}
		}
	]
}

TOGGLE_CAPTAIN = {
	"title": {
		"type": "plain_text",
		"text": "Toggle Cleanup Captain Portal"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"type": "modal",
	"callback_id": "toggle-captain-modal",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please pick a member to toggle their captain status for cleanups:"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user"
				},
				"options": [],
				"action_id": "null-action"
			}
		}
	]
}

TOGGLE_CLEANUP = {
	"title": {
		"type": "plain_text",
		"text": "Toggle Cleanup Member Portal"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"type": "modal",
	"callback_id": "toggle-cleanup-modal",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please pick a member to toggle their cleanup status for cleanups:"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user"
				},
				"options": [],
				"action_id": "null-action"
			}
		}
	]
}

ADD_ADMIN_USER = {
	"title": {
		"type": "plain_text",
		"text": "Add Admin Portal"
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit"
	},
	"type": "modal",
	"callback_id": "add-admin-modal",
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please pick a user for the position:"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user"
				},
				"options": [],
				"action_id": "null-action"
			}
		},
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Please pick a position for the user:"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a position"
				},
				"options": [
                    {
						"text": {
							"type": "plain_text",
							"text": "Theta-1"
						},
						"value": "Theta-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Theta-2"
						},
						"value": "Theta-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Theta-3"
						},
						"value": "Theta-3"
					}],
				"action_id": "null-action"
			}
		}
	]
}