2.1
def register_party(parties):
    """
    Check if the new party has an acceptable number of members for registration.

    Args:
    - parties (list): List of parties, each represented by key-value pairs with keys "party_name",
                      "reg_number", and "member_count".

    Returns:
    - accepted_parties (list): List of parties with acceptable member counts for registration.
    """
    accepted_parties = []

    for party in parties:
        # Extract party details
        party_name = party.get("party_name")
        reg_number = party.get("reg_number")
        member_count = party.get("member_count")

        # Check if the member count meets the registration requirements
        if member_count >= 100:
            accepted_parties.append(party_name)
            print(f"Party '{party_name}' with registration number '{reg_number}' is accepted for registration.")
        else:
            print(f"Party '{party_name}' with registration number '{reg_number}' does not have enough members for registration.")

    return accepted_parties


2.2  
# Define the parties list with the last registered party's details
parties = [
    {"party_name": "ABC Party", "reg_number": 10003318, "member_count": 120},
   
]

# Define the details for the new MK party
new_party = {"party_name": "MK Party", "reg_number": parties[-1]["reg_number"] + 1, "member_count": 5300}

 
accepted_parties = register_party(parties + [new_party])

# Check if the MK party was registered

if "MK Party" in accepted_parties:
    print("MK Party has been successfully registered.")
else:
    print("MK Party did not meet the registration criteria and could not be registered.")

     # List of party abbreviations from Annexure A
    

2.4
party_abbreviations = ["ASC", "ATM", "AASD", "ANC", "AGANG SA", "ALJAMA", "ATA", "ZAPO", "APC", "BRA","BLF","ZACP","CMP","CSA","COPE","DA","DLC","ECOFORUM","EFF","F4SD","FREE DEMS"]
# List of parties with more than 1000 members
parties_with_more_than_1000_members = ["ASC", "EFF", "ANC", "DA"]   

# Using list comprehension to filter out parties with less than 1,000 members
filtered_parties_lc = [party for party in party_abbreviations if party in parties_with_more_than_1000_members]

# Using filter function as an alternative approach
filtered_parties_filter = list(filter(lambda party: party in parties_with_more_than_1000_members, party_abbreviations))

print("Filtered Parties (using list comprehension):", filtered_parties_lc)
print("Filtered Parties (using filter function):", filtered_parties_filter)


2.5
#Rewrite the list comprehension in question 2.4 into a normal list data structure.

# List of party abbreviations from Annexure A
party_abbreviations = ["ASC", "ATM", "AASD", "ANC", "AGANG SA", "ALJAMA", "ATA", "ZAPO", "APC", "BRA","BLF","ZACP","CMP","CSA","COPE","DA","DLC","ECOFORUM","EFF","F4SD","FREE DEMS"]

# List of parties with more than 1000 members
parties_with_more_than_1000_members = ["ANC", "EFF", "ASC", "DA"]  

# Initialize an empty list to store filtered parties
filtered_parties = []

# Filter out parties with less than 1,000 members using a for loop
for party in party_abbreviations:
    if party in parties_with_more_than_1000_members:
        filtered_parties.append(party)

print("Filtered Parties (using for loop):", filtered_parties)


 
registered_voters = list(filter(lambda voter: voter.get('registered', False),filtered_parties))