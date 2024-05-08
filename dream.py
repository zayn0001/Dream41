import streamlit as st
import server
import json
import scraper

ipl_teams = ['CSK', 'DC', 'KKR', 'MI', 'PBKS', 'RR', 'RCB', 'SRH','GT','LSG']

global mteam1
mteam1 = ""
global mteam2
mteam2 = ""
global mteam1_players
mteam1_players = []
global mteam2_players
mteam2_players = []

def getteam1players(team):
    global mteam1_players,mteam1

    if mteam1 != team:
        mteam1 = team
        mteam1_players = scraper.scrape_ipl_team_players(team)

def getteam2players(team):
    global mteam2_players,mteam2
    if mteam2 != team:
        mteam2 = team
        mteam2_players = scraper.scrape_ipl_team_players(team)


def main():
    global mteam1_players, mteam2_players
    st.title("Dream 11 Helper")
    apikey = st.text_input("OpenAI API KEY")

    team1 = st.selectbox('Team 1', ipl_teams)
    getteam1players(team1)
    
    selected_team1_players = st.multiselect('Select Active Players:', mteam1_players)
    

    team2 = st.selectbox('Team 2', [x for x in ipl_teams if x!=team1])
    getteam2players(team2)

    selected_team2_players = st.multiselect('Select Active Players:', mteam2_players)

    
    if st.button('Submit'):
        players1 = ""
        players2 = ""

        for bat in selected_team1_players:
            players1 = players1 + bat + "\n"
        players1 += "\n"

        for bat in selected_team2_players:
            players2 = players2 + bat + "\n"
        players2 += "\n"

        ans = server.assist(team1,team2,players1,players2, apikey)
        ans = ans.replace("```json","").replace("```","")
        ans = json.loads(ans)
        st.write(ans)



        

if __name__ == "__main__":
    main()
