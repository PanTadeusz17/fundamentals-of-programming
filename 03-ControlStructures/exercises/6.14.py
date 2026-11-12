facebook = True
twitter = False
instagram = True


if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print(f"facebook = {facebook}")
    print(f"twitter = {twitter}")
    print(f"instagram = {instagram}")
    print("You are a good influencer!")