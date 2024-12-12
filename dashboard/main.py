
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Set page layout
st.set_page_config(layout="wide")

def load_css():
    css = """
    .title {
        color: #007BFF; 
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }
    .info {
        background-color: #EAF6FF; 
        padding: 10px;
        border-radius: 10px;
        font-size: 18px;
        display: flex;
        justify-content: space-between;
        width: 100%;
    }
    .footer {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
    }
    .header {
        font-size: 27px;
        font-weight: bold;
        text-align: center;
    }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()


# Display title and user information
def display_header():
    st.markdown('<h1 class="title">BIKE SHARING DASHBOARD 🚲</h1>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="info">
            <p><strong>Name:</strong> Aini Nurpadilah</p>
            <p><strong>Email:</strong> aininurfadilah354@gmail.com</p>
            <p><strong>Dicoding ID:</strong> aininrp</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

display_header()

# Load and preprocess data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

main_df = load_data("hour.csv")

# Sidebar for date range selection
st.sidebar.header("Select Date Range")
start_date = st.sidebar.date_input("Start date:", value=main_df['dteday'].min())
end_date = st.sidebar.date_input("End date:", value=main_df['dteday'].max())

# Filter dataframe for selected date range
filtered_df = main_df[(main_df['dteday'] >= pd.Timestamp(start_date)) & (main_df['dteday'] <= pd.Timestamp(end_date))]

# Calculate and display metrics
def display_metrics(filtered_df):
    registered_total = filtered_df['registered'].sum()
    casual_total = filtered_df['casual'].sum()
    total_rentals = registered_total + casual_total

    st.markdown('<h1 class="header">Registered and Casual User</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Total Registered Users", value=registered_total)
    with col2:
        st.metric(label="Total Casual Users", value=casual_total)
    with col3:
        st.metric(label="Total Rentals", value=total_rentals)

display_metrics(filtered_df)

# Create and display monthly rentals plot
def plot_monthly_rentals(df):
    df['month'] = df['dteday'].dt.to_period('M')
    monthly_df = df.groupby('month').agg({
        'registered': 'sum',
        'casual': 'sum'
    }).reset_index()

    monthly_df['month'] = monthly_df['month'].dt.to_timestamp()
    monthly_df['total_rentals'] = monthly_df['registered'] + monthly_df['casual']

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(monthly_df['month'], monthly_df['registered'], marker='o', label='Registered Rentals', color='#4CAF50')
    ax.plot(monthly_df['month'], monthly_df['casual'], marker='o', label='Casual Rentals', color='#FF9800')

    ax.set_xlabel("Month")
    ax.set_ylabel("Total Customers")
    ax.set_title("Monthly Bike Rentals", fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True)
    st.pyplot(fig)

plot_monthly_rentals(main_df)

# Display pie chart for user types
def plot_user_types(registered_total, casual_total):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie([registered_total, casual_total], labels=['Registered', 'Casual'], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FF9800'])
    st.markdown('<h1 class="header">Percentage of Registered vs Casual Users</h1>', unsafe_allow_html=True)
    st.pyplot(fig)

plot_user_types(filtered_df['registered'].sum(), filtered_df['casual'].sum())

# Display seasonal rentals
st.markdown('<h1 class="header">Users Based On Seasons</h1>', unsafe_allow_html=True)
def display_seasonal_rentals(df):
    season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season'] = df['season'].map(season_map)

    seasonal_df = df.groupby('season').agg({'registered': 'sum', 'casual': 'sum'}).reset_index()
    seasonal_df['total_rentals'] = seasonal_df['registered'] + seasonal_df['casual']

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(seasonal_df['season'], seasonal_df['total_rentals'], color=['#4CAF50', '#FF9800', '#2196F3', '#9C27B0'])
    ax.set_xlabel("Season")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Seasonal Bike Rentals", fontsize=14)
    st.pyplot(fig)

display_seasonal_rentals(filtered_df)

# Display rentals by day of the week
def display_day_rentals(df):
    df['day_of_week'] = df['dteday'].dt.dayofweek
    day_map = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
        4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }
    df['day_name'] = df['day_of_week'].map(day_map)

    day_df = df.groupby('day_name').agg({'registered': 'sum', 'casual': 'sum'}).reset_index()
    day_df['total_rentals'] = day_df['registered'] + day_df['casual']
    day_df['day_name'] = pd.Categorical(day_df['day_name'], categories=list(day_map.values()), ordered=True)
    day_df.sort_values(by='day_name', inplace=True)

    highest_day = day_df.loc[day_df['total_rentals'].idxmax()]

    st.markdown('<h1 class="header">Day with Highest Rentals</h1>', unsafe_allow_html=True)
    st.write(f"**{highest_day['day_name']}** has the highest rentals with **{highest_day['total_rentals']}** rentals.")

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        day_df['day_name'],
        day_df['total_rentals'],
        color=['#4CAF50' if day == highest_day['day_name'] else '#FF9800' for day in day_df['day_name']]
    )

    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():,}', ha='center', va='bottom')

    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Bike Rentals by Day", fontsize=16)
    st.pyplot(fig)

display_day_rentals(main_df)

# Display rentals by hour
def display_hour_rentals(df):
    hour_df = df.groupby('hr').agg({'registered': 'sum', 'casual': 'sum'}).reset_index()
    hour_df['total_rentals'] = hour_df['registered'] + hour_df['casual']

    busiest_hour = hour_df.loc[hour_df['total_rentals'].idxmax()]

    st.markdown('<h1 class="header">Busiest Hour</h1>', unsafe_allow_html=True)
    st.write(f"The busiest hour is **{busiest_hour['hr']} o'clock**.")

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(
        hour_df['hr'],
        hour_df['total_rentals'],
        color=['#4CAF50' if hr == busiest_hour['hr'] else '#FF9800' for hr in hour_df['hr']]
    )

    ax.set_xlabel("Hour of the Day")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Bike Rentals by Hour", fontsize=16)
    st.pyplot(fig)

display_hour_rentals(filtered_df)

# Footer
def display_footer():
    st.markdown('<h1 class="footer">&copy; Aini Nurpadilah 2024</h1>', unsafe_allow_html=True)

display_footer()