def main():
    required_permissions = {"read", "write", "execute"}
    user_permissions = {"read", "write"}
    has_permissions = required_permissions.issubset(user_permissions) # jesli dobrze rozumiem to issubset sprawdza czy elementy sa w dwoch podanych argumentach
    print(has_permissions)

if __name__ == "__main__":
    main()