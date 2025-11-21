import random
import json
# Binary Search Tree for users with running time of 0(logn) for search and 0(logn) for insertion
class UserNode:
    def __init__(self, user_data):
        self.user = user_data
        self.left = None
        self.right = None
class UserBST:
    def __init__(self):
        self.root = None
    def insert(self, user_data): # if it does not have a root node it is established as root node 
        if self.root is None:
            self.root = UserNode(user_data)
        else: # if it has a root node we call the function _insert_recursive
            self._insert_recursive(self.root, user_data)
    
    def _insert_recursive(self, node, user_data):
        username = user_data['username'].lower() # Obtain username in lower case
        if username < node.user['username'].lower(): # if alphabetically is smaller than node it goes to left subtree
            if node.left is None: # if it does not have a left subtree it will be the new left subtree, creating a new node
                node.left = UserNode(user_data)
            else: # if it has a left subtree we call recursively and now the new root will be the actual left-node 
                self._insert_recursive(node.left, user_data)
        else: # if it is alphabetically greater it goes to right subtree
            if node.right is None: # if it does nor have a right child the node then it is the new right child creating a new node
                node.right = UserNode(user_data)
            else: # # if it has a right subtree we call recursively and now the new root will be the actual right-node 
                self._insert_recursive(node.right, user_data)
              
    def search(self, username): # this function search user in binary search tree with 0(logn) running time, calling the _search_recursive function
        return self._search_recursive(self.root, username.lower())
      
    def _search_recursive(self, node, username):
        if node is None: # in case is not root we return None
            return None
        if username == node.user['username'].lower(): # if username we want to find is the same as the name of the node we return it 
            return node.user
        elif username < node.user['username'].lower(): # if it is lower we call recursively the function searching in the left-subtree
            return self._search_recursive(node.left, username)
        else:  # else we call recursively the function searching in the right-subtree
            return self._search_recursive(node.right, username)
          
    # We create a Max Heap Map for a quicker access to products 0(1) and 0(logn) for insertion 
  class ProductHeap: # we create the max heap
    def __init__(self):
        self.heap = [] 
    def insert(self, product):
        self.heap.append(product)  # Add the product at the end 
        self._bubble_up(len(self.heap) - 1) # and call the function _bubble_up which to meet properties of max heap
    def _bubble_up(self, idx):
        while idx > 0: # while the index is greater than 0 
            parent_idx = (idx - 1) // 2 # calculate the parent index
            if self.heap[idx]['price'] > self.heap[parent_idx]['price']: # if the child is greater than parent then
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx] # it interchanges the order
                idx = parent_idx # and new index becomes the new parent indx 
            else: # else is in correct position so it finishes the loop
                break
    def get_all_sorted(self): # This return all products sorted 
        return sorted(self.heap, key=lambda x: x['price'], reverse=True)
    def remove(self, product): 
        self.heap = [p for p in self.heap if p != product] #it eliminates the product and create a new list without the eliminated item 
        #it reconstructuct the tree to meet the properties from the last parent node using ._bubble_down as now is reconstructing in the other way
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._bubble_down(i)
    def _bubble_down(self, idx): # This is the inverse operation we did with _bubble_up
        size = len(self.heap)
        while 2 * idx + 1 < size: # while it exists left child
            left_child_idx = 2 * idx + 1 
            right_child_idx = 2 * idx + 2
            largest_idx = idx # assume is parent indx
            
            if self.heap[left_child_idx]['price'] > self.heap[largest_idx]['price']:
                largest_idx = left_child_idx # if the left child is greater than the parent node, we redefine alrgest_indx
            
            if right_child_idx < size and self.heap[right_child_idx]['price'] > self.heap[largest_idx]['price']:
                largest_idx = right_child_idx # if right child is greater then we redefine largest index
            
            if largest_idx != idx: # now if the largest index is not equal to the index(parent) this means the parent was not the actual largest index so we interchange
                self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx] 
                idx = largest_idx
            else:
                break
