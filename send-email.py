from sendgrid import SendGridAPIClient
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = SendGridAPIClient('SG.K6yDCV4-TV2zADdV_F9_Tw.rH5zl6aM1wu-0n2V19j4Q6j19HBolqDMJFB0MZi56KACopied!')
from_email = Email("pratikdesai93@gmail.com")
to_email = To("pratikdesai93@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)