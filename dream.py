import streamlit as st
import server
import json


ipl_teams = ['CSK', 'DC', 'KKR', 'MI', 'PBKS', 'RR', 'RCB', 'SRH','GT','LSG']

example_format = """
Enter player names in the following format:\n
Sam Curran (All-Rounder)\n
Prabhsimran Singh (Batsman)\n
Rilee Rossouw (Batsman)\n
Liam Livingstone (All-Rounder)\n
Harpreet Singh Bhatia (Batsman)\n
Shashank Singh (Batsman)\n
Jitesh Sharma (Wicket-Keeper)\n
Ashutosh Sharma (Batsman)\n
Harpreet Brar (Bowler)\n
Harshal Patel (Bowler)\n
Kagiso Rabada (Bowler)\n
"""

def main():
    st.title("Dream 11 Helper")
    apikey = st.text_input("OpenAI API KEY")
    team1 = st.selectbox('Team 1', ipl_teams)
    team2 = st.selectbox('Team 2', [x for x in ipl_teams if x!=team1])
   

    st.write(example_format)
    players1 = st.text_area(team1 + " players and their roles", key="players")
    players2 = st.text_area(team2 + " players and their roles", key="players2")
    if players2 and players1:
        ans = server.assist(team1,team2,players1,players2, apikey)
        ans = ans.replace("```json","").replace("```","")
        ans = json.loads(ans)
        st.write(ans)



        

if __name__ == "__main__":
    main()
