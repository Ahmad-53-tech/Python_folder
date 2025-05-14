from bs4 import BeautifulSoup


#Load and parse the website.html file
with open('my_file.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')


#Extract and print the entire <title> tag
title_tag = soup.title
print("Entire <title> tag:")
print(title_tag)


#Extract and print the name of the <title> tag
print("\nName of <title> tag:")
print(title_tag.name)


# Extract and print the text inside the <title> tag
print("\nText inside the <title> tag:")
print(title_tag.string)


# Print the formatted (prettified) HTML code
print("\nPrettified HTML code:")
print(soup.prettify())


# Extract and print the first <a> tag in the document
first_a_tag = soup.find('a')
print("\nFirst <a> tag:")
print(first_a_tag)


# Extract and print a list of all <a> tags
a_tags = soup.find_all('a')
print("\nAll <a> tags:")
for a in a_tags:
    print(a)


# Extract and print the text inside each <a> tag
print("\nText inside each <a> tag:")
for a in a_tags:
    print(a.get_text())


# Extract and print the href attributes of all <a> tags
print("\nHref attributes of all <a> tags:")
for a in a_tags:
    print(a.get('href'))


# Extract and print the text inside the <h1> tag with an id of "name"
h1_name = soup.find('h1', id='name')
print("\nText inside the <h1> tag with id='name':")
print(h1_name.get_text() if h1_name else "No <h1> tag with id='name' found.")


# Extract and print the text inside the first <h3> tag with a class of "heading"
h3_heading = soup.find('h3', class_='heading')
print("\nText inside the first <h3> tag with class='heading':")
print(h3_heading.get_text() if h3_heading else "No <h3> tag with class='heading' found.")


# Extract and print all items inside the <ul> list
ul_items = soup.find_all('ul')
print("\nAll items inside <ul> list:")
for ul in ul_items:
    for li in ul.find_all('li'):
        print(li.get_text())


# Modify and print the text inside the <h1> tag to "Student Name" instead of "Divine"
if h1_name:
    h1_name.string = "Student Name"
    print("\nModified <h1> tag text:")
    print(h1_name.get_text())
else:
    print("\nNo <h1> tag with id='name' found to modify.")