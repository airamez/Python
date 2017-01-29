"""
   Write a program to read the the first name, last name, email and address of a costumer and
   print all information following the template below:
   -------------------------------------------------------------------------------------------------------
   First Name: [first name]; Last Name: [last name]; email: [email]
   Address: Suite #: [suite number]; Street#: [street number]; Street: [street name]
            City: [city]; Province/State: [province/state]; Country: [country]; Postal Code: [postal code]
   -------------------------------------------------------------------------------------------------------
   Attention: Make sure the program assists the user during the data entry
"""
first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email: ")

suite_number = input("Suite #: ")
street_number = input("Street Number: ")
street_name = input("Street Name: ")

city = input("City: ")
province_or_state = input("Province/State: ")
country = input("Country: ")
postal_code = input("Postal Code: ")

# Option 1
print("-------------------------------------------------------------------------------------------------------")
print("First Name: {0}; Last Name: {1}; email: {2}".format(first_name, last_name, email))
print("Address: Suite #: {0}; Street#: {1} Street: {2}".format(suite_number, street_number, street_name))
print("         City: {0}; Province/State: {1}; Country: {2}; Postal Code: {3}"
      .format(city, province_or_state, country, postal_code))
print("-------------------------------------------------------------------------------------------------------")

# Option 2
template = """-------------------------------------------------------------------------------------------------------
First Name: {first_name}; Last Name: {last_name}; email: {email}
Address: Suite #: {suite_number}; Street#: {street_number}; Street: {street_name}
         City: {city}; Province/State: {province_or_state}; Country: {country}; Postal Code: {postal_code}
-------------------------------------------------------------------------------------------------------"""

data = template.format(first_name=first_name,
                       last_name=last_name,
                       email=email,
                       suite_number=suite_number,
                       street_number=street_number,
                       street_name=street_name,
                       city=city,
                       province_or_state=province_or_state,
                       country=country,
                       postal_code=postal_code)

print(data)


