#
# Example file for parsing and processing JSON

import urllib.request
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print(count, "events recorded")
    print()
    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("--------------------------------\n")

    # print the events that only have a magnitude greater than 4
    for event in theJSON["features"]:
        if event["properties"]["mag"] > 4:
            print(event['properties']["place"])
    print("--------------------------------\n")

    # print only the events where at least 1 person reported feeling something
    for event in theJSON["features"]:
        if event["properties"]["felt"]:
            print(event['properties']["place"])
    print("--------------------------------\n")


def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))

    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from the sever.")


if __name__ == "__main__":
    main()
