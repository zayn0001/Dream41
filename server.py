import openai

def assist(team1, team2, players1, players2,apikey):

    client = openai.OpenAI(api_key=apikey)
    assistant = client.beta.assistants.create(
    instructions="You are a helpful housing support assistant and you answer questions based on the files provided to you.",
  model="gpt-4-turbo",
  tools=[{"type": "file_search"}],
  tool_resources={
    "file_search": {
      "vector_store_ids": ["vs_74DhNUKh6sErnaaSk5sT2X9e"]
    }
  }
  ) 
    thread = client.beta.threads.create()

    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions=f"Dream11 is a well-known fantasy sports platform where participants build virtual teams from real-life cricket players and earn points based on those players' performances in live matches. \
Create 15 unique fantasy cricket teams, each designed to maximize winning potential in a fantasy league setting. Utilize comprehensive player data to assess past performances and predict future success within fantasy sports.\
To create a team for IPL Fantasy Cricket 2024 on Dream11 there are certain rules to follow. To build a solid Fantasy IPL team, you must have a combination of players listed below to make a solid squad.\
\
\
Combination Type C1	C2	C3	C4	C5	C6	C7\
\
Wicket-Keeper   1	  1   1	  1	  1	  1	  1\
Batsman	        5	  5	  4	  4	  4	  3	  3\
All-Rounder	    2	  1	  1	  2	  3	  2	  3\
Bowler	        3	  4	  5	  4	  3	  5	  4\
TOTAL	          11  11  11  11  11  11  11\
\
Here's how your  IPL Fantasy team earns Fantasy points\
\
\
Main Points\
--------------\
\
Part of the starting XI- 4 Point\
Run scored- 1 Point\
Wicket taken (run-out excluded)- 25 Point\
Catch taken- 8 Point\
Caught & Bowled- 33 Point\
Stumping.Run Out (direct)- 12 Point\
Run Out (Thrower/Catcher)- 6/6 Point\
Dismissal for a Duck (Only for batsmen, wicket-keepers and all-rounders)- 2 Point\
\
Bonus Points\
---------------------\
Every boundary hit- 1 Point\
Every six hit- 2 Point\
Half-Century (50 runs scored by a batsman in a single inning)- 8 Point\
Century (100 runs scored by a batsman in a single inning- 16 Point\
Maiden over- 8 Point\
4 wickets- 8 Point\
5 wickets- 16 Point\
\
Economy Rate Points\
---------------------\
\
Between 6 and 5 runs per over- 2 Point\
Between 4.99 and 4 runs per over- 4 Point\
Below 4 runs per over- 6 Point\
Between 9 and 10 runs per over- 6 Point\
Between 10.01 and 11 runs per over- 4 Point\
Above 11 runs per over- 6 Point\
\
Strike Rate (Except Bowler) Points\
-----------------------------------\
\
Above 170 runs per 100 bowls- 6 Point\
Between 150.01-170 runs per 100 balls- 4 Point\
Between 130-150 runs per 100 balls- 2 Point\
Between 60-70 runs per 100 balls- -2 Point\
Between 50-59.99 runs per 100 balls- -4 Point\
Below 50 runs per 100 balls- -6 Point     \
\
\
I need to create 15 unique fantasy cricket teams based on specific player details. The team should be constructed in accordance with the fantasy league rules and the point system, taking into account the players' past performances from the csv provided. The columns team 1 bat 1, team 2 ball 2, etc correspond to the best batsmen and bowlers of the match. Ensure that the team created follows the valid combination constraints\
The 11 players can be selected from the mixture of these 2 teams\
\
Plyers and their role \
---------------------\
\
{team1}\
------------\
{players1}\
\
{team2}\
--------------\
{players2}\
\
\
The output should strictly adhere to the format provided, with no additional text.\
\
Output JSON Format:\
\
  \"player 1 name\":\"wicket-keeper\",\
  \"player 2 name\":\"batsman\"\
  ...\
\
Output:",
    )

    if run.status == 'completed': 

        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        
        contents = messages.data[0].content[0].text.value
        print(contents)
        contents.replace("```json","").replace("```","")
        return contents
