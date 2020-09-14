mydictionary = {'sprocket': 5, 'widgets': 11, 'cogs': 3, 'gizoms': 15}

print('mydictionary ->', mydictionary)
print('mydictionary["gaddets"] = 1')
mydictionary['gaddets'] = 1
print('mydictionary ->', mydictionary)
print('del mydictionary["gaddets"]')
del mydictionary['gaddets']
print('mydictionary ->', mydictionary)

print('-----------------------------------------------------------------------')
# 

phone_dictionary = {"David" : "4045551234", "Lucy" : "4045555678",
                "Vrushali" : "4045559101"}

print('phone_dictionary ->', phone_dictionary)
# check if a key is exist in dictionay and then adding new phone number
print('check if "David" key is in phone_dictionary, if not we will adding\
    the new key and its value, otherwise we will add the key with different name')
if 'David' in phone_dictionary:
    print('David is already in phone_dictionary')
    phone_dictionary['David2'] = '4045551121'
else:
    mydictionary['David'] = '4045551121'
print(phone_dictionary)

try:
    print(phone_dictionary['kais'])
    # phone_dictionary['kais'] = '+213662063212'
except Exception as identifier:
    print(f'error - the key {identifier} doesn\'t exist')

