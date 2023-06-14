import webbrowser
import requests
from bs4 import BeautifulSoup

# Function to perform the Google search and display the results
def run_dork(keyword, dork):
    if dork == 15:
        postman_search(keyword)
        return

    query = get_query(keyword, dork)

    print(f"\n----- Dork {dork} -----\n")
    print(f"Performing Google search for '{query}'...")

    search_results = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.select('a')

    for result in results:
        url = result.get('href')
        if url.startswith('/url?q='):
            url = url[7:]
            if 'google' not in url:
                search_results.append(url)

    if search_results:
        print("\n----- Search Results -----")
        for result in search_results:
            print(result)
    else:
        print("No results found.")

# Function to get the dork query based on the dork number
def get_query(keyword, dork):
    dork_queries = {
        1: f"site:github.com OR site:gitlab.com OR site:bitbucket.org {keyword}",
        2: f"site:s3.amazonaws.com {keyword}",
        3: f"site:{keyword} -www {keyword}",
        4: f"site:pastebin.com {keyword}",
        5: f"site:{keyword} intitle:phpinfo",
        6: f"site:{keyword} intitle:index of OR inurl:/logs",
        7: f"site:{keyword} intext:'SQL Error'",
        8: f"site:{keyword} intitle:apache +intext:conf | cnf | config",
        9: f"site:{keyword} intitle:index of OR inurl:/",
        10: f"site:{keyword} ext:sql OR ext:dbf OR ext:mdb",
        11: f"site:{keyword} ext:doc OR ext:docx OR ext:odt OR ext:pdf OR ext:rtf OR ext:sxw OR ext:psw OR ext:ppt OR ext:pptx OR ext:pps OR ext:csv",
        12: f"site:{keyword} inurl:readme OR inurl:license OR inurl:install OR inurl:setup OR inurl:config",
        13: f"site:{keyword} inurl:/phpinfo.php OR inurl:.htaccess",
        14: f"site:atlassian.net OR site:bitbucket.org {keyword}",
        15: f"https://www.postman.com/search?q={keyword}&scope=public&type=request"
    }
    return dork_queries.get(dork, "")

# Function to display the help menu
def display_help():
    print("Usage: python dork_search.py")
    print("Interactive Dork Search Menu:")
    print("1. GitHub, GitLab, Bitbucket Dork")
    print("2. S3 Bucket Dork")
    print("3. Subdomain Dork")
    print("4. Pastebin Dork")
    print("5. intitle:phpinfo Dork")
    print("6. Logs Dork")
    print("7. SQL Errors Dork")
    print("8. Apache Config Files Dork")
    print("9. Index and Directory Dork")
    print("10. Database Files Dork")
    print("11. File Extensions Dork")
    print("12. Specific Files in URLs Dork")
    print("13. PHP Info and .htaccess Files Dork")
    print("14. Atlassian and Bitbucket Dork")
    print("15. Postman Search")
    print("-h or --help: Display this help menu")

# Function to perform Postman search
def postman_search(keyword):
    query = get_query(keyword, 15)
    print(f"\n----- Postman Search -----\n")
    print(f"Postman search URL: {query}")
    webbrowser.open(query)


# Interactive menu
print("Welcome to Dork Search!")
print("This tool allows you to perform various Google dorks to search for specific information.")
print("Dork Search is developed by Shubham Pandey.")
print("Give credit to the developer and provide feedback to improve the tool.")
print("GitHub URL: https://github.com/shubhamvpandey")
print("LinkedIn URL: https://www.linkedin.com/in/shubham-pandey-10704014b/")

# Interactive menu
print("\nAvailable dorks:")
print("1. GitHub, GitLab, Bitbucket Dork")
print("2. S3 Bucket Dork")
print("3. Subdomain Dork")
print("4. Pastebin Dork")
print("5. intitle:phpinfo Dork")
print("6. Logs Dork")
print("7. SQL Errors Dork")
print("8. Apache Config Files Dork")
print("9. Index and Directory Dork")
print("10. Database Files Dork")
print("11. File Extensions Dork")
print("12. Specific Files in URLs Dork")
print("13. PHP Info and .htaccess Files Dork")
print("14. Atlassian and Bitbucket Dork")
print("15. Postman Search")
print("Enter 'all' to run all dorks.")

dork_input = input("Select a dork number or enter 'all': ")

if dork_input == "all":
    for i in range(1, 16):
        run_dork(keyword, i)
else:
    try:
        dork_number = int(dork_input)
        run_dork(keyword, dork_number)
    except ValueError:
        print("Invalid input. Please select a valid dork number.")

print("\nThank you for using Dork Search!")
