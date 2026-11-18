import emails

def main():
    print("Sender:", emails.email_sender())
    print("Recipient:", emails.email_recipient())
    print("Subject:", emails.email_subject())
    print("Body:\n" + emails.email_body())

if __name__ == "__main__":
    main()