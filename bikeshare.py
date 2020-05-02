# Project Name - Bikeshare Data Analysis
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # used lower() and strip() functions to handle invalid inputs

    city = input('\nEnter name of the city to analyze from Chicago, New York City or Washington : ').lower().strip()

    while city not in CITY_DATA.keys():
        print('\nYou entered an invalid city name: {} '.format(city))
        city = input('\nEnter name of the city to analyze from Chicago, New York City or Washington : ').lower().strip()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nEnter name of the month to filter by from January to June, or "all" to apply no month filter: ').lower().strip()

    months_check_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months_check_list:
        print('\nYou entered an invalid month: {} '.format(month))
        month = input('\nEnter name of the month to filter by from January to June, or "all" to apply no month filter: ').lower().strip()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nEnter day of week like 1-Monday, 2-Tuesday, 0-Sunday or "all" to apply no day filter : ').strip()

    days_check_list = ['0','1','2','3','4','5','6','all']
    while day not in days_check_list:
        print('\nYou entered the day in wrong format')
        day = input('\nEnter day of week like 1-Monday, 2-Tuesday, 0-Sunday or "all" to apply no day filter : ').strip()


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

    # loading data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converting start time column to date time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracting month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == int(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nMost common month: {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_dow = df['day_of_week'].mode()[0]
    print('\nMost common day of week: {}'.format(most_common_dow))


    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\nMost common start hour: {}'.format(most_common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_used_start_stn = df['Start Station'].mode()[0]
    print('\n Most commonly used start station is: {}'.format(most_used_start_stn))


    # TO DO: display most commonly used end station

    most_used_end_stn = df['End Station'].mode()[0]
    print('\n Most commonly used end station is: {}'.format(most_used_end_stn))


    # TO DO: display most frequent combination of start station and end station trip

    # adding start and end station concatenated column to the data frame.
    df['start_end_station'] = df['Start Station']+'---'+df['End Station']

    most_used_start_end_stn = df['start_end_station'].mode()[0]

    print('\n Most commonly used start and end station are: {}'.format(most_used_start_end_stn))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()/3600

    print('\n Total travel time in hours: {}'.format(total_travel_time))


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()/3600

    print('\n Mean travel time in hours: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = dict(df['User Type'].value_counts())

    print('\n Displaying the counts of user types:\n {}'.format(counts_of_user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = dict(df['Gender'].value_counts())
        print('\n Displaying the counts of gender:\n {}'.format(counts_of_gender))
    else:
        print('\n No Gender information available')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob = int(df['Birth Year'].min())
        most_recent_yob = int(df['Birth Year'].max())
        most_common_yob = int(df['Birth Year'].mode()[0])

        print('\n Earliest year of birth: {}\n Most recent year of birth: {}\n Most common year of birth: {}'.format(earliest_yob,most_recent_yob,most_common_yob))
    else:
        print('\n No Birth Year information available')

        print("\nThis took %s seconds." % (time.time() - start_time))

        print('-'*40)

def display_raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """
    data = 0
    while True:
        answer = input('Would you like to see 5 rows of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[data : data+5])
            data += 5

        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
