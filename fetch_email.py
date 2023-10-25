import requests
import re

# URL of the webpage to search
url = "https://www.stortinget.no/no/Stottemeny/kontakt/representanter-og-partigrupper/Representantenes-e-postadresser/"  # Replace with the URL of the webpage you want to search

# Your email ending to search for
email = "@stortinget.no" 

response = requests.get(url)

if response.status_code == 200:

    pattern = r"<td><a href='mailto:(.*?){}'>".format(email)
    matches = re.findall(pattern, response.text, re.DOTALL)

    if matches:
        for i, match in enumerate(matches):
            extracted_text = match.strip()
            print(f"Occurrence {i + 1}: {extracted_text}")
        formatted_occurrences = [f"{match.strip()}{email}" for match in matches]
        comma_separated_list = ", ".join(formatted_occurrences)
        print(f"Comma-separated list of e-mails: {comma_separated_list}")  
    else:
        print("No matching text found")
else:
    print("Failed to retrieve the webpage. Check URL or your internet connection.")