user_bst = UserBST()
product_heap = ProductHeap()  
positive_actions = {}  
negative_actions = {}  
current_user = None
# REGISTRATION with the use of binary search tree with all operations 0(logn)
def register():
  print("REGISTRATION")
  # we ask for info
  name = input("Enter username: ")
    age = input("Enter age: ")
    hours = input("Enter hours worked per week: ")
    salary = input("Enter monthly salary: ")
# if it does not introduce the name or the passwords and other requirements in the proper format it returns to the log in page
if not name or not age.isdigit() or not hours.isdigit() or not salary.isdigit():
        print("Data introduced is not valid")
        print("Redirecting to login screen...\n")
        return login()
# if the username is found then we show error message and redirect to log in page
if user_bst.search(name) is not None:
        print("User already exists! Please log in.")
        print("Redirecting to login screen...\n")
        return login()
# if it does not exist and proper conditions it inserts the new user 
user_bst.insert(new_user)
print("Welcome, you have been registered!")
    return login()
# LOGIN ALGORITHM with the use of binary Search tree with all operations 0(logn)
def login():
  print("LOGIN")
  username = input("Enter username: ")
  password = input("Enter password: ")
  user = user_bst.search(username) # we search for the user given the inputs 
  if user is None or user['password'] != password: # if the user is not found or password is incorrect it returns to log in page
        print("Incorrect credentials\n")
        print("Redirecting to login screen...\n")
        return login()
    else: # ifis found it goes to the home page 
        current_user = user['username']
        print(f"Welcome {user['username']}! Redirecting to Home Page\n")
        return home_page()
# MAIN MENU STRCUTURE
while True:
    print("1. Log in")
    print("2. Register")
    print("3. Exit")
    option = input("Choose an option: ")

    if option == "1":
        login()
    elif option == "2":
        register()
    elif option == "3":
        print("Exiting")
        break
    else:
        print("Invalid option.\n")
# HOME PAGE 
def home_page():
    while True:
        print("HOME PAGE")
        print("\n1. Upload Image")
        print("2. View Smart Shopping Cart")
        print("3. View Economic and Environmental Metrics")
        print("4. Log Out")

        option = input("Choose an option: ")

        if option == "1":
            return upload_image()
        elif option == "2":
            print("Redirecting to Smart Shopping Cart...\n")
            return smart_cart()
        elif option == "3":
            print("Redirecting to Metrics Page...\n")
            return metrics_page()
        elif option == "4":
            print("Logging out...\n")
            return
        else:
            print("Invalid option.\n")
#Creation of a function so that user chooses to upload image from camera or gallery
def upload_image():
    print("You have chosen 'Upload Image'")
    print("'Choose from Gallery or Take photo?'")

    option = input("1. Gallery\n2. Take Photo\nChoose option: ")

    if option == "1":
        return gallery_flow()
    elif option == "2":
        return camera_flow()
    else:
        print("Invalid option. We return to the home page ")
        return home_page()

#Creation of the function of the gallery
def gallery_flow():
    print("System requests gallery access")
    permission = input("Grant permission? (yes/no): ").lower()

    if permission == "yes":
        print("Access granted → Opening Gallery...")
        print("User selects a photo.")
        return photo_and_product_recognition()
    else:
        print("Permission needed to access gallery.")
        return home_page()

#Creation of the function of the camera
def camera_flow():
    print("System requests camera access")
    permission = input("Grant permission? (yes/no): ").lower()

    if permission == "yes":
        print("Access granted → Opening Camera...")
        print("User takes a photo.")
        return photo_and_product_recognition()
    else:
        print("Permission needed to access camera.")
        return home_page()

