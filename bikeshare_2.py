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

    city = input("Please enter the city for which you'd like to analyze bikeshare data (Chicago, New York City, or Washington): ").lower()
    while city not in CITY_DATA.keys():
        city = input("The city you entered is not a valid city. Please enter a valid city: ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter the month for which you'd like to analyze bikeshare data (January-June). Enter 'all' if you'd like to analyze data for all months: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input("The month you entered is not a valid month. Please enter a valid month: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Please enter the day of the week for which you'd like to analyze bikeshare data, or enter 'all' if you'd like to analyze data for all days of the week: ").lower()
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("The day you entered is not a valid day. Please enter a valid day: ").lower()


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
    if city == "new york city":
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv(city + '.csv')

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month of Trip'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['Weekday of Trip'] = df['Start Time'].dt.strftime('%A').str.lower()
    df['Start Hour'] = df['Start Time'].dt.hour

    if month != "all" and day != "all":
        df = df[(df['Month of Trip'] == month) & (df['Weekday of Trip'] == day)]
    elif day != "all":
        df = df[df['Weekday of Trip'] == day]
    elif month != "all":
        df = df[df['Month of Trip'] == month]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print("\nThe most frequently traveled month is: ", df['Month of Trip'].mode().to_string(index=False))

    # TO DO: display the most common day of week

    print("\nThe most frequently traveled weekday is: ", df['Weekday of Trip'].mode().to_string(index=False))

    # TO DO: display the most common start hour

    print("\nThe most common start hour is: ", df['Start Hour'].mode().to_string(index=False))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("\nThe most common start station is: ", df['Start Station'].mode().to_string(index=False))

    # TO DO: display most commonly used end station

    print("\nThe most common end station is: ", df['End Station'].mode().to_string(index=False))

    # TO DO: display most frequent combination of start station and end station trip

    print("\nThe most frequent trip is: ", (df['Start Station'] + ' to ' + df['End Station']).mode().to_string(index=False))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("The total travel time is: ", (df['End Time'] - df['Start Time']).sum())

    # TO DO: display mean travel time

    print("\nThe average travel time is: ", (df['End Time'] - df['Start Time']).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print("Here is data on number of trips by the different user types:\n", df['User Type'].value_counts().to_string(index=True))

    # TO DO: Display counts of gender
    while True:
        try:
            print("\nHere is data on number of trips by gender:\n", df['Gender'].value_counts().to_string(index=True))
            break
        except:
            print("\nGender data is not available for this city.")
            break

    # TO DO: Display earliest, most recent, and most common year of birth

    while True:
        try:
            print("The oldest user was born in: ", df['Birth Year'].min())
            print("The youngest user was born in: ", df['Birth Year'].max())
            print("The most common birth year for users was: ", df['Birth Year'].mode().to_string(index=False))
            break
        except:
            print("\nBirth Year data is not available for this city.")
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    display_data = 'yes'
    times_through = 1
    x = 0
    i = 0

    ##while more_data == 'yes':
        ## more_data = input("Would you like to see the raw data? ").lower()
        ## if more_data != 'yes':
        ##     break
        ## print(df.iloc[x:times_through * 5])
        ## x = times_through * 5
        ## times_through += 1

    while True:
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if display_data.lower() != 'yes':
            break
        print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
        i+=5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
