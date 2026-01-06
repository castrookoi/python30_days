#string Concatenation
string1 = 'Thirthy'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
space = ' '
result = string1 + space + string2 + space + string3 + space + string4
print(result)

#string Concatenation2
result2 = 'Coding' + space + 'For' + space + 'All'
print(result2)


#Reasign value
company = "Coding For All"

#Print Company
print(company)

#Print lenght of company
print(len(company))

#Change all characters to upper case
print(company.upper())

#Change all characters to lower case
print(company.lower())

#use Capitalize(), Title(),Swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Slice out the first word of the string.
first_word = company [0:6]
print(first_word)

#check for the work coding using index, find or other methods.
print('Coding' in company)
print(company.find('Coding'))
print(company.index('Coding'))

#Repace the word i a string
new_company = company.replace('Coding', 'python')
print(new_company)

#change string using replacement method
text = "Python for Everyone"
new_text = text.replace("Everyone", "All")
print(new_text)

#Split the String 'Coding for All using space as the seperator
company = "Coding for All"
print(company.split())

#split "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

#what is the character a index 0 in the string "Coding For All"
print(company[0])

#what is the last index of the string "Coding For All"
print(len(company) -1)

#What character is at index 10 in "Coding For All"
print(company[10])