# function of the photo recognition by the system once provided the photo by the user to ask user for label
def photo_and_product_recognition():
    
    print("System uploads photo")
    print("AI recognizes clothing successfully!")

    print("\nSystem asks: 'Please upload the clothing label photo to continue.'")
    label = input("Upload label? (yes/no): ").lower()

    if label == "yes":
        #AI EXTRACTION SIMULATION
        print("\nAI extracts brand, price, origin, material, and CO2 impact...")
        brand = input("Brand: ")
        price = input("Price (€): ")
        origin = input("Origin: ")
        material = input("Material: ")
        co2 = input("CO2 impact (kg): ")
        
        # Validación de valores numéricos
        try:
            price_float = float(price) if price.replace('.', '', 1).isdigit() else 0.0
            co2_float = float(co2) if co2.replace('.', '', 1).isdigit() else 0.0
        except ValueError:
            print("Invalid numeric values. Returning to home page.\n")
            return home_page()
        
        product = {
            "brand": brand,
            "price": price_float,
            "origin": origin,
            "material": material,
            "co2": co2_float
        }
        
        # insert the product using max heap structure for O(log n)
        product_heap.insert(product)
        return calculate_metrics(product)
    else:
        print("\nError: Missing label information.")
        print("Returning to the home page.\n")
        return home_page()
  # function to metrics
  def calculate_metrics(product):
    
    print("\nCALCULATING ECONOMIC AND ENVIRONMENTAL METRICS")
    username = input("\nConfirm your username to calculate working hours: ")
    
    # search for the user using bianry search tree
    user = user_bst.search(username)
    
    if user is not None: # if found we extract its information
        monthly_salary = user["salary"]
        hours_per_week = user["hours"]
        hourly_wage = monthly_salary / (4 * hours_per_week)
        hours_to_afford = product["price"] / hourly_wage
    else:
        hours_to_afford = 0 # if not found set it to 0 
        print("User not found in system. Unable to calculate working hours.")
    
    print("ECONOMIC AND ENVIRONMENTAL METRICS")
    print(f"Brand: {product['brand']} | Price: {product['price']}€ | Origin: {product['origin']}")
    print(f"Material: {product['material']} | CO2 Impact: {product['co2']} kg")
    print(f"Hours worked to afford this item: {hours_to_afford:.2f} hours\n")
    
    choice = input("Answer (yes/no): Would you like to see second-hand alternatives?").lower()
    if choice == "yes":
        return show_second_hand_options(product)
    else:
        print("Redirecting to Smart Shopping Cart...\n")
        return smart_cart()
  # To access to database of second hand alternatives 
  def load_vinted_data():
    try:
        with open('vinted_dataset.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
      
  def show_second_hand_options(product):

    print("SHOWING SECOND-HAND ALTERNATIVES")
    print("Fetching second-hand data...")
    data = load_vinted_data()
    matches = []
    
    if data:
        #Simpe search 0(n) for data to see if matches 
        matches = [d for d in data if d["brand"].lower() == product["brand"].lower()]
    
    if not matches: # if not direct matches we apply a simulation
        print("No direct matches found in dataset. Showing default simulated options:")
        alternatives = [
            {"source": "VintageStore", "price": round(product["price"] * 0.6, 2)},
            {"source": "ReuseApp", "price": round(product["price"] * 0.5, 2)},
            {"source": "EcoWear", "price": round(product["price"] * 0.4, 2)}
        ]
    else: # if found we print the matches found in the database
        print(f"Found {len(matches)} second-hand alternatives for {product['brand']}:")
        alternatives = []
        for m in matches:
            alt_price = round(float(m.get("second_hand_price", product["price"] * 0.6)), 2)
            alt_source = m.get("source", "Vinted")
            alternatives.append({
                "source": alt_source,
                "price": alt_price
            })
    
    print("SECOND-HAND OPTIONS")
    for alt in alternatives:
        print(f"- {alt['source']} : {alt['price']}€")
    
    product["alternatives"] = alternatives # add the alternatives 
    print("Alternatives have been added to the Smart Shopping Cart")
    return smart_cart()

 def smart_cart():
   print("SMART SHOPPING CART")
   print("Displaying all recognized items:")
   ordered_products = product_heap.get_all_sorted() # to obtain the products sorted 0(nlogn)
   print("ITEMS IN CART (from highest to lowest price)")
    for idx, item in enumerate(ordered_products, 1):
        print(f"{idx}. {item['brand']} | {item['price']}€ | CO2: {item['co2']} kg")
        if "alternatives" in item:
            print("   Second-hand options:")
            for alt in item["alternatives"]:
                print(f"   - {alt['source']} - {alt['price']}€")
    
    print("\nChoose an item to manage (enter number) or 0 to return:")
    choice_input = input("Select a digit Option: ")
    
    if not choice_input.isdigit():
        print("Invalid input. Returning to Smart Cart...\n")
        return smart_cart()
    
    choice = int(choice_input)
    
    if choice == 0:
        return home_page()
    
    if choice < 1 or choice > len(ordered_products):
        print("Invalid choice. Returning...\n")
        return smart_cart()
    
    selected_item = ordered_products[choice - 1]
    print(f"\nSelected: {selected_item['brand']} | {selected_item['price']}€")
    
    print("\n1. Completed Original Purchase")
    print("2. Saved the Money")
    print("3. Purchased Second-Hand Alternative")
    print("4. Cancel")
    action = input("Choose an option: ")
    
    # initiate a new dictionary if it does not exist
    if current_user not in positive_actions:
        positive_actions[current_user] = []
    if current_user not in negative_actions:
        negative_actions[current_user] = []
    
    if action == "1":
        negative_actions[current_user].append(selected_item)
        product_heap.remove(selected_item)
        print("Item removed from Smart Cart and stored in negative actions.\n")
        return metrics_page()
    elif action == "2":
        positive_actions[current_user].append(selected_item)
        product_heap.remove(selected_item)
        print("Item removed from Smart Cart and stored in positive actions.\n")
        return metrics_page()
    elif action == "3":
        print("\nSystem asks for the price of the second-hand item.")
        try:
            alt_price = float(input("Enter second-hand price (€): "))
        except ValueError:
            print("Invalid price. Returning to cart...\n")
            return smart_cart()
        
        savings = selected_item["price"] - alt_price
        record = {
            "brand": selected_item["brand"],
            "original_price": selected_item["price"],
            "second_hand_price": alt_price,
            "savings": round(savings, 2),
            "co2": selected_item["co2"]
        }
        positive_actions[current_user].append(record)
        product_heap.remove(selected_item)
        print("Second-hand purchase recorded. Item removed from cart.\n")
        return metrics_page()
    elif action == "4":
        print("Returning to Smart Shopping Cart...\n")
        return smart_cart()
    else:
        print("Invalid option. Returning to Smart Shopping Cart...\n")
        return smart_cart()
  def metrics_page():
      print("\nMETRICS PAGE")
      print("Choose what you want to view:")
      print("1. Economic Metrics")
      print("2. Environmental Metrics")
      print("3. Back to Home Page")
      option = input("Choose an option: ")
    
      if option == "1":
          return economic_metrics()
      elif option == "2":
          return environmental_metrics()
      elif option == "3":
          return home_page()
      else:
          print("Invalid option.\n")
          return metrics_page()
  def economic_metrics():
    
    print("\nECONOMIC ANALYSIS")
    print("Displaying two boxes: Positive Actions and Negative Actions")
    print("\nPOSITIVE ECONOMIC ACTIONS")
    
    # access to the hash table in 0(1)
    user_positive = positive_actions.get(current_user, [])
    
    if not user_positive:
        print("No positive actions yet.")
    else:
        for act in user_positive:
            if "savings" in act:
                print(f"- {act['brand']} | Saved {act['savings']}€ | CO2: {act['co2']} kg")
            else:
                print(f"- {act['brand']} | Price: {act['price']}€ | CO2: {act['co2']} kg")
    
    print("\nNEGATIVE ACTIONS:")
    
    # access to the hash table in 0(1)

    user_negative = negative_actions.get(current_user, [])
    
    if not user_negative:
        print("No negative actions yet.")
    else:
        for act in user_negative:
            print(f"- {act['brand']} | Paid {act['price']}€ | CO2: {act['co2']} kg")
    
    print("\n1. Back to Home Page")
    option = input("Choose an option: ")

    if option == "1":
        return home_page()
    else:
        return metrics_page()

  def environmental_metrics():
        print("\nENVIRONMENTAL ANALYSIS")
        print("This section would display CO2 impact metrics.")
        print("1. Back to Metrics Page")
        option = input("Choose an option: ")
        
        if option == "1":
            return metrics_page()
        else:
            return home_page()
      

