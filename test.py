from twilio.rest import Client

def main():
    print("Testing twilio!")

    # Your Account SID from twilio.com/console
    account_sid = "AC498919314d33c0523546f6c9d6c0c41d"


    # Your Auth Token from twilio.com/console
    auth_token  = "ed71fc1d9ae77b93d5f4ae5fd801a5e4"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+4917632288154',
        to='+4917632288154')

    print(message.sid)


    print(message.sid)
  
if __name__== "__main__":
  main()

