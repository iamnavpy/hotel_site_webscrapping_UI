import requests
from bs4 import BeautifulSoup

def extract_unit_details(url):
    url='https://chapterkingscross.prospectportal.global/Apartments/module/application_unit_info/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    unit_details = soup.find_all('div', class_='sus-unit-space-details')

    extracted_details = []
    for unit in unit_details:
        building = unit.find('dt', class_='title', text='Building').find_next_sibling('dd').text.strip()
        rent = unit.find('dt', class_='title', text='Rent').find_next_sibling('dd').text.strip()
        deposit = unit.find('dt', class_='title', text='Deposit').find_next_sibling('dd').text.strip()
        amenities = unit.find('dt', class_='title', text='Amenities').find_next_sibling('dd').text.strip()

        extracted_details.append({
            'building': building,
            'rent': rent,
            'deposit': deposit,
            'amenities': amenities
        })

    return extracted_details