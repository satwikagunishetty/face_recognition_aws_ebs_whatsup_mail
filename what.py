from twilio.rest import Client
def whatsup():
    account_sid = "xxxxxxxxxxxxxxxxxx"
    # Your Auth Token from twilio.com/console
    auth_token  = "xxxxxxxxxxxxxxxxxx"

    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    client = Client(account_sid, auth_token)
 
    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155xxxxx'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+91xxxxx'

    client.messages.create(body='Hi Satwika your face was recognized!!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
    return('Whatsup message sent successfully')