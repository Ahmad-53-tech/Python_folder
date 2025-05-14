# Web Scrapping is a way you scrape the HTML content of a page to get the data you want if the API url is not provided.
# BEAUTIFUL SOUP is an HTML parser that we use to make sense of the HTML.

#
#
#                                                  HOW DOES HTML PARSING WORK
# * The browser fetches the HTML: When you visit a webpage, the browser downloads the HTML file from the web server.
# * Tokenization: The browser breaks down the HTML codes into tokens (individual element like <h1>, <p>, <a> etc.).
# * Building the DOM (Document Object Model): The browser creates a tree-like structure where each HTML element is a node. This structure is called the
#   DOM. Think of the DOM like a family tree where each HTML tag is a node like a family member. Parent nodes contain child node (just like a parent has
#   children)
# * Rendering the page: The browser applies styles(CSS) executes scripts(javascript) and displays the final webpage to the user.
#
#
#
#                                               WHY IS THE HTML PARSING IMPORTANT
# It ensures that HTML is properly structured before displaying content
#
#
#
#                                               METHODS IN BEAUTIFULSOUP
# * Find: It gets the first matching element. It finds the occurrence of a tag that matches the criteria. It is used when you only need one element. It
#          returns a single beautifulsoup element or none if not found. It is also used when you only need one element like the first <p> tag or <h> tag.
# * Find_all: It finds all occurrences of a tag that matches a criteria. It returns a list of beautifulsoup element and an empty list if none are found
#   It is used when you need multiple elements like all <p> tags or all <a> links.
# * Select_one: It finds the first matching element using CSS selectors. It is used when you prefer CSS selectors instead of tag names.
# * Select: It finds all matching elements using CSS selectors.
# * Prettify: It indexes the HTML code in a more readable way.
# * getText: It is used to get all texts in a tag.




