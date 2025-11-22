# SpendSense
SpendSense is positioned as the first digital solution in the Spanish ecommerce market, which turns shopping into a responsible and conscious act, helping you save, gain control, and reduce your environmental footprint, by calculating both the financial and environmental impact for every purchase 

# Description 
SpendSense is a Python-based web app developed as part of the Algorithms and Data Structures course at IE University.
The project applies multiple core algorithms learned in class. We used data structures such as arrays or hash tables in Code.py and algorithms such as binary search, quicksort and selection sort. 
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/df466ff7-89b0-4614-a5b8-4ade4b508787" 
           alt="Spend Sense App Home Page" 
           width="300" />
      <br><b>App Home Page</b>
    </td>
  </tr>
</table>

# Table of Contents
- Features
- Files in Directory 
- Installation and Usage
- Algorithms Usage
- Credits
  

# Features 
- **Product Recognition:** Upload an image of an item to extraxt its brand, price and origin.   

- **Financial Awareness:** Converts price into hours of work based on user salary data          

- **Environmental Awarness:** Calculates carbon footprtint using API data and associations' databases. 


- **Alternative finder:** Suggests second-hand or eco-friendly options via integrates marketplace APIs, like Wallapop or Vinted 

- **Smart Shopping Cart:** Tracks spending vs. savings and visualizes progress over time. 

- **Gamification:** Rewards users for sustainable desicions through progress metrics. 

# Files in the Directory 

| **File/Folder** | **Description** |
|-----------------|-----------------|
| `Code.py` | Main file that runs the Flask web app and handles routing logic. Contains the search, sorting, and recommendation algorithms. |
| `Code_complementary_Binary_Search_Treee.py` | file with possible future implementation to offer lower running time (not actual app) |
| `data/` | Includes environmental impact datasets and product examples. |
| `static/` | CSS, images, and front-end assets used in the app interface. |
| `templates/` | HTML templates (Home, Upload, Results, Metrics). |
| `README.md` | The document you’re reading now. |
| `vinted_dataset.csv` | Dataset with second hand alternatives of Vinted. |

# Installation and Usage 
**Step-by-Step Setup:**

  **Step 1:** Download and extract the ZIP folder `SpendSense-main.zip`
  
  **Step 2:** Open the extracted folder. 
  
  **Step 3:** Double-click the file `run_app.command`(Mac) or `run_app.bat`(Windows)
  
  This automatically creates a virtual environment, installs dependencies, and        launches the app 

   **Step 4:** Once the installation completes, your default browser will open           automatically at: `http://127.0.0.1:5000`

   **Step 5:** Use the intereface: 
   
- Register or log in 
- Upload a product image 
- View metrics and alternative suggestions
- Save your results or share them
  
# Algorithm Usage
Our goal was the implementation of many algorithms to evaluate direct comparison and also prove real-word applications in different cases. 
However we also found interesting getting the lowest running time as possible so made a complementary code "Code_complementary_Binary_Search_trees" to search for the minimum running time as possible. 

Firstly in our main code directory which support the main application we used. 
- Selection sort: for sorting the names in alphabetical order for then use the binary search which require sorted list. Running time was 0(n^2). We used this approach for the internal flow as we do not require that large amount of time and we don`t risk space management as we do in quicksort (at same time of quicksort is done recursion which occupies more memory). 
- Quicksort algorithm: We use quicksort_desc(), to sort the products from more expensive to cheaper in the section of smart_cart(). The specific use of this was because in this action we wanted a lower running time 0(nlogn) for users to see more quicy their cart. Here we assume a risk of space management due to also application of recursion inside the Quicksort algorithms. 
- Binary Search is used in the registration with the application of seeing if the user is not already registered, in the login to find the user credentials and in the metric calculation to search data about the users salary. The running time was of 0(logn), but as we had previously to sort it its running time increased.
- Hash Tables are used to store structure data of users, the recognized products, positive and negative actions allowing access time of 0(1). 

Secondly we could see how this runnning times were not as efficient so we dive less profundly in the application of Binary Search tree for future considerations in a future time
- Binary Search Tree construction allowed a search and insertion in average of 0(logn) which would allowed a more faster way of sorting and searching for elements when the tree is ordered. In case of not ordered it would be 0(n)
- Max Heap implementation with parent being always greater than the child in the sorting of products allow to access in 0(1) running time and insertion in 0(logn). With functions to reorganize itself to meet the properties
- Hash tables being used as accessng tool provide in average case 0(1) running time
- Simple Search 0(n) to go one by one through products of the database

# Further Improvements 

- Implement user account storage (SQLite)
- Expand enviromental data bases with live APIs
- Include community-based sustainability scoring
- Introduce notificatons for price drops or impact milestones 
- Add multilingual support (EN/ES) 

# Bibliography 





# Credits 
This project was developed for the Algorithms and Data Structures (2025-26) course at IE university. 

**Team SpendSense**
- Ana Cañizales 
- Asis Saldaña 
- Mario Sanchez 
- Diego Marcos de Oro
- Lucía Bartolomé 
- Irene García 


  
  
                                                              
                                                  






