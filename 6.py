DistanceFull = 384400
SpeedFirst = 20000
SpeedSecond = 15000
SpeedThird = 10000

DistanceKnownFirst = 20000 * 5
DistanceKnownLast = 10000 * 1

DistanceUnknownMid = DistanceFull - (DistanceKnownFirst + DistanceKnownLast)

HoursOfFlightFirst = 5
HoursOfFlightSecond = DistanceUnknownMid // 15000
HoursOfFlightLast = 1

# print(DistanceUnknownMid // 15000)

print("Итого Баба Яга на ступе летела", HoursOfFlightFirst + HoursOfFlightSecond + HoursOfFlightLast, "часа")

# засыпаю
