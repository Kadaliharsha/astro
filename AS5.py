import tkinter as tk
from tkinter import ttk

# Function to calculate the single digit (reduction to a single digit)
def reduce_to_single_digit(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

# Function to calculate Primary Number (PN) and Destiny Number (DN)
def calculate_primary_and_destiny(dob):
    # Split the date of birth into day, month, and year
    day, month, year = map(int, dob.split('/'))

    # Calculate Primary Number (PN) -> based on the day
    primary_number = reduce_to_single_digit(day)

    # Calculate Destiny Number (DN) -> based on the full date (DD/MM/YYYY)
    destiny_number = reduce_to_single_digit(day + month + year)

    return primary_number, destiny_number

# Define the KPN based on the industry (as a dictionary)
industry_kpn_mapping = {
    "Agriculture": [3, 6],
    "Fishing": [3, 2],
    "Mining": [8, 9],
    "Automobile": [8, 2],
    "Electronics": [8, 4],
    "Textiles": [3, 6],
    "Food & Beverage": [2, 3],
    "Pharmaceuticals": [5, 4],
    "Chemicals": [8, 4],
    "Plastic": [5, 4],
    "Machinery": [8, 5],
    "Processing/Converting": [5, 4],
    "Construction": [8, 9],
    "Steel & Metals": [8, 9],
    "Healthcare": [3, 5],
    "Education": [3, 5],
    "Finance & Insurance": [3, 4],
    "Real Estate": [8, 9],
    "Retail": [3, 5],
    "Hospitality & Tourism": [2, 6],
    "Transportation & Logistics": [8, 9],
    "Telecommunications": [4, 5],
    "Media & Entertainment": [4, 6],
    "Information Technology (IT)": [4, 5],
    "Legal": [1, 8],
    "Doctor": [3, 9],
    "Architect": [1, 9],
    "Management Consultancy": [1, 9],
    "Non-Profit Organizations": [2, 8],
    "Renewable Energy": [1, 4],
    "Artificial Intelligence (AI)": [4, 5],
    "Blockchain & Cryptocurrencies": [4, 5],
    "Biotechnology": [3, 4],
    "Sports & Gaming": [3, 9],
    "Astrology & Occult": [3, 7],
    "Security": [8, 9],
}

# Name Number Compatibility Table
compatibility_table = [
    {"planet_number": 1, "planet_name": "Sun", "friends": [1, 2, 4, 7], "neutrals": [3, 5, 6, 9], "enemies": [8]},
    {"planet_number": 2, "planet_name": "Moon", "friends": [1, 2, 3, 4, 7], "neutrals": [8, 9], "enemies": [5, 6]},
    {"planet_number": 3, "planet_name": "Jupiter", "friends": [1, 2, 3, 9], "neutrals": [6, 5, 8], "enemies": [4, 7]},
    {"planet_number": 4, "planet_name": "Rahu", "friends": [1, 2, 7], "neutrals": [5, 6, 9], "enemies": [3, 4]},
    {"planet_number": 5, "planet_name": "Mercury", "friends": [1, 3, 4, 5, 6, 8], "neutrals": [7, 9], "enemies": [2]},
    {"planet_number": 6, "planet_name": "Venus", "friends": [5, 8, 9], "neutrals": [1, 3, 4, 6, 7], "enemies": [2]},
    {"planet_number": 7, "planet_name": "Ketu", "friends": [1, 2], "neutrals": [4, 5], "enemies": [3]},
    {"planet_number": 8, "planet_name": "Saturn", "friends": [3], "neutrals": [2], "enemies": [1]},
    {"planet_number": 9, "planet_name": "Mars", "friends": [2, 3], "neutrals": [1, 5, 6, 9], "enemies": [4, 7, 8]},
]

# Function to calculate Name Number for a company
def calculate_name_number(name):
    letter_to_number = {
        'A': 1, 'J': 1, 'S': 1,
        'B': 2, 'K': 2, 'T': 2,
        'C': 3, 'L': 3, 'U': 3,
        'D': 4, 'M': 4, 'V': 4,
        'E': 5, 'N': 5, 'W': 5,
        'F': 6, 'O': 6, 'X': 6,
        'G': 7, 'P': 7, 'Y': 7,
        'H': 8, 'Q': 8, 'Z': 8,
        'I': 9, 'R': 9
    }
    
    # Sum the numeric values of each letter in the company name
    total = sum(letter_to_number.get(char.upper(), 0) for char in name if char.isalpha())
    
    # Reduce the sum to a single digit
    name_number = reduce_to_single_digit(total)
    return name_number

# GUI setup
class NumerologyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numerology KPN Calculator")
        self.root.geometry("400x800")
        
        # Add this new section in the GUI to select the type of company/firm.
        self.label_firm_type = tk.Label(root, text="Select Firm Type:")
        self.label_firm_type.pack(pady=10)

        self.selected_firm_type = tk.StringVar()
        self.firm_type_dropdown = ttk.Combobox(root, textvariable=self.selected_firm_type)
        self.firm_type_dropdown['values'] = ["New Company", "Existing Company", "Partnership Firm", "Proprietorship Firm"]
        self.firm_type_dropdown.pack(pady=5)
        
        # Company name input
        self.company_name_label = tk.Label(root, text="Enter Company Name:")
        self.company_name_label.pack(pady=10)
        self.company_name_entry = tk.Entry(root)
        self.company_name_entry.pack(pady=5)

        # Button to calculate Name Number for the company
        self.calculate_name_number_button = tk.Button(root, text="Calculate Name Number", command=self.display_name_number)
        self.calculate_name_number_button.pack(pady=5)

        # Label to display the calculated Name Number
        self.name_number_label = tk.Label(root, text="")
        self.name_number_label.pack(pady=10)

        # Label and dropdown for industry selection
        self.label_industry = tk.Label(root, text="Select Industry:")
        self.label_industry.pack(pady=10)

        self.selected_industry = tk.StringVar()
        self.industry_dropdown = ttk.Combobox(root, textvariable=self.selected_industry)
        self.industry_dropdown['values'] = sorted(list(industry_kpn_mapping.keys()))
        self.industry_dropdown.pack(pady=5)

        # Button to get the KPN based on selected industry
        self.get_kpn_button = tk.Button(root, text="Get KPN", command=self.display_kpn)
        self.get_kpn_button.pack(pady=5)

        # Label to display the selected KPN
        self.kpn_label = tk.Label(root, text="")
        self.kpn_label.pack(pady=10)
        

        # Entry fields for owner data input
        self.owner_count_label = tk.Label(root, text="Enter number of owners:")
        self.owner_count_label.pack(pady=10)
        self.owner_count = tk.Entry(root)
        self.owner_count.pack(pady=5)

        # Button to submit owner count and get owner details
        self.submit_button = tk.Button(root, text="Submit", command=self.get_owner_details)
        self.submit_button.pack(pady=5)
        
        self.favorable_number_label = tk.Label(root, text="")
        self.favorable_number_label.pack(pady=10)
        

    # Function to display Name Number based on company name
    def display_name_number(self):
        company_name = self.company_name_entry.get()
        name_number = calculate_name_number(company_name)
        self.name_number_label.config(text=f"Name Number for '{company_name}': {name_number}")
        
    # Function to display KPN based on selected industry
    def display_kpn(self):
        industry = self.selected_industry.get()
        kpn = industry_kpn_mapping.get(industry, [])
        self.kpn_label.config(text=f"KPN for {industry}: {kpn}")

    # Function to dynamically gather owner details
    def get_owner_details(self):
        try:
            owner_count = int(self.owner_count.get())
            owner_details_window = tk.Toplevel(self.root)
            owner_details_window.title("Owner Details")

            # List to hold owner data entries
            self.owner_entries = []

            for i in range(owner_count):
                owner_data = {}

                tk.Label(owner_details_window, text=f"Owner {i+1} Name:").pack(pady=5)
                owner_name_entry = tk.Entry(owner_details_window)
                owner_name_entry.pack(pady=5)
                owner_data['name'] = owner_name_entry

                tk.Label(owner_details_window, text="Date of Birth (DD/MM/YYYY):").pack(pady=5)
                owner_dob_entry = tk.Entry(owner_details_window)
                owner_dob_entry.pack(pady=5)
                owner_data['dob'] = owner_dob_entry

                self.owner_entries.append(owner_data)

            # Submit button for processing owner details
            tk.Button(owner_details_window, text="Submit", command=self.process_owner_details).pack(pady=10)

        except ValueError:
            print("Please enter a valid number of owners.")

    def process_owner_details(self):
        all_numbers = []
        unique_numbers = set()

        kpn = [int(num) for num in self.kpn_label.cget("text").split(":")[1].strip()[1:-1].split(", ")]
        firm_type = self.selected_firm_type.get()

        for idx, owner in enumerate(self.owner_entries):
            name = owner['name'].get()
            dob = owner['dob'].get()
            primary_number, destiny_number = calculate_primary_and_destiny(dob)

            all_numbers.extend([primary_number, destiny_number])
            unique_numbers.update([primary_number, destiny_number])

            print(f"Owner {idx + 1} Name: {name}, Primary Number: {primary_number}, Destiny Number: {destiny_number}")

        print("All Values:", list(all_numbers))
        print("Unique Numbers:", unique_numbers)

        # Calculate compatible planets based on PN and DN
        compatible_planets = self.display_compatible_planets(all_numbers, unique_numbers)  # Pass unique_numbers here
        compatible_planets_kpn = self.display_compatible_planets_kpn(kpn, compatible_planets)

        name_number = None

        # Check if any KPN is in compatible planets
        for planet in compatible_planets_kpn:
            kpn_value = next((p['planet_number'] for p in compatibility_table if p['planet_name'] == planet), None)
            if kpn_value and kpn_value in all_numbers:
                name_number = kpn_value
                break

        # If no name number found based on KPN, check for preferred list
        if name_number is None:
            name_number = self.check_preferred_list(all_numbers, kpn)

        # Display results
        if name_number:
            self.favorable_number_label.config(text=f"Name Number for '{self.company_name_entry.get()}': {name_number}")
        else:
            self.favorable_number_label.config(text="No compatible Name Number found.")
        
        print("Compatible Planets based on PN and DN:", compatible_planets)
        print(f"Selected Name Number: {name_number}")

    def display_compatible_planets(self, all_numbers, unique_numbers):  # Add unique_numbers as a parameter
        compatible_planets = []
        
        for planet in compatibility_table:
            planet_number = planet["planet_number"]
            
            # Check if none of the unique numbers are in the enemies list
            if not any(num in planet["enemies"] for num in unique_numbers):
                
                # Check if all unique numbers are in friends or neutrals list
                if all(num in planet["friends"] or num in planet["neutrals"] for num in unique_numbers):
                    compatible_planets.append(f"Planet {planet_number}: {planet['planet_name']}")
                    
        return compatible_planets  # Return the compatible planets for further processing

    def display_compatible_planets_kpn(self, kpn, compatible_planets):
        compatible_planets_kpn = []

        for kpn_value in kpn:
            if kpn_value in [planet['planet_number'] for planet in compatibility_table]:
                # If KPN is in the compatibility table and also compatible with PN and DN
                if compatibility_table[kpn_value - 1]['planet_name'] in compatible_planets:
                    compatible_planets_kpn.append(compatibility_table[kpn_value - 1]['planet_name'])

        return compatible_planets_kpn

    def check_preferred_list(self, all_numbers, kpn):
        preferred_list = [1, 3, 5, 6]
        preferred_matches = list(set(all_numbers) & set(preferred_list))
        matches = sorted(preferred_matches, reverse=True)  # Sort in descending order

        if matches:
            print("Checking against preferred list (based on PN and DN):")
            print(f"Preferred Matches: {matches}")
            
            # Assigning favorable levels
            name_numbers = {}
            if len(matches) == 1:
                name_numbers['Favorable'] = matches[0]
            elif len(matches) == 2:
                name_numbers['Extreme Favorable'] = matches[0]
                name_numbers['Favorable'] = matches[1]
            elif len(matches) == 3:
                name_numbers['Extreme Favorable'] = matches[0]
                name_numbers['Favorable 1'] = matches[1]
                name_numbers['Favorable 2'] = matches[2]

            # Print the assigned name numbers based on priority
            for level, num in name_numbers.items():
                print(f"{level}: {num}")

            return name_numbers.get('Extreme Favorable', matches[0])  # Return the highest priority
        return None


# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    app = NumerologyApp(root)
    root.mainloop()
