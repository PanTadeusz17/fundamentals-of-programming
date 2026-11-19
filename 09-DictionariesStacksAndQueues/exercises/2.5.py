def main():
    contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
    contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}
    merged_contacts = contacts_A | contacts_B # ta kreska to suma zbiorow wiec laczy a i b
    print("Merged contacts:", merged_contacts)

if __name__ == "__main__":
    main()