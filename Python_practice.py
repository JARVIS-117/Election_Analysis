print("Hello World")
counties = ["Arapahoe","Denver","Jeffersion"]
counties
counties[0]
print(counties[2])
counties[-3]
len(counties)
counties[1 :]
counties.append("El Paso")
counties.insert(2, "El Paso")
counties.remove("El Paso")
counties.pop("El Paso")
counties.insert(2, "El Paso")
counties.pop(3)
counties[2] = "Jefferson"
counties.insert(1, "El Paso")
counties.remove("El Paso")
counties.pop(-4)
counties.append("Denver")
counties.pop(1)
counties[0] = "Arapahoe"
counties[0] = "El Paso"
counties.insert(-0, "Arapahoe")
counties.remove("Arapahoe")
counties.insert(4, "Arapahoe")
counties.pop(2)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_tuple[: -1]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict["Arapahoe"]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data
len(voting_data)
voting_data.insert(1, ({"county":"El Paso", "registered_voters":461149}))
voting_data.pop(0)
voting_data.insert(2, ({"county": "Denver","registered_voters":463353}))
voting_data.pop(1)
voting_data.append(({"county":"Arapahoe","registered_voters":422829}))
voting_data