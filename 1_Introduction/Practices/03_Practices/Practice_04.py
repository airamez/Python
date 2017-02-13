"""
Write a program with the same input as the previous one but printing the data using the formatting below:
{
 "first_name" : "[first name]",
 "last_name" : "[last name]",
 "email" : "[email]",
 "address" : {
   "suite_number" : "[suite number]",
   "street_number" : "[street number]",
   "street_name"  : "[street name]",
   "city" : "[city]",
   "province_state" : "[province/estate]",
   "country" : "[country]",
   "postal_code" : "[postal code]"
 }
}
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

template = '''
{{
 "first_name" : "{first_name}",
 "last_name" : "{last_name}",
 "email" : "{email}",
 "address" : {{
   "suite_number" : "{suite_number}",
   "street_number" : "{street_number}",
   "street_name"  : "{street_name}",
   "city" : "{city}",
   "province_state" : "{province_or_state}",
   "country" : "{country}",
   "postal_code" : "{postal_code}"
 }}
}}
'''

data = template.format(**locals())

print(data)
