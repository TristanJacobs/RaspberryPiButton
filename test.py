import pymsteams

myTeamsMessage =pymsteams.connectorcard("https://cipal.webhook.office.com/webhookb2/642e95be-13ad-4047-9524-7540837007be@f8a354ea-4ec5-4d7c-b3b2-882f2f2e3e71/IncomingWebhook/27a74a1a8c634108ae1bcaea6699f987/06cde2be-7569-4a9d-9259-05fedafa1c59")

myTeamsMessage.text("Hello World")