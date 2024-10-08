import os
from pizzapi import Customer, Address

# Retrieve secrets for customer info
customer_name = os.getenv('CUSTOMER_NAME')
customer_email = os.getenv('CUSTOMER_EMAIL')
customer_phone = os.getenv('CUSTOMER_PHONE')

# Retrieve customer address from secrets
customer_address = os.getenv('CUSTOMER_ADDRESS')  # This should be a string like "123 Main St, Temecula, CA, 92592"

# Split address into components (assuming the format: "Street, City, State, Zip")
address_parts = customer_address.split(',')
street = address_parts[0].strip()
city = address_parts[1].strip()
state = address_parts[2].strip()
zip_code = address_parts[3].strip()

# Create a customer
customer = Customer(customer_name, '', customer_email, customer_phone)

# Create an address object using the address details from secrets
address = Address(street, city, state, zip_code)

# Find the closest Domino's store
store = address.closest_store()

# Print the store information
print(f'Closest store ID: {store.store_id}')
print(f'Store address: {store.address}')
print(f'Store phone number: {store.phone}')
