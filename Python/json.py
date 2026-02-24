import json
json_data = '''
{
    "id": 235,
    "brand": "Nike",
    "qty": 84,
    "Status": {
        "isForSale": true
    }
}
'''
sneakers = json.loads(json_data)
print(type(sneakers))




# JSON --> Data Exchange format and file format 
# JSON stands for JavaScript Object Notation. It is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate. JSON is often used to transmit data between a server and a web application as an alternative to XML.
# {
#     "id": 235,
#     "brand": "Nike",
#     "qty": 84,
#     "Status": {
#         "isForSale": true,
#     }
# }

# CONVERTING JSON to dictionary in Python




