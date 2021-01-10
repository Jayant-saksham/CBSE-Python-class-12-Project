'''

BASIC OVERVIEW OF THE PROJECT (COVID-19) - 

THis is a program used to fetch the Covid-19 live data from two different API's
Python modules used : 
1. json - To parse the obtained data
2. requests - To request the API for data
3. win10toast - For notification toast

Python concept used :
1. STACKS - To storing the search history
2. Basic if else, f strings
3. Loops (for and while) 
4. User defined functions (Doc strings)
5. Try except handling - For handling the bugs if found

Others : 
API - API stands for Application Programming Interface which is a software intermediary that allows two applications to talk to each other

'''

import json
import requests
from win10toast import ToastNotifier
toaster = ToastNotifier()

# Defining data structure used
stacks = []

# Defining API links
countryAPI = 'https://disease.sh/v3/covid-19/countries'
indianAPI = 'https://api.covidindiatracker.com/state_data.json'


def saveHistory(region):
    ''' Function to save the history of the searched country or state of India'''

    try:
        stacks.append(region)

    except Exception as e:
        print("Something went wrong")
        toaster.show_toast(
            "Error",
            "Something went wrong",
            duration=6
        )


def printHistory():
    ''' Funtion for printing the search history '''

    if len(stacks) == 0:
        print("No history found")
        toaster.show_toast(
            "Not found",
            "No history found",
            duration=4
        )
    else:
        for i in range(len(stacks)-1, -1, -1):
            print(stacks[i])


def check_all_countries():
    ''' Function for printing all countries available'''

    response = requests.get(countryAPI)
    countries = json.loads(response.text)
    for i in range(len(countries)):
        print(f"{i+1}", countries[i]['country'])


def check_all_Indian_state():
    ''' Function for printing all state of India available'''

    response = requests.get(indianAPI)
    state = json.loads(response.text)
    for i in range(len(state)):
        print(f"{i+1}", state[i]['state'])


