

bioData = {"Name" : "Abisheak",
           "Age" : "23",
           "City" : "Marthandam",
           "Qualification" : {
               "Degree" : "B.Sc. Perfusion Technology",
               "Studying" : "Python, JavaScript",
               "Japanese" : "N3 Level"}}

print(bioData) #prints every data inside the bioData variable

#to access the individual data use square brackets or .get() method
print(bioData["Name"])
print(bioData.get("Qualification")["Japanese"])
