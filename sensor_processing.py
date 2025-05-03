def average_calculator(values):
  return sum(values) / len(values)

data = [72, 55 , 101, 90]
average = average_calculator(data)
print("Average:"  , average)


stations = [
    ['A1' , 62] ,
    ['B5' , 97] ,
    ['C3' , 155]
]

for value in stations:
      print(f"{value[0]} → {value[1]}")

def status_reporter(stations, thresold):
  for [id, pm25] in stations:
    if pm25 < thresold:
      print(f"{id} → {pm25}μg/m^3  (safe)")
    else:
      print(f"{id} → {pm25}μg/m^3 (danger)")

status_reporter(stations, 100)