def covid19Precations():
    '''Function for printing Covid-19 precautions '''

    print("Clean your hands often. Use soap and water, or an alcohol-based hand rub.")
    print("Maintain a safe distance from anyone who is coughing or sneezing")
    print("Wear a mask when physical distancing is not possible.")
    print("Don’t touch your eyes, nose or mouth.")
    print("Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
    print("Stay home if you feel unwell.")
    print("If you have a fever, cough and difficulty breathing, seek medical attention.")
    print("For more information visit : https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public")


def worldMenu():
    '''Menu box for world's data'''

    print("Enter 1 : Total cases")
    print("Enter 2 : Total recoverd cases")
    print("Enter 3 : Cases today")
    print("Enter 4 : Today's recovered cases today")
    print("Enter 5 : Active cases")
    print("Enter 6 : Total population")
    print("Enter 7 : Today's death")
    print("Enter 8 : Total deaths")
    print("Enter 9 : Total tests done COVID")
    print("Enter 10 - Critical cases")

def indiaStateMenu():
    '''Menu box for India's data'''

    print("Enter 1 : Active cases")
    print("Enter 2 : Total recoverd cases")
    print("Enter 3 : Confirmed cases")
    print("Enter 4 : Deaths")

def queryFunctionWorld():
    ''' Function to fetch the data from API country wise'''

    print("Do you want to see country list ? y for yes")
    myChoice = input("Your choice : ")
    if myChoice == 'y' or myChoice == 'Y':
        check_all_countries()
    else:
        pass
    country = input("Enter your country : ")
    worldMenu()
    
    try:
        response = requests.get(countryAPI)
    except:
        print("Error, Something went wrong")
        toaster.show_toast(
            "Error",
            "Something went wrong",
            duration=4
        )

    country_found = False
    countries = json.loads(response.text)
    for i in range(len(countries)):
        if countries[i]['country'] == country:
            country_found = True
            toaster.show_toast(
                "Country found",
                f"{country} found in the lists",
                duration=4
            )
            saveHistory(country)
            png_icon = countries[i]['countryInfo']['flag']

            try:
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    toaster.show_toast(
                        f"Total cases in {countries[i]['country']}",
                        f"{countries[i]['cases']}",
                        duration=6
                    )
                    return (f"Total cases {countries[i]['cases']}")

                elif choice == 2:
                    toaster.show_toast(
                        f"Total recovered cases in {countries[i]['country']}",
                        f"{countries[i]['recovered']}",
                        duration=6
                    )
                    return (f"Recovered cases {countries[i]['recovered']}")

                elif choice == 3:
                    toaster.show_toast(
                        f"Today's cases in {countries[i]['country']}",
                        f"{countries[i]['todayCases']}",
                        duration=6
                    )
                    return (f"Today's cases {countries[i]['todayCases']}")

                elif choice == 4:
                    toaster.show_toast(
                        f"Today's recovered cases in {countries[i]['country']}",
                        f"{countries[i]['todayRecovered']}",
                        duration=6
                    )
                    return (
                        f"Today's recovered cases {countries[i]['todayRecovered']}"
                    )

                elif choice == 5:
                    toaster.show_toast(
                        f"Active cases in {countries[i]['country']}",
                        f"{countries[i]['active']}",
                        duration=6
                    )
                    return (f"Active cases {countries[i]['active']}")

                elif choice == 6:
                    toaster.show_toast(
                        f"Total population of {countries[i]['country']}",
                        f"{countries[i]['population']}",
                        duration=6
                    )
                    return (
                        f"Total population of {countries[i]['country']} is {countries[i]['population']}"
                    )

                elif choice == 7:
                    toaster.show_toast(
                        f"Today's death  {countries[i]['country']}",
                        f"{countries[i]['todayDeaths']}",
                        duration=6
                    )
                    return (
                        f"Today's death  {countries[i]['country']} is {countries[i]['todayDeaths']}"
                    )

                elif choice == 8:
                    toaster.show_toast(
                        f"Total deaths in {countries[i]['country']}",
                        f"{countries[i]['deaths']}",
                        duration=6
                    )
                    return (
                        f"Total deaths in {countries[i]['country']} is {countries[i]['deaths']}"
                    )

                elif choice == 9:
                    toaster.show_toast(
                        f"Total tests in {countries[i]['country']}",
                        f"{countries[i]['tests']}",
                        duration=6
                    )
                    return (
                        f"Total deaths in {countries[i]['country']} is {countries[i]['tests']}"
                    )

                elif choice == 10:
                    toaster.show_toast(
                        f"Critical cases in {countries[i]['country']}",
                        f"{countries[i]['critical']}",
                        duration=6
                    )
                    return (
                        f"Critical cases in {countries[i]['country']} is {countries[i]['critical']}"
                    )

                else:
                    toaster.show_toast(
                        "Error",
                        "Something went wrong",
                        duration=6
                    )
                    print("Invalid choice ")

            except Exception as e:
                toaster.show_toast(
                    "Error",
                    "Something went wrong",
                    duration=6
                )
                print("Something when wrong")

    if not country_found:
        toaster.show_toast(
            "Error",
            "Country not found",
            duration=4
        )


def queryFunctionIndia():
    ''' Function for fetching the data state wise'''

    print("For India")
    toaster.show_toast(
        "India",
        "Indian statewise data",
        duration=4
    )
    c = input("Do you want to see Indian states list : ?. Enter y for yes : ")
    if c == 'y' or c == 'Y' or c == 'Yes' or c == 'yes':
        check_all_Indian_state()
    else:
        pass

    state = input("Enter state : ")
    try:
        response = requests.get(
            indianAPI)

    except Exception as e:
        print("Error, Something went wrong")
        toaster.show_toast(
            "Error",
            "Invalid API request",
            duration=4
        )

    state_found = False
    gotState = json.loads(response.text)
    for i in range(len(gotState)):
        if gotState[i]['state'] == state:
            state_found = True
            toaster.show_toast(
                "State found",
                f"{state} found in the list",
                duration=4
            )
            saveHistory(state)
            indiaStateMenu()

            try:
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    toaster.show_toast(
                        f"Total cases in {gotState[i]['state']}",
                        f"{gotState[i]['active']}",
                        duration=6
                    )
                    return (f"Total cases {gotState[i]['active']}")

                elif choice == 2:
                    toaster.show_toast(
                        f"Total recovered cases in {gotState[i]['state']}",
                        f"{gotState[i]['recovered']}",
                        duration=6
                    )
                    return (f"Recovered cases {gotState[i]['recovered']}")

                elif choice == 3:
                    toaster.show_toast(
                        f"Today's cases in {gotState[i]['state']}",
                        f"{gotState[i]['confirmed']}",
                        duration=6
                    )
                    return (f"Today's cases {gotState[i]['confirmed']}")

                elif choice == 4:
                    toaster.show_toast(
                        f"Total deaths in {gotState[i]['state']}",
                        f"{gotState[i]['deaths']}",
                        duration=6
                    )
                    return (
                        f"Total deaths {gotState[i]['deaths']}")

                else:
                    toaster.show_toast(
                        "Error",
                        "Something went wrong",
                        duration=6
                    )
                    print("Invalid choice ")

            except:
                toaster.show_toast(
                    "Error",
                    "Something went wrong",
                    duration=6
                )
                print("Something when wrong")

    if not state_found:
        toaster.show_toast(
            "Error",
            "Country not found",
            duration=4
        )


def menu():
    ''' Menu box function '''

    print("Enter 1 to get data country wise")
    print("Enter 2 to get data of India's state only")
    print("Any key to exit")
    print('\n')


# Driver function - main
# All the code execution goes from here
if __name__ == "__main__":
    print("Welcome")
    toaster.show_toast(
        "COVID19",
        "Lets fight against this pandamic together",
        duration=4
    )
    toaster.show_toast(
        "Python",
        "This is a simple Python program used to fetch the COVID-19 data from different API's",
        duration=4
    )

    # Driver loop
    while True:
        menu()
        try:
            choice = int(input("Enter your choice : "))
        except:
            print("Something went wrong")
            toaster.show_toast(
                "Error",
                "Invalid choice",
                duration=4
            )
            break

        if choice == 1:
            toaster.show_toast(
                "Python",
                "World's COVID 19 data",
                duration=4
            )
            queryFunctionWorld()

        elif choice == 2:
            toaster.show_toast(
                "Python",
                "India's COVID 19 data",
                duration=4
            )
            queryFunctionIndia()

        else:
            print("Exiting....")
            toaster.show_toast(
                "Exiting",
                "Thank you for using me",
                duration=6
            )
            break

print("Do you want to see your search history : ?")
choice = input("Enter y to Yes : ")
if choice == 'y' or choice == 'Y' or choice == 'Yes' or choice == 'yes':
    toaster.show_toast(
        "Python",
        "Search history",
        duration=2
    )
    printHistory()
else:
    pass


print("Do you want to see COVID-19 precautions : ?")
choice = input("Enter y to Yes : ")
if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
    toaster.show_toast(
        "COVID19",
        "Precautions",
        duration=2
    )
    covid19Precations()
else:
    pass



# Clearing the history
stacks.clear()
