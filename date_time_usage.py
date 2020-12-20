from datetime import *
class Event:
    def __init__(self,StartTime,EndTime):
        self.StartTime=StartTime
        self.EndTime=EndTime
    def addvenue(self,venue):
        self.Venue=venue
class Venue:
    def __init__(self,name):
        self.name=name
    def addaddress(self,address):
        self.address=address
class Address:
    def __init__(self,street,city,state,country,zip):
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.zip=zip

event=Event(date(2020,12,1),date(2020,12,11))
venue=Venue("Kid")
address=Address("UE2","Ssr","Ryna","Jndic",120015)
event.addvenue(venue)
venue.addaddress(address)

print("Event starts at: ", event.StartTime," end at:",event.EndTime)
print("Event named: ",venue.name," held at: ",address.street,",",address.city,",",address.state,",",address.country,",",address.zip)
