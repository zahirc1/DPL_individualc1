
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/electric_vehicles.csv")
    return df

df = load_data()

# Title
st.title("Electric Vehicle Population Dashboard")

# Filters
make_options = df['Make'].dropna().unique()
selected_make = st.multiselect("Select Make(s)", make_options, default=make_options[:3])

filtered_df = df[df['Make'].isin(selected_make)]

# Visualizations
st.subheader("Electric Vehicle Distribution by Model")
model_counts = filtered_df['Model'].value_counts().reset_index()
model_counts.columns = ['Model', 'Count']
fig1 = px.bar(model_counts.head(10), x='Model', y='Count', title='Top 10 EV Models')
st.plotly_chart(fig1)

st.subheader("EV Types by Electric Range")
if 'Electric Range' in filtered_df.columns:
    fig2 = px.box(filtered_df, x='Electric Vehicle Type', y='Electric Range', points='all')
    st.plotly_chart(fig2)

st.subheader("Geographic Distribution (State-wise)")
if 'State' in filtered_df.columns:
    state_counts = filtered_df['State'].value_counts().reset_index()
    state_counts.columns = ['State', 'Count']
    fig3 = px.choropleth(state_counts, 
                         locations='State',
                         locationmode="USA-states",
                         color='Count',
                         scope="usa",
                         title="EVs by State")
    st.plotly_chart(fig3)

st.write("Dataset Preview:")
st.dataframe(filtered_df.head())
