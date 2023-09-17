import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
MONTH_DATA = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Auguest', 'September', 'October', 'November', 'December']
DAY_DATA = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # DONE: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        # Get user input for city (chicago, new york city, washington)
        city = input('Hello! Let\'s explore some US bikeshare data!\nWould you like to see data for Chicago, New York City, or Washington?\n').title()
        if city in CITY_DATA.keys():
            # DONE: get user input for month (all, january, february, ... , june)
            month = input('Which month do you like to filter by? Please type: January, February, March, April, May, June, July, Auguest, September, October, November, December or All(including all month)!\n').title()
            if (month in MONTH_DATA) or (month == 'All'):
                # DONE: get user input for day of week (all, monday, tuesday, ... sunday),
                day = input('Which day? Please type your response as Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All(including all weekdays)\n').title()
                if day in DAY_DATA:
                    print('{} is an avaliable day'.format(day))
                elif day == 'All':
                    print('Day is ', day)
                else:
                    print('{} is NOT an avaliable day'.format(day))
                    continue
            else:
                print('{} is NOT an avaliable month'.format(month))
                continue
        else:
            print('{} is NOT an avaliable city'.format(city))
            continue    
        break

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
   
    # filter by month if applicable
    if month != 'All':
        # Filter by month to create the new dataframe
        # user inputs should be made case insensitive,
        # which means the input should accept the string of "Chicago" and its case variants
        # such as "chicago", "CHICAGO", or "cHicAgo"
        df = df[df['month'] == month.title()]
    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # DONE: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month: ', popular_month)
    # DONE: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day: ', popular_day)
    # DONE: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # DONE: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', popular_start_station)
    # DONE: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ', popular_end_station)

    # DONE: display most frequent combination of start station and end station trip
    df['Start End Station'] = df ['Start Station'].astype (str) + '-' + df ['End Station'].astype (str)
    popular_start_station = df['Start End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip: ', popular_start_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # DONE: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)
    # DONE: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats_all(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # DONE: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of user types: ', user_type_count)
    # DONE: Display counts of gender
    user_gender_count = df['Gender'].value_counts()
    print('Counts of user gender: ', user_gender_count)

    # DONE: Display earliest, most recent, and most common year of birth
    user_earliest_birth = df['Birth Year'].min()
    print('Earliest birth year of users: ', user_earliest_birth)
   
    user_recent_birth = df['Birth Year'].max()
    print('Recent birth year of users: ', user_recent_birth)
   
    user_common_birth = df['Birth Year'].mode()[0]
    print('Most common birth year of users: ', user_common_birth)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # DONE: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of user types: ', user_type_count)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data_present(df):
    """Displays raw data of the table."""
    start_loc = 0
    print('\nCalculating Raw Data Presenting...\n')
    start_time = time.time()
    load_more = input('\nDo you want to see the first 5 rows of data? Enter yes or no.\n')
    # DONE: Display raw data of the filter
    while True:
        if load_more.lower() == 'yes':
            print(df.iloc[start_loc:start_loc+5])    
            start_loc += 5
            load_more = input('\nDo you want to see the next 5 rows of data? Enter yes or no.\n')
        elif load_more.lower() == 'no':
            break
        else:
            print('Your input is invalid')
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        # Use descriptive statistics to answer questions about the data.
        # Raw data is displayed upon request by the user.
        city, month, day = get_filters()
        print('City: {}， Month: {}， Day: {}'.format(city, month, day))
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        if city != 'Washington':
           user_stats_all(df)
        else:
            user_stats(df)
        raw_data_present(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
