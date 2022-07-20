from bs4 import BeautifulSoup
import requests

cnic = int(input("Enter CNIC No: "))
postdata = {"cnicNumber": cnic}
print("Please Wait While Value is being getting......")
response = requests.post('https://cnic.com.pk/', postdata)
if response.status_code != 200:
    print("Error Occurred....")

else:
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {"class": "result"})
    counter = 0;
    for td in div:
        rows = ''
        row = td.find_all_next('td')
        # print(row)
        for rows in row:
            counter += 1
            if counter > 0 and counter < 10:
                print(rows.text)
    # print(td)
