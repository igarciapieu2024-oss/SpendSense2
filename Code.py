#Algorithms 
def quicksort_desc(products): #QUICKSORT for sorting products from expensive to cheap
    if len(products) <= 1: #if the len is smaller or equal to one we return the products list
        return products
    pivot = random.choice(products) # state the pivot randomly to avoid worst case scenario
    higher = [x for x in products[1:] if x['price'] > pivot['price']] #  subarrays based on if more expensive or cheaper than the product
    lower = [x for x in products[1:] if x['price'] <= pivot['price']]
    return quicksort_desc(higher) + [pivot] + quicksort_desc(lower) # call recursively on high and low arrays
positive_actions = []  # creation of two hash tables for storage of positive and negative actions
negative_actions = []

def find_smallest(users):
    smallest_index = 0
    smallest = users[smallest_index]['username'].lower()
    for n in range(1, len(users)):
        if users[n]['username'].lower() < smallest:
            smallest_index = n
            smallest = users[n]['username'].lower()
    return smallest_index
    
def selection_sort_inplace(users):
    #Sorts uses in alphabetical order avoiding consuming extra space
    for i in range(len(users)):
        # Find the smallest element from position i onwards
        smallest_index = find_smallest(users, i)
        # Elemnsts are directly swaped in the original list
        users[i], users[smallest_index] = users[smallest_index], users[i]
    return users
    
def binary_search(users, username):
    low = 0
    high = len(users) - 1
    while low <= high:
        mid = (low + high) // 2
        if users[mid]['username'].lower() == username.lower():
            return mid
        elif users[mid]['username'].lower() < username.lower():
            low = mid + 1
        else:
            high = mid - 1
    return None
users = []

#CREATION OF THE REGISTRATION PAGE
# ALGORITHM REGISTRATION

def register():
    
    print("REGISTRATION")
    # WE ASK FOR INFORMATION TO THE USER
    name = input("Enter username: ")
    age = input("Enter age: ")
    hours = input("Enter hours worked per week: ")
    salary = input("Enter monthly salary: ")
    # IF IT DOES NOT INTRODUCE THE NAME, OR IF THE CONDITIONS OF PROPER FORMAT OF DIGIT IT RETURNS TO LOGIN SCREEN
    if not name or not age.isdigit() or not hours.isdigit() or not salary.isdigit():
        print("Data introduced is not valid")
        print("Redirecting to login screen...\n")
        return  login() #We finish if the data is not valid (return to log-in screen calling the log-in function)
    global users #Global variable to communicate operations inside and outside the function
    selection_sort(users) #If data is valid we first sort it users before searching as we need
    # for binary search sorted list
    if binary_search(users, name) is not None: #if when doing the search it does not
        # return None (it exists) we finish and redirect to the login screen
        print("User already exists! Please log in.")
        print("Redirecting to login screen...\n")
        return login()
    users.append({ #else we create the user dictionary hash table
            "username": name,
            "password": "1234",
            "age": int(age),
            "hours": int(hours),
            "salary": float(salary)
        })
    print("Welcome, you have been registered!")
    return login() # And we call log in for user introducing the credentials
    
# ALGORITHM LOGIN

def login():
    print("LOGIN")
    username = input("Enter username: ") #  the user is asked their credentials
    password = input("Enter password: ")

    global users
    selection_sort(users) # we first sort it before searching as we need
    # for binary search sorted list
    pos = binary_search(users, username) # we search in username the credentials

    if pos is None or users[pos]['password'] != password: #if the username is not found or the user name is found
        #but password is not correct it returns incorrect credentials and returns to log-in page
        print("Incorrect credentials\n")
        print("Redirecting to login screen...\n")
        return login()
    else: # else we welcome the user and redirect to the home page
        print(f"Welcome {users[pos]['username']}! Redirecting to Home Page\n")
        return home_page() #We call the home page menu to appear
