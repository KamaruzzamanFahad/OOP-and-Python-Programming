from user import  Rider, Driver
from ride import Ride, RideRequest, RideMatching, RideSharing
from vehicle import Car, Bike

neya_zao = RideSharing("Neya Zao")
rahim = Rider("Rahim", "rahim@example.com", 10001, "Mohakhali", 500)
neya_zao.add_rider(rahim)
klimoddin = Driver("Klimoddin", "klimoddin@example.com", 10002, "Dhaka")
neya_zao.add_driver(klimoddin)
rahim.request_ride(neya_zao, "Gulshan", "car")
rahim.show_current_ride()
klimoddin.rech_destination(rahim.current_ride)
print(neya_zao)