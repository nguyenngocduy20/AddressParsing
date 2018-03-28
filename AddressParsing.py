# Python 3.6.3 Anaconda
# Virtual Environment
import unicodecsv
import csv
import library
import re

# import csv file in to list of Address List
addrList = []
with open('address.csv', newline='', encoding='utf-8') as csvFile:
    csvList = csv.reader(csvFile, delimiter=',')
    count = 0
    for row in csvList:
        # print("{0}. {1}".format(str(count),''.join(row)))
        if count > 0:
            addrList.append(','.join(row))
        count += 1

# remove accent from string
addrListNoAccent = []
count = 0
for item in addrList:
    item = library.remove_accent(item)
    addrListNoAccent.append([item])
    # print("{0}. {1}".format(str(count), addrListNoAccent[len(addrListNoAccent)-1][0]))
    count += 1

# Parsing
addrListAccent = []
count = 0
for item in addrList:
    addrListAccent.append([item])
    count += 1

# combine list
for i in range(0, len(addrListNoAccent)):
    provinceIndex = library.detect_province_index(addrListNoAccent[i][0])
    cityIndex = library.detect_city_index(addrListNoAccent[i][0])
    districtIndex = library.detect_district_index(addrListNoAccent[i][0])
    province = library.detect_province(addrListNoAccent[i][0])
    city = library.detect_city(addrListNoAccent[i][0])
    district = library.detect_district(addrListNoAccent[i][0])

    if provinceIndex < cityIndex or provinceIndex < districtIndex:
        province = ""
    if cityIndex < districtIndex:
        city = ""
    if districtIndex > -1:
        city = u"Hồ Chí Minh"
        province = u"Hồ Chí Minh"
    if city and (province == ""):
        province = library.city_province_mapping(city)
    else:
        if city != "":
            if library.city_province_mapping(city) != province:
                city = ""

    if province != "":
        addrListAccent[i].append(province)
    else:
        addrListAccent[i].append("")
    if city != "":
        addrListAccent[i].append(city)
    else:
        addrListAccent[i].append("")
    if district != "":
        addrListAccent[i].append(district)
    else:
        addrListAccent[i].append("")
    # print("{0: <3}{1: <3}{2: <3}{3: <20}{4: <20}{5: <20}{6}".format(provinceIndex, cityIndex, districtIndex, str(province), str(city), str(district), addrListNoAccent[i][0]))

for i in range(0, len(addrListAccent)):
    print("{0: <20}{1: <20}{2: <20}{3}".format(str(addrListAccent[i][1]), str(addrListAccent[i][2]), str(addrListAccent[i][3]), str(addrListAccent[i][0])))

# export to aggregated list CSV
# with open('aggregatedList.csv', 'wb', encoding='utf-8', newline='') as csvFile:
with open('aggregatedList.csv', 'wb') as csvFile:
    wr = unicodecsv.writer(csvFile, quoting=csv.QUOTE_ALL)
    for i in range(0, len(addrListAccent)):
        # print(addrListNoAccent[i])
        # wr.writerow("\"" + addrListAccent[i][0] + "\",\"" + addrListAccent[i][1] + "\",\"" + addrListAccent[i][2] + "\",\"" + addrListAccent[i][3] + "\"")
        wr.writerow(addrListAccent[i])