#HERE is the representation of the first screen, if user selects 1 calls function login, 2 calls function register,
#if 3 it breaks and finishes the while loop and else it indicates it is not a valid option
#TO START IN WHILE CONDITION RUNNING WE ASK THE USER TO CHOOSE 3 OPTIONS
while True:
    print("1. Log in")
    print("2. Register")
    print("3. Exit")
    option = input("Choose an option: ")

    if option == "1": # IF SELECTED ONE WE CALL LOGIN
        login()
    elif option == "2": # IF SELECTED TWO WE CALL REGISTER
        register()
    elif option == "3": # IF SELECTED THREE WE BREAK AND FINISH THE LOOP
        print("Exiting")
        break
    else:
        print("Invalid option.\n") # PRINT INVALID AND ANOTHER OPTION WILL BE ASKED AS CONDITION STILL TRUE
      
# WE CREATE THE HOME PAGE FUNCTION THAT REPRESENTS THE MENU PAGE
def home_page():
    print("HOME PAGE")
    while True: # WHILE CONDITION OF TRUE TO STILL BE RUNNING
        print("\n1. Upload Image")
        print("2. View Smart Shopping Cart")
        print("3. View Economic and Environmental Metrics")
        print("4. Log Out")

        option = input("Choose an option: ") #WE ASK USER TO CHOOSE AN OPTION

        if option == "1": # IF CHOOSE ONE WE GO TO THE UPLOAD IMAGE MENU
            return upload_image() # IF SELECTED 1 CALL THE UPLOAD FUNCTION
        elif option == "2": # IF WE CHOOSE OPTION 2 IT GOES TO THE CART HOME PAGE
            print("Redirecting to Smart Shopping Cart...\n")
            return smart_cart()  # WILL BE CREATED LATER
        elif option == "3": # IF WE CHOOSE OPTION 3 IT GOES TO THE METRICS  PAGE
            print("Redirecting to Metrics Page...\n")
            return metrics_page()  # IF 3 WE CHOOSE IT RETURNS TO METRICS
        else:
            print("Invalid option.\n")
            
#Creation of a function so that user chooses to upload image from camera or gallery

def upload_image():
    print("You have chosen 'Upload Image'")
    print("'Choose from Gallery or Take photo?'")

    option = input("1. Gallery\n2. Take Photo\nChoose option: ")

    if option == "1":
        return gallery_flow() # IF CHOOSE 1 WE REDIRECT TO GALLERY PAGE CALLING IT
    elif option == "2":
        return camera_flow() # IF CHOOSE 2 WE REDIRECT TO CAMERA PAGE CALLING IT
    else: # IF OTHER  WE REDIRECT TO HOME AGE AND RETURN ERROR MESSAGE
        print("Invalid option. We return to the home page ")
        return home_page()
#Creation of the function of the gallery

def gallery_flow():
    print("System requests gallery access")
    permission = input("Grant permission? (yes/no): ").lower() # Ask user for permission

    if permission == "yes": # if permission granted gallery open
        print("Access granted → Opening Gallery...")
        print("User selects a photo.")
        return photo_and_product_recognition() # we call product recognition function
    else: # if permission not granted error message displayed and we return to home_page
        print("Permission needed to access gallery.")
        return home_page()

#Creation of the function of the camera

def camera_flow():
    print("System requests camera access")
    permission = input("Grant permission? (yes/no): ").lower() # ask user for permission

    if permission == "yes": # if permission granted camera is open
        print("Access granted → Opening Camera...")
        print("User takes a photo.")
        return photo_and_product_recognition()
    else: # if permission is not granted error message displayed
        print("Permission needed to access camera.")
        return home_page()
recognized_products = [] # creation of a hash table and dictionary
# function of the photo recognition by the system once provided the photo by the user to ask user for label

def photo_and_product_recognition():
    print("System uploads photo")
    print("AI recognizes clothing successfully!")

    print("\nSystem asks: 'Please upload the clothing label photo to continue.'") # we ask for the label
    label = input("Upload label? (yes/no): ").lower() # ask the user to upload the label

    if label == "yes": # if label introduced we call the function to analyze the label
        #AI EXTRACTION SIMULATION
        print("\nAI extracts brand, price, origin, material, and CO2 impact...")
        brand = input("Brand: ")
        price = input("Price (€): ")
        origin = input("Origin: ")
        material = input("Material: ")
        co2 = input("CO2 impact (kg): ")
        product = { # create hash table dictionary
            "brand": brand,
            "price": float(price) if price.replace('.', '', 1).isdigit() else 0.0,
            "origin": origin,
            "material": material,
            "co2": float(co2) if co2.replace('.', '', 1).isdigit() else 0.0
        }
        recognized_products.append(product) # Add the product to the hash table
        return calculate_metrics(product) # We then call to the metrics calculation
    else:
        print("\nError: Missing label information.")
        print("Returning to the home page.\n")
        return home_page()  # Return to the home page and error message is displayed.
      
