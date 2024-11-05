import string

# Step 1: Function to calculate Primary Number (PN) from Date of Birth
def calculate_primary_number(dob):
    day = int(dob.split('-')[0])
    return reduce_to_single_digit(day)

# Step 2: Function to calculate Destiny Number (DN) from Date of Birth
def calculate_destiny_number(dob):
    total = sum([int(d) for d in dob.replace('-', '')])
    return reduce_to_single_digit(total)

# Step 3: Function to reduce numbers to a single digit
def reduce_to_single_digit(num):
    while num > 9:
        num = sum([int(digit) for digit in str(num)])
    return num

# Step 4: Function to calculate Name Number (NN) based on the letters in the name
def calculate_name_number(company_name):
    letter_values = {letter: index % 9 + 1 for index, letter in enumerate(string.ascii_uppercase)}
    total = sum([letter_values[letter.upper()] for letter in company_name if letter.upper() in letter_values])
    return reduce_to_single_digit(total)

# Step 5: Function to calculate KPN (Karaka Planet Number) based on industry and return planet name
def get_kpn_by_industry(industry):
    industry_kpn = {
        "Agriculture": [3, 6], "IT": [4, 5], "Real Estate": [8, 9], "Hospitality": [2, 6],
        "Education": [3, 5], "Automobile": [8, 2], "Finance": [3, 4], "Healthcare": [3, 5],
        # Add more industries as needed...
    }
    return industry_kpn.get(industry, [0])

# Step 6: Compatibility check function with compatibility table and planet names
def check_compatibility(nn, kpn):
    # Compatibility table as a dictionary with planet numbers as keys
    compatibility_table = {
        1: {"planet": "Sun", "friends": [1, 2, 4, 7], "neutral": [3, 5, 6, 9], "enemies": [8]},
        2: {"planet": "Moon", "friends": [1, 2, 3, 4, 7], "neutral": [8, 9], "enemies": [5, 6]},
        3: {"planet": "Jupiter", "friends": [1, 2, 3, 9], "neutral": [5, 6, 8], "enemies": [4, 7]},
        4: {"planet": "Rahu", "friends": [1, 2, 7], "neutral": [5, 6, 9], "enemies": [3, 4, 8]},
        5: {"planet": "Mercury", "friends": [1, 3, 4, 5, 6, 8], "neutral": [7, 9], "enemies": [2]},
        6: {"planet": "Venus", "friends": [5, 8, 9], "neutral": [1, 3, 4, 6, 7], "enemies": [2]},
        7: {"planet": "Ketu", "friends": [1, 2], "neutral": [4, 5, 7], "enemies": [3, 6, 8, 9]},
        8: {"planet": "Saturn", "friends": [3, 5], "neutral": [2, 6], "enemies": [1, 4, 7, 8, 9]},
        9: {"planet": "Mars", "friends": [2, 3], "neutral": [1, 5, 6, 9], "enemies": [4, 7, 8]}
    }

    planet_name = compatibility_table.get(kpn, {}).get("planet", "Unknown")
    kpn_friends = compatibility_table.get(kpn, {}).get("friends", [])
    kpn_neutral = compatibility_table.get(kpn, {}).get("neutral", [])
    kpn_enemies = compatibility_table.get(kpn, {}).get("enemies", [])

    if nn in kpn_friends:
        return f"Most Favourable ({planet_name})"
    elif nn in kpn_neutral:
        return f"Neutral ({planet_name})"
    elif nn in kpn_enemies:
        return f"Unfavourable ({planet_name})"
    else:
        return f"No Compatibility Data ({planet_name})"

# Step 7: Clean company name by removing legal suffixes
def clean_company_name(company_name):
    legal_suffixes = ['Limited', 'Pvt. Ltd.', 'LLC', 'LLP']
    for suffix in legal_suffixes:
        company_name = company_name.replace(suffix, "").strip()
    return company_name

# Step 8: Main function to handle calculations based on number of owners and details
def calculate_company_name_compatibility():
    # Input the industry (simulating dropdown with options)
    industries = ["Agriculture", "IT", "Real Estate", "Hospitality", "Education", "Automobile", "Finance", "Healthcare"]
    print("Select an Industry:")
    for i, industry in enumerate(industries, 1):
        print(f"{i}. {industry}")
    industry_choice = int(input("Enter the number corresponding to the industry: "))
    industry = industries[industry_choice - 1]
    kpn_values = get_kpn_by_industry(industry)
    
    # Compatibility table to display planet names
    planet_names = {
        1: "Sun", 2: "Moon", 3: "Jupiter", 4: "Rahu", 5: "Mercury", 
        6: "Venus", 7: "Ketu", 8: "Saturn", 9: "Mars"
    }

    print(f"KPN for {industry}: {[(kpn, planet_names.get(kpn, 'Unknown')) for kpn in kpn_values]}")

    # Input the number of owners
    num_owners = int(input("Enter the number of owners: "))
    
    owners = []
    for i in range(num_owners):
        print(f"\nOwner {i+1} details:")
        name = input("Enter the owner's name: ")
        dob = input("Enter the date of birth (dd-mm-yyyy): ")
        time_of_birth = input("Enter the time of birth (hh:mm, 24hr format): ")
        place_of_birth = input("Enter the place of birth: ")
        pn = calculate_primary_number(dob)
        dn = calculate_destiny_number(dob)
        owners.append({"name": name, "pn": pn, "dn": dn})
        print(f"Owner {name}: PN = {pn}, DN = {dn}")

    # Company incorporation details (existing company)
    print("\nCompany Incorporation Details:")
    incorporation_date = input("Enter the company incorporation date (dd-mm-yyyy): ")
    incorporation_place = input("Enter the place of incorporation: ")

    # Input the proposed company name and clean it
    company_name = input("\nEnter the proposed/current company name (ignore Limited/Pvt. Limited/LLC/LLP): ")
    cleaned_name = clean_company_name(company_name)
    nn = calculate_name_number(cleaned_name)
    print(f"Name Number (NN) for '{cleaned_name}': {nn}")

    # Perform compatibility check for single owner
    if num_owners == 1:
        owner = owners[0]
        compatibility = check_compatibility(nn, kpn_values[0])
        print(f"Compatibility for single owner: {compatibility}")

    # Perform compatibility check for multiple owners (calculate CCPN, CCDN)
    elif num_owners > 1:
        ccpn = owners[0]['pn']
        ccdn = owners[0]['dn']
        for owner in owners[1:]:
            ccpn = min(ccpn, owner['pn'])  # Common Compatible Primary Number
            ccdn = min(ccdn, owner['dn'])  # Common Compatible Destiny Number

        print(f"CCPN (Common Compatible Primary Number): {ccpn}")
        print(f"CCDN (Common Compatible Destiny Number): {ccdn}")

        compatibility = check_compatibility(nn, kpn_values[0])
        print(f"Compatibility for multiple owners: {compatibility}")

if __name__ == "__main__":
    calculate_company_name_compatibility()