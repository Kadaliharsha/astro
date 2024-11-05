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

# Preferred list for favorable numbers
preferred_list = [1, 3, 5, 6]

# GUI setup
class NumerologyApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Numerology KPN Calculator")
        self.root.geometry("400x500")

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

                tk.Label(owner_details_window, text=f"Owner {i + 1} Name:").pack(pady=5)
                owner_data['name'] = tk.Entry(owner_details_window)
                owner_data['name'].pack(pady=5)

                tk.Label(owner_details_window, text=f"Owner {i + 1} DOB (DD/MM/YYYY):").pack(pady=5)
                owner_data['dob'] = tk.Entry(owner_details_window)
                owner_data['dob'].pack(pady=5)

                self.owner_entries.append(owner_data)

            # Submit button to gather and process the data
            tk.Button(owner_details_window, text="Submit", command=self.process_owner_details).pack(pady=10)

        except ValueError:
            print("Please enter a valid number of owners")

    # Function to process owner details on submission
    def process_owner_details(self):
        all_numbers = []  # To collect all PN and DN of all owners
        unique_numbers = set()  # To collect unique numbers

        # Extract KPN list from the label text
        kpn_text = self.kpn_label.cget("text")
        kpn = [int(num) for num in kpn_text.split(":")[1].strip()[1:-1].split(", ")] if kpn_text else []
        print(f"KPN values: {kpn}")

        # Calculate PN and DN for each owner
        for idx, owner in enumerate(self.owner_entries):
            name = owner['name'].get()
            dob = owner['dob'].get()
            primary_number, destiny_number = calculate_primary_and_destiny(dob)

            # Add PN and DN to all_numbers list
            all_numbers.extend([primary_number, destiny_number])
            unique_numbers.update([primary_number, destiny_number])

            print(f"Owner {idx + 1} Name: {name}, Primary Number: {primary_number}, Destiny Number: {destiny_number}")

        # Find compatible planets based on PN and DN
        compatible_planets = []
        for number in all_numbers:
            for planet in compatibility_table:
                if number in planet['friends']:
                    compatible_planets.append(planet['planet_name'])
                    break  # Found a friend planet, no need to check further

        # Find compatible planets based on KPN
        kpn_compatible_planets = []
        for k in kpn:
            for planet in compatibility_table:
                if k in planet['friends']:
                    kpn_compatible_planets.append(planet['planet_name'])
                    break  # Found a friend planet, no need to check further

        # Viable Name Number based on compatible KPN
        viable_name_number = []
        for k in kpn:
            for planet in compatibility_table:
                if k in planet['friends']:
                    viable_name_number.append(planet['planet_name'])
                    break  # Found a friend planet, no need to check further

        # Prepare additional favorable name numbers based on preferred list
        additional_favorable = {}
        for num in unique_numbers:
            if num in preferred_list:
                if num in additional_favorable:
                    additional_favorable[num] += 1
                else:
                    additional_favorable[num] = 1

        # Sort and categorize the favorable name numbers based on priority
        most_favorable = [num for num in preferred_list if num in unique_numbers][:1]
        favorable = [num for num in preferred_list if num in unique_numbers][1:2]
        neutral_favorable = [num for num in preferred_list if num in unique_numbers][2:3]
        less_favorable = [num for num in preferred_list if num in unique_numbers][3:4]

        # Print results
        print(f"All Values: {all_numbers}")
        print(f"Unique Numbers: {unique_numbers}")

        print(f"Compatible Planets based on PN and DN: {compatible_planets}")
        print(f"Compatible Planets based on KPN: {kpn_compatible_planets}")

        print(f"Viable Name Number based on compatible KPN: {viable_name_number}")

        print("\nAdditional Favorable Name Numbers based on Preferred List:")
        print(f"Most Favorable Name Number: {most_favorable[0] if most_favorable else 'None'}")
        print(f"Favorable Name Number: {favorable[0] if favorable else 'None'}")
        print(f"Neutral Favorable Name Number: {neutral_favorable[0] if neutral_favorable else 'None'}")
        print(f"Less Favorable Number: {less_favorable[0] if less_favorable else 'None'}")

# Run the application
if __name__ == "_main_":
    root = tk.Tk()
    app = NumerologyApp(root)
    root.mainloop()