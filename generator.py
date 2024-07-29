import uuid
from datetime import datetime, timedelta
import random

def generate_test_data():
    # Generate a unique transaction ID (tid)
    tid = str(uuid.uuid4())
    
    # Generate a random amount between 1000.00 and 5000.00
    amount = "{:.2f}".format(random.uniform(50, 500000))
    
    # Define transaction types
    transaction_types = ["Credit", "Debit"]
    
    # Randomly select transaction type (0 for Credit, 1 for Debit)
    transaction_type_index = random.choice([0, 1])
    transaction_type = transaction_types[transaction_type_index]
    
    # Predefine a list of potential senders/receivers
    names = ["John Doe", "Jane Smith", "Acme Corporation", "Doe's Diner", "Tech Solutions Inc.", "Smith's Grocery", "Happy Paws Pet Shop", "Green Thumb Nursery", "Blue Sky Cafe", "Star Electronics", "City Bookstore", "Fitness First Gym", "QuickFix Auto Repair", "Sunshine Bakery", "Peak Performance Sports", "Elegant Fashions Boutique", "Corner Pharmacy", "Creative Minds Art Studio", "Taste of Italy Restaurant", "Ocean Breeze Spa"]

    
    # Determine sender and receiver based on transaction type
    if transaction_type == "Credit":
        sender = random.choice(names)
        receiver = "John Doe"
    else:  # Debit
        sender = "John Doe"
        receiver = random.choice(names)
    
    # Generate a random date within the next month
    days_into_future = random.randint(1, 30)
    date = datetime.now() + timedelta(days=days_into_future)
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    # Define possible descriptions
    descriptions = ["Salary", "Bonus", "Expense Reimbursement"]
    
    # Randomly select a description
    description = random.choice(descriptions)
    
    # Construct the test data dictionary
    test_data = {
        "tid": tid,
        "amount": amount,
        "transactionType": transaction_type_index,  # Use index (0 for Credit, 1 for Debit)
        "sender": sender,
        "receiver": receiver,
        "date": date_str,
        "description": description
    }
    
    return test_data

def iteration(iterations):
    for i in range(0,iterations):
        print(generate_test_data(),end=",\n")

iteration(iterations = 10)
