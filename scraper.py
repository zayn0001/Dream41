import requests
from bs4 import BeautifulSoup

def scrape_ipl_team_players(team_abbr):
    # Dictionary to store players

    ipl_teams = {
    "CSK": "Chennai Super Kings",
    "DC": "Delhi Capitals",
    "PBKS": "Punjab Kings",
    "KKR": "Kolkata Knight Riders",
    "MI": "Mumbai Indians",
    "RR": "Rajasthan Royals",
    "RCB": "Royal Challengers Bangalore",
    "SRH": "Sunrisers Hyderabad",
    "LSG":"Lucknow Super Giants",
    "GT":"Gujarat Titans"
    }

    team_name = ipl_teams[team_abbr]
    
    team_players = []
    # URL of the IPL team webpage
    url = f"https://www.iplt20.com/teams/{team_name.lower().replace(' ', '-')}"
    
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find batsmen
        players = soup.find_all('li', class_='dys-box-color ih-pcard1')
        for player in players:
            div = player.find("div",class_="ih-p-name")
            name = div.find('h2').text.strip()
            position = player.find('span',class_="d-block w-100 text-center").text.strip()
            
            team_players.append(name + " ("+position+")")
            
    return team_players


