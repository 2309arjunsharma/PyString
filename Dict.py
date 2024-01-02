car =  {
    "brand": "Hyundai",
    "model": "Tucson",
    "year": 1964
}
print(car.get("model"))
car["year"] = 2023
print(car["year"])

car["color"] = "dual tone(white and black)"
print(car)
car.pop("model")
car.clear()