def calculate_metrics(product):
    print("\nCALCULATING ECONOMIC AND ENVIRONMENTAL METRICS")
    global users #connect users information along the functions
    username = input("\nConfirm your username to calculate working hours: ") # want to know the hours
    #and therefore ask for username to search in hash
    selection_sort(users) # we sort for then the application of binary search
    person = binary_search(users, username) # we search for the username in user hash table
    if person is not None: # if the username is found
        user = users[person]
        monthly_salary = user["salary"] # we extract the information
        hours_per_week = user["hours"]
        hourly_wage = monthly_salary / (4 * hours_per_week)
        hours_to_afford = product["price"] / hourly_wage
    else:
        hours_to_afford = 0 # we have not found the user in the hash table we return error message
            # and set hours to 0
        print("User not found in system. Unable to calculate working hours.")
    # DISPLAY THE INFORMATION  CALCULATED
    print("\n--ECONOMIC AND ENVIRONMENTAL METRICS --")
    print(f"Brand: {product['brand']} | Price: {product['price']}€ | Origin: {product['origin']}")
    print(f"Material: {product['material']} | CO2 Impact: {product['co2']} kg")
    print(f"Hours worked to afford this item: {hours_to_afford:.2f} hours\n")
    # NOW WE ASK FOR THE USER IF IT WANTS
    choice = input("Answer (yes/no): Would you like to see second-hand alternatives?").lower()
    if choice == "yes":
        return show_second_hand_options(product) # IF YES WE GO CALL THE FUNCTION TO SEE SECOND HAND ALTERNATIVES
    else:
        print("Redirecting to Smart Shopping Cart...\n")
        return smart_cart() # IF NOT WE CALL SMART CART FUNCTION HOME PAGE
        
def load_vinted_data():
    with open('vinted_dataset.json', 'r') as file:
        return json.load(file)   
        
def show_second_hand_options(product):
    print("\nSHOWING SECOND-HAND ALTERNATIVES")
    print("Fetching second-hand data...")
    data = load_vinted_data()  # Load external dataset
    matches = []
    # If data is opened, we search for matches
    if data:
        matches = [d for d in data if d["brand"].lower() == product["brand"].lower()]
    # If there are no matches, we use  simulated alternatives more deeper
    if not matches:
        print("No direct matches found in dataset. Showing default simulated options:")
        alternatives = [
            {"source": "VintageStore", "price": round(product["price"] * 0.6, 2)},
            {"source": "ReuseApp", "price": round(product["price"] * 0.5, 2)},
            {"source": "EcoWear", "price": round(product["price"] * 0.4, 2)}
        ]
    else:
        print(f"Found {len(matches)} second-hand alternatives for {product['brand']}:")
        alternatives = []
        for m in matches[:]: show matches
            alt_price = round(float(m.get("second_hand_price", product["price"] * 0.6)), 2)
            alt_source = m.get("source", "Vinted")
            alternatives.append({
                "source": alt_source,
                "price": alt_price
            })
    # Display results
    print("\nSECOND-HAND OPTIONS")
    for alt in alternatives:
        print(f"- {alt['source']} : {alt['price']}€")
    # Finally all the alternatives are introduced to each of the product so stored in hash tables dictionary 
    product["alternatives"] = alternatives
    print("\nAlternatives have been added to the Smart Shopping Cart.\n")
    return smart_cart()  # redirect to the smart cart 

import random

positive_actions = []  # creation of two hash tables for storage of positive and negative actions
negative_actions = []

