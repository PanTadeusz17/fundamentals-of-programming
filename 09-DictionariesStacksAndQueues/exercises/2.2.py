def main():
    emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]
    unique_emails = set(emails) # set robi konkretne niepowtarzajace sie elementy wiec jak cos sie powtorzy to znika
    print(unique_emails)

if __name__ == "__main__":
    main()