"""MODAL VIEWS"""

USER_PORTAL = """
{
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
							"text": "Monday"
						},
						"value": "M"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Tuesday"
						},
						"value": "T"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Wednesday"
						},
						"value": "W"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Thursday"
						},
						"value": "TH"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Friday"
						},
						"value": "F"
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
"""