def smart_cart():
    print("\nSMART SHOPPING CART")
    print("Displaying all recognized items:\n")
    ordered_products = quicksort_desc(recognized_products) # short the products from more expensive to cheaper
    print(" ITEMS IN CART (from highest to lowest price)")
    for item in ordered_products:
        print(f"- {item['brand']} | {item['price']}€ | CO2: {item['co2']} kg") #display elements sorted
        if "alternatives" in item: # if alternatives are in the product dictionary then we display them also in the smart cart
            print("  Second-hand options:")
            for alt in item["alternatives"]:
                print(f"{alt['source']} - {alt['price']}€")
    print("\nChoose an item to manage (enter number) or 0 to return:")
    choice = input("Select a digit Option: ")
    if not choice.isdigit(): # If choice is not appropiate returns to the smart cart menu
        print("Invalid input. Returning to Home Page...\n")
        return smart_cart()
    if choice < 1 or choice > len(ordered_products):
        print("Invalid choice. Returning...\n")
        return smart_cart()
    selected_item = ordered_products[choice - 1] # As first product index 1
    print(f"\nSelected: {selected_item['brand']} | {selected_item['price']}€") # Describe the product selected
    # Now we ask user what he has done with the product
    print("\n1. Completed Original Purchase")
    print("2. Saved the Money")
    print("3. Purchased Second-Hand Alternative")
    print("4. Cancel")
    action = input("Choose an option: ")
    if action == "1": # if we choose option 1
        negative_actions.append(selected_item) # appends to negative action
        recognized_products.remove(selected_item) # removes the product from the smart cart
        print("Item removed from Smart Cart and stored in negative actions.\n")
        return metrics_page() # calls the metric page function to redirect the user
    elif action == "2": # if it selects the 2
        positive_actions.append(selected_item) # stores to positive actions
        recognized_products.remove(selected_item) # removes the product from the smart cart
        print("Item removed from Smart Cart and stored in positive actions.\n")
        return metrics_page() # calls the metric page function to redirect the user
    elif action == "3": # if it selects the 3
        print("\nSystem asks for the price of the second-hand item.")
        alt_price = float(input("Enter second-hand price "))
        savings = selected_item["price"] - alt_price
        record = { # create a record and add to positive metrics
            "brand": selected_item["brand"],
            "original_price": selected_item["price"],
            "second_hand_price": alt_price,
            "savings": round(savings, 2),
            "co2": selected_item["co2"]
        }
        positive_actions.append(record)
        recognized_products.remove(selected_item) # remove from the smart cart
    elif action == "4": # if select action 4 then we redirect to smart cart with all the options visible
        print("Returning to Smart Shopping Cart...\n")
        return smart_cart()
    else: # in case invalid option we finally return to smart cart
        print("Invalid option. Returning to Smart Shopping Cart...\n")
        return smart_cart()

# Now we build the metric page
def metrics_page():
    print("METRICS PAGE")
    print("Choose what you want to view:") # ask for the feature they want to see
    print("1. Economic Metrics")
    print("2. Environmental Metrics")
    if option == "1":
        return economic_metrics()  # call economic metrics functions
    elif option == "2":
        return environmental_metrics()  # call environmental metrics functions

def economic_metrics():
    print("ECONOMIC ANALYSIS")
    print("Displaying two boxes: Positive Actions and Negative Actions")
    print(" POSITIVE ECONOMIC ACTIONS")
    if not positive_actions: # if we do not have positive actions we return message
        print("No positive actions yet.")
    else: # if we have we print each of the positive action
        for act in positive_actions:
            if "savings" in act: # if it has been chosen action 3 of doing second hand we have other attributes
                print(f"- {act['brand']} | Saved {act['savings']}€ | CO2: {act['co2']} kg")
            else: # if chosen 1
                print(f"- {act['brand']} | Price: {act['price']}€ | CO2: {act['co2']} kg")
    print("NEGATIVE ACTIONS:")
    if not negative_actions: # if we do not have negative actions we return message
        print("No negative actions yet.")
    else: # if we have we print each of the negative  action
        for act in negative_actions:
            print(f"- {act['brand']} | Paid {act['price']}€ | CO2: {act['co2']} kg")
    #Option to return to the Home page
    print("2. Back to Home Page")
    option = input("Choose an option: yes or no ")

    if option == "yes":
        return home_page()
    if option == "no":
        return metrics_page()
