from bs4 import BeautifulSoup
import requests
''''' 
in case you discovered this then i should tell you that this is just my first day of python learning cnic info 
is done using scraping from website cnic.com.pk that i discovered from google.com if you want any of your website to 
be scraped feel free to contact me on twitter.
 '' '''

cnic = int(input("Enter CNIC No: "))
postdata = {"cnicNumber": cnic}
print("Please Wait While Value is being getting......")
response = requests.post('https://cnic.com.pk/', postdata)
if response.status_code != 200:
    print("Error Occurred....")

else:
    output = []
    soup = BeautifulSoup(response.text, 'html.parser')
    div = soup.find('div', {"class": "result"})
    counter = 0;
    for td in div:
        rows = ''
        row = td.find_all_next('td')
        # print(row)
        for rows in row:
            counter += 1
            if 0 < counter < 11:
                # print(rows.text)
                output.append(rows.text)

    finout = {"Name: ": output[1], "Tehsil: ": output[3], "Division: ": output[5], "CNIC: ": output[7],
              "Province: ": output[9]}
    finaloutput = "Name: " + finout["Name: "] + "\n" + "Tehsil: " + finout["Tehsil: "] + "\n" + "Division: " + finout[
        "Division: "] + "\n" + "CNIC: " + finout["CNIC: "] + "\n" + "Province: " + finout["Province: "] + "\n"
    print(finaloutput)
    print("Do You Want Do Download File? \n 1.Yes \n 2.No")
    if int(input("Enter 1 or 2: ")) == 1:
        with open('userinfo ' + finout["CNIC: "] + ' .txt', 'w') as file:
            file.write(finaloutput)
            print("File is Downloaded")
    else:
        print("File is not downloaded")

    # print(finout)
