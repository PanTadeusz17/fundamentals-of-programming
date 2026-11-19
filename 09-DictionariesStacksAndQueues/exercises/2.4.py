def main():
    emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
    spam_list = {"spam1@example.com", "spam2@example.com"}
    spam_emails = emails_received & spam_list # & to czesc wspolna wiec te dwa spamy tylko wypisze
    print("Spam emails:", spam_emails)

if __name__ == "__main__":
    main()