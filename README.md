Inventory Management App

This is a command-line Python application which allows the user to manage an inventory of products.

This application enables the user to performs all product "CRUD" operations: "List", "Show", "Create", "Update", "Destroy", "Reset", and "Quit.""

Note: this application uses a CSV file datastore.

Installation
First, "fork" this upstream repository under your own control.

Then download your forked version of this repository using the GitHub.com online interface or the Git command-line interface.

After downloading your forked repository, navigate into its root directory:

cd path/to/inventory-mgmt-app-py/
NOTE: all commands in this document assume you are running them from this root directory.

Setup
Before you run this application for the first time (or anytime you want to reset the database), reset the database by populating it with the default products:

# For Homebrew-installed Python 3.x on Mac OS:
python3 products_app/reset.py

# All others:
python products_app/reset.py
Usage
Run the application:

# For Homebrew-installed Python 3.x on Mac OS:
python3 products_app/app.py

# All others:
python products_app/app.py

# Explanation of Operations
1) List - allows the user to see all the products in the inventory.
2) Show - allows the user to see the information for a particular product by specifying the product identifier.
3) Create - allows the user to add a new product to the inventory.
4) Update - allows the user to change the information for a particular product by specifying the product identifier and desired changes.
5) Destroy - allows the user to delete a product from the inventory.
6) Reset - allows the user to overwrite any changes with the original product information.
7) Quit - allows the user to end the application.
