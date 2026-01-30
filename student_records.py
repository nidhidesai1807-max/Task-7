import json

#working with dictionary
insaan = {"naam":"Alexa",
          "umar": 21,
          "kaam": "vichaar"}
print("key=",insaan.keys())
print("Value of naam:",insaan["naam"])
insaan["kaam"]="Padhai"
del insaan["umar"]
for key,value in insaan.items():
    print(key,":",value)

#Converting dictionary to JSON file
insaan_json=json.dumps(insaan, indent=4)
#Saving
with open("insaan_data.json","w") as file:
    file.write(insaan_json)
#Reading
with open("insaan_data.json","r") as file:
    loaded_data = json.load(file)
#Printing output
print("\nData Record:")
for key,values in loaded_data.items():
    print(key, ":", value)
