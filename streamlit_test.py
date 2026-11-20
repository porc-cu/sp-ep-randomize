import streamlit as st

st.title("South Park Episode Randomizer")

import random
season = random.randint(0, 29)

ep_ndict = {1:13, 2:18, 3:17, 4:17, 5:14, 6:17, 7:15, 8:14, 9:14, 10:14, 
            11:14, 12:14, 13:14, 14:14, 15:14, 16:14, 17:10, 18:10, 19:10, 20:10, 
            21:10, 22:10, 23:10, 24:2, 25:6, 26:6, 27:5, 28:5, 29:6}

if season in range(1, 30):
    ep = random.randint(1, ep_ndict[season])
else:
    season = "Special"
    ep = "Hold on I'm working on it"

st.header(f"Season {season}, Episode {ep}")
st.write("Refresh the page to get a new episode (while I figure out how to put in an auto reset button & include the specials lol)")