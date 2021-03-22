""""
Author:         Yaan Dalzell
Created:        24/01/2021

License:        All contents are the intellectual property of Yaan Dalzell
                Not to be used in any manner without written consent

Description:    Scrapes data from the given url
Last Valid On   24/01/2021
"""
from selenium import webdriver as web
from selenium.webdriver.firefox.options import Options
import sys
import json
from datetime import datetime
# Define target url
target_url = "https://www.marketindex.com.au/director-transactions"

# Web Driver
options = Options()
options.headless = True
driver = web.Firefox(options = options)

# Set ExtractDate
extract_date_time = str(datetime.now())
driver.get(target_url)

table = driver.find_element_by_tag_name("table")

if table:
    # Get header information
    header = table.find_element_by_tag_name("thead")
    extracted_fields = [field.text for field in header.find_elements_by_tag_name("th")]

    # Check that header fields are all present and accounted for
    expected_fields = ['Code', 'Company', 'Date', 'Director', 'Type', 'Amount', 'Price', 'Value']
    # Convert to sets for symmetric difference
    extracted_set = set(extracted_fields)
    expected_set = set(expected_fields)
    if extracted_set.symmetric_difference(expected_set):
        print(extracted_set.symmetric_difference(expected_set))
        raise Exception('Extracted fields are not as expected. Please investigate')
    # Incase the table order has changed (Happened before)
    code_field = extracted_fields.index("Code")
    company_field = extracted_fields.index("Company")
    date_field = extracted_fields.index("Date")
    director_field = extracted_fields.index("Director")
    type_field = extracted_fields.index("Type")
    amount_field = extracted_fields.index("Amount")
    price_field = extracted_fields.index("Price")
    value_field = extracted_fields.index("Value")


    # Discard Junk fields
    keys = extracted_fields[2:]

    # Get tables rows (excluding header)
    body = table.find_element_by_tag_name("tbody")
    rows = body.find_elements_by_tag_name("tr")
    outputs = []

    for row in rows:
        row_values = row.find_elements_by_tag_name("td")
        values = [value.text for value in row_values]
        temp = {
            "ExtractDateTime": extract_date_time,
            "CompanyCode": values[code_field],
            "CompanyName": values[company_field],
            "TransactionDate": values[date_field],
            "PersonName": values[director_field],
            "TransactionType": values[type_field],
            "NumberTraded": values[amount_field],
            "TradePrice": values[price_field],
            "TotalValue": values[value_field]
        }
        outputs.append(temp)

    # Return row data as a string
    # for row in rows:
    #     facts = [fact.text for fact in row.find_elements_by_tag_name("td")]

# print(outputs)

sys.stdout.write("{0}\n".format(json.dumps(outputs, sort_keys=True, indent=5)))

driver.quit()
