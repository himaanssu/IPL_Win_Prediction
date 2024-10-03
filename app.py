import streamlit as st
import pickle
import pandas as pd

# List of IPL teams
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bengaluru',
    'Kolkata Knight Riders',
    'Punjab Kings',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals',
    'Gujarat Titans',
    'Lucknow Super Giants'
]

# List of cities where matches can be hosted
cities = [
    'Bengaluru', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
    'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
    'Centurion', 'East London', 'Johannesburg', 'Kimberley',
    'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
    'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Indore',
    'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati', 'Mohali'
]

# Load the pre-trained model using pickle
pipe = pickle.load(open('pipe.pkl','rb'))

# Set the title of the Streamlit app
st.title('IPL Win Predictor')

# Create two columns for team selection
col1, col2 = st.columns(2)

# Select the batting team
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

# Select the bowling team
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

# Select the host city
selected_city = st.selectbox('Select host city', sorted(cities))

# Input for the target score as an integer
target = st.number_input('Target', min_value=0, step=1, format="%d")

# Create three columns for additional inputs
col3, col4, col5 = st.columns(3)

# Input for the present score as an integer
with col3:
    score = st.number_input('Present score', min_value=0, step=1, format="%d")

# Input for overs completed as an integer
with col4:
    overs = st.number_input('Overs completed', min_value=0, step=1, format="%d")

# Input for wickets out as an integer
with col5:
    wickets = st.number_input('Wickets out', min_value=0, step=1, format="%d")

# Button to predict probabilities
if st.button('Predict Probability'):
    # Calculate runs left, balls left, wickets left, CRR, and RRR
    runs_left = target - score
    balls_left = 120 - (overs * 6)  # 120 balls in total for T20
    wickets_left = 10 - wickets
    crr = score / overs if overs > 0 else 0  # Current Run Rate
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0  # Required Run Rate

    # Create a DataFrame for the input features
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'inning1_runs': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    # Get prediction probabilities
    result = pipe.predict_proba(input_df)
    loss = result[0][0]  # Probability of losing
    win = result[0][1]   # Probability of winning

    # Display the results with two decimal places
    st.header(f"{batting_team} - {win * 100:.2f}%")  # Winning probability
    st.header(f"{bowling_team} - {loss * 100:.2f}%")  # Losing probability