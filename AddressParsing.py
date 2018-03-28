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
# Detect Province/City Dictionary
provinceList = ["An Giang",
                "Vung Tau",
                "Bac Giang",
                "Bac Kan",
                "Bac Lieu",
                "Bac Ninh",
                "Ben Tre",
                "Binh Dinh",
                "Binh Duong",
                "Binh Phuoc",
                "Binh Thuan",
                "Ca Mau",
                "Cao Bang",
                "Dak Lak",
                "Dak Nong",
                "Dien Bien",
                "Dong Nai",
                "Dong Thap",
                "Gia Lai",
                "Ha Giang",
                "Ha Nam",
                "Ha Tinh",
                "Hai Duong",
                "Hau Giang",
                "Hoa Binh",
                "Hung Yen",
                "Khanh Hoa",
                "Kien Giang",
                "Kon Tum",
                "Lai Chau",
                "Lam Dong",
                "Lang Son",
                "Lao Cai",
                "Long An",
                "Nam Dinh",
                "Nghe An",
                "Ninh Binh",
                "Ninh Thuan",
                "Phu Tho",
                "Quang Binh",
                "Quang Nam",
                "Quang Ngai",
                "Quang Ninh",
                "Quang Tri",
                "Soc Trang",
                "Son La",
                "Tay Ninh",
                "Thai Binh",
                "Thai Nguyen",
                "Thanh Hoa",
                "Thua Thien Hue",
                "Tien Giang",
                "Tra Vinh",
                "Tuyen Quang",
                "Vinh Long",
                "Vinh Phuc",
                "Yen Bai",
                "Phu Yen",
                "Can Tho",
                "Da Nang",
                "Hai Phong",
                "Ha Noi",
                "Ho Chi Minh"]

# District in Ho Chi Minh City Dictionary
districtListHCM = [["q10", "Quan 10"],
                   ["q 10", "Quan 10"],
                   ["q\.10", "Quan 10"],
                   ["q\. 10", "Quan 10"],
                   ["quan 10", "Quan 10"],
                   ["quan\.10", "Quan 10"],
                   ["quan\. 10", "Quan 10"],
                   ["q11", "Quan 11"],
                   ["q 11", "Quan 11"],
                   ["q\.11", "Quan 11"],
                   ["q\. 11", "Quan 11"],
                   ["quan 11", "Quan 11"],
                   ["quan\.11", "Quan 11"],
                   ["quan\. 11", "Quan 11"],
                   ["q12", "Quan 12"],
                   ["q 12", "Quan 12"],
                   ["q\.12", "Quan 12"],
                   ["q\. 12", "Quan 12"],
                   ["quan 12", "Quan 12"],
                   ["quan\.12", "Quan 12"],
                   ["quan\. 12", "Quan 12"],
                   ["q1", "Quan 1"],
                   ["q 1", "Quan 1"],
                   ["q\.1", "Quan 1"],
                   ["q\. 1", "Quan 1"],
                   ["quan 1", "Quan 1"],
                   ["quan\.1", "Quan 1"],
                   ["quan\. 1", "Quan 1"],
                   ["q2", "Quan 2"],
                   ["q 2", "Quan 2"],
                   ["q\.2", "Quan 2"],
                   ["q\. 2", "Quan 2"],
                   ["quan 2", "Quan 2"],
                   ["quan\.2", "Quan 2"],
                   ["quan\. 2", "Quan 2"],
                   ["q3", "Quan 3"],
                   ["q 3", "Quan 3"],
                   ["q\.3", "Quan 3"],
                   ["q\. 3", "Quan 3"],
                   ["quan 3", "Quan 3"],
                   ["quan\.3", "Quan 3"],
                   ["quan\. 3", "Quan 3"],
                   ["q4", "Quan 4"],
                   ["q 4", "Quan 4"],
                   ["q\.4", "Quan 4"],
                   ["q\. 4", "Quan 4"],
                   ["quan 4", "Quan 4"],
                   ["quan\.4", "Quan 4"],
                   ["quan\. 4", "Quan 4"],
                   ["q5", "Quan 5"],
                   ["q 5", "Quan 5"],
                   ["q\.5", "Quan 5"],
                   ["q\. 5", "Quan 5"],
                   ["quan 5", "Quan 5"],
                   ["quan\.5", "Quan 5"],
                   ["quan\. 5", "Quan 5"],
                   ["q6", "Quan 6"],
                   ["q 6", "Quan 6"],
                   ["q\.6", "Quan 6"],
                   ["q\. 6", "Quan 6"],
                   ["quan 6", "Quan 6"],
                   ["quan\.6", "Quan 6"],
                   ["quan\. 6", "Quan 6"],
                   ["q7", "Quan 7"],
                   ["q 7", "Quan 7"],
                   ["q\.7", "Quan 7"],
                   ["q\. 7", "Quan 7"],
                   ["quan 7", "Quan 7"],
                   ["quan\.7", "Quan 7"],
                   ["quan\. 7", "Quan 7"],
                   ["q8", "Quan 8"],
                   ["q 8", "Quan 8"],
                   ["q\.8", "Quan 8"],
                   ["q\. 8", "Quan 8"],
                   ["quan 8", "Quan 8"],
                   ["quan\.8", "Quan 8"],
                   ["quan\. 8", "Quan 8"],
                   ["q9", "Quan 9"],
                   ["q 9", "Quan 9"],
                   ["q\.9", "Quan 9"],
                   ["q\. 9", "Quan 9"],
                   ["quan 9", "Quan 9"],
                   ["quan\.9", "Quan 9"],
                   ["quan\. 9", "Quan 9"],
                   ["GV", "Quan Go Vap"],
                   ["Go Vap", "Quan Go Vap"],
                   ["qGo Vap", "Quan Go Vap"],
                   ["qGV", "Quan Go Vap"],
                   ["q Go Vap", "Quan Go Vap"],
                   ["q GV", "Quan Go Vap"],
                   ["q\.Go Vap", "Quan Go Vap"],
                   ["q\.Gv", "Quan Go Vap"],
                   ["q\. Go Vap", "Quan Go Vap"],
                   ["q\. GV", "Quan Go Vap"],
                   ["quan Go Vap", "Quan Go Vap"],
                   ["quan Gv", "Quan Go Vap"],
                   ["quan\.Go Vap", "Quan Go Vap"],
                   ["quan\.Gv", "Quan Go Vap"],
                   ["quan\. Go Vap", "Quan Go Vap"],
                   ["quan\. Gv", "Quan Go Vap"],
                   ["BT", "Quan Binh Thanh"],
                   ["Binh Thanh", "Quan Binh Thanh"],
                   ["qBinh Thanh", "Quan Binh Thanh"],
                   ["qBT", "Quan Binh Thanh"],
                   ["q Binh Thanh", "Quan Binh Thanh"],
                   ["q BT", "Quan Binh Thanh"],
                   ["q\.Binh Thanh", "Quan Binh Thanh"],
                   ["q\.BT", "Quan Binh Thanh"],
                   ["q\. Binh Thanh", "Quan Binh Thanh"],
                   ["q\. BT", "Quan Binh Thanh"],
                   ["quan Binh Thanh", "Quan Binh Thanh"],
                   ["quan BT", "Quan Binh Thanh"],
                   ["quan\.Binh Thanh", "Quan Binh Thanh"],
                   ["quan\.BT", "Quan Binh Thanh"],
                   ["quan\. Binh Thanh", "Quan Binh Thanh"],
                   ["quan\. BT", "Quan Binh Thanh"],
                   ["Binh Tan", "Quan Binh Tan"],
                   ["BT", "Quan Binh Tan"],
                   ["qBinh Tan", "Quan Binh Tan"],
                   ["qBT", "Quan Binh Tan"],
                   ["q Binh Tan", "Quan Binh Tan"],
                   ["q BT", "Quan Binh Tan"],
                   ["q\.Binh Tan", "Quan Binh Tan"],
                   ["q\.BT", "Quan Binh Tan"],
                   ["q\. Binh Tan", "Quan Binh Tan"],
                   ["q\. BT", "Quan Binh Tan"],
                   ["quan Binh Tan", "Quan Binh Tan"],
                   ["quan BT", "Quan Binh Tan"],
                   ["quan\.Binh Tan", "Quan Binh Tan"],
                   ["quan\.BT", "Quan Binh Tan"],
                   ["quan\. Binh Tan", "Quan Binh Tan"],
                   ["quan\. BT", "Quan Binh Tan"],
                   ["Tan Binh", "Quan Tan Binh"],
                   ["qTan Binh", "Quan Tan Binh"],
                   ["q Tan Binh", "Quan Tan Binh"],
                   ["q\.Tan Binh", "Quan Tan Binh"],
                   ["q\. Tan Binh", "Quan Tan Binh"],
                   ["quan Tan Binh", "Quan Tan Binh"],
                   ["quan\.Tan Binh", "Quan Tan Binh"],
                   ["quan\. Tan Binh", "Quan Tan Binh"],
                   ["PN", "Quan Phu Nhuan"],
                   ["qPN", "Quan Phu Nhuan"],
                   ["q PN", "Quan Phu Nhuan"],
                   ["q\.PN", "Quan Phu Nhuan"],
                   ["q\. PN", "Quan Phu Nhuan"],
                   ["quan PN", "Quan Phu Nhuan"],
                   ["quan\.PN", "Quan Phu Nhuan"],
                   ["quan\. PN", "Quan Phu Nhuan"],
                   ["Phu Nhuan", "Quan Phu Nhuan"],
                   ["qPhu Nhuan", "Quan Phu Nhuan"],
                   ["q Phu Nhuan", "Quan Phu Nhuan"],
                   ["q\.Phu Nhuan", "Quan Phu Nhuan"],
                   ["q\. Phu Nhuan", "Quan Phu Nhuan"],
                   ["quan Phu Nhuan", "Quan Phu Nhuan"],
                   ["quan\.Phu Nhuan", "Quan Phu Nhuan"],
                   ["quan\. Phu Nhuan", "Quan Phu Nhuan"],
                   ["PN", "Quan Phu Nhuan"],
                   ["qPN", "Quan Phu Nhuan"],
                   ["q PN", "Quan Phu Nhuan"],
                   ["q\.PN", "Quan Phu Nhuan"],
                   ["q\. PN", "Quan Phu Nhuan"],
                   ["quan PN", "Quan Phu Nhuan"],
                   ["quan\.PN", "Quan Phu Nhuan"],
                   ["quan\. PN", "Quan Phu Nhuan"],
                   ["Tan Phu", "Quan Tan Phu"],
                   ["qTan Phu", "Quan Tan Phu"],
                   ["q Tan Phu", "Quan Tan Phu"],
                   ["q\.Tan Phu", "Quan Tan Phu"],
                   ["q\. Tan Phu", "Quan Tan Phu"],
                   ["quan Tan Phu", "Quan Tan Phu"],
                   ["quan\.Tan Phu", "Quan Tan Phu"],
                   ["quan\. Tan Phu", "Quan Tan Phu"],
                   # ["TP", "Quan Tan Phu"],
                   ["qTP", "Quan Tan Phu"],
                   ["q TP", "Quan Tan Phu"],
                   ["q\.TP", "Quan Tan Phu"],
                   ["q\. TP", "Quan Tan Phu"],
                   ["quan TP", "Quan Tan Phu"],
                   ["quan\.TP", "Quan Tan Phu"],
                   ["quan\. TP", "Quan Tan Phu"],
                   ["Nha Be", "Huyen Nha Be"],
                   ["qNha Be", "Huyen Nha Be"],
                   ["q Nha Be", "Huyen Nha Be"],
                   ["q\.Nha Be", "Huyen Nha Be"],
                   ["q\. Nha Be", "Huyen Nha Be"],
                   ["quan Nha Be", "Huyen Nha Be"],
                   ["quan\.Nha Be", "Huyen Nha Be"],
                   ["quan\. Nha Be", "Huyen Nha Be"],
                   ["Nha Be", "Huyen Nha Be"],
                   ["hNha Be", "Huyen Nha Be"],
                   ["h Nha Be", "Huyen Nha Be"],
                   ["h\.Nha Be", "Huyen Nha Be"],
                   ["h\. Nha Be", "Huyen Nha Be"],
                   ["quan Nha Be", "Huyen Nha Be"],
                   ["huyen\.Nha Be", "Huyen Nha Be"],
                   ["huyen\. Nha Be", "Huyen Nha Be"],
                   ["NB", "Huyen Nha Be"],
                   ["qNB", "Huyen Nha Be"],
                   ["q NB", "Huyen Nha Be"],
                   ["q\.NB", "Huyen Nha Be"],
                   ["q\. NB", "Huyen Nha Be"],
                   ["quan NB", "Huyen Nha Be"],
                   ["quan\.NB", "Huyen Nha Be"],
                   ["quan\. NB", "Huyen Nha Be"],
                   ["NB", "Huyen Nha Be"],
                   ["hNB", "Huyen Nha Be"],
                   ["h NB", "Huyen Nha Be"],
                   ["h\.NB", "Huyen Nha Be"],
                   ["h\. NB", "Huyen Nha Be"],
                   ["huyen NB", "Huyen Nha Be"],
                   ["huyen\.NB", "Huyen Nha Be"],
                   ["huyen\. NB", "Huyen Nha Be"],
                   ["Thu Duc", "Quan Thu Duc"],
                   ["qThu Duc", "Quan Thu Duc"],
                   ["q Thu Duc", "Quan Thu Duc"],
                   ["q\.Thu Duc", "Quan Thu Duc"],
                   ["q\. Thu Duc", "Quan Thu Duc"],
                   ["quan Thu Duc", "Quan Thu Duc"],
                   ["quan\.Thu Duc", "Quan Thu Duc"],
                   ["quan\. Thu Duc", "Quan Thu Duc"],
                   ["TD", "Quan Thu Duc"],
                   ["qTD", "Quan Thu Duc"],
                   ["q TD", "Quan Thu Duc"],
                   ["q\.TD", "Quan Thu Duc"],
                   ["q\. TD", "Quan Thu Duc"],
                   ["quan TD", "Quan Thu Duc"],
                   ["quan\.TD", "Quan Thu Duc"],
                   ["quan\. TD", "Quan Thu Duc"],
                   ["Binh Chanh", "Huyen Binh Chanh"],
                   ["qBinh Chanh", "Huyen Binh Chanh"],
                   ["q Binh Chanh", "Huyen Binh Chanh"],
                   ["q\.Binh Chanh", "Huyen Binh Chanh"],
                   ["q\. Binh Chanh", "Huyen Binh Chanh"],
                   ["quan Binh Chanh", "Huyen Binh Chanh"],
                   ["quan\.Binh Chanh", "Huyen Binh Chanh"],
                   ["quan\. Binh Chanh", "Huyen Binh Chanh"],
                   ["Binh Chanh", "Huyen Binh Chanh"],
                   ["hBinh Chanh", "Huyen Binh Chanh"],
                   ["h Binh Chanh", "Huyen Binh Chanh"],
                   ["h\.Binh Chanh", "Huyen Binh Chanh"],
                   ["h\. Binh Chanh", "Huyen Binh Chanh"],
                   ["huyen Binh Chanh", "Huyen Binh Chanh"],
                   ["huyen\.Binh Chanh", "Huyen Binh Chanh"],
                   ["huyen\. Binh Chanh", "Huyen Binh Chanh"],
                   ["BC", "Huyen Binh Chanh"],
                   ["qBC", "Huyen Binh Chanh"],
                   ["q BC", "Huyen Binh Chanh"],
                   ["q\.BC", "Huyen Binh Chanh"],
                   ["q\. BC", "Huyen Binh Chanh"],
                   ["quan BC", "Huyen Binh Chanh"],
                   ["quan\.BC", "Huyen Binh Chanh"],
                   ["quan\. BC", "Huyen Binh Chanh"],
                   ["BC", "Huyen Binh Chanh"],
                   ["hBC", "Huyen Binh Chanh"],
                   ["h BC", "Huyen Binh Chanh"],
                   ["h\.BC", "Huyen Binh Chanh"],
                   ["h\. BC", "Huyen Binh Chanh"],
                   ["huyen BC", "Huyen Binh Chanh"],
                   ["huyen\.BC", "Huyen Binh Chanh"],
                   ["huyen\. BC", "Huyen Binh Chanh"],
                   ["Binh Chanh", "Huyen Binh Chanh"],
                   ["qBinh Chanh", "Huyen Binh Chanh"],
                   ["q Binh Chanh", "Huyen Binh Chanh"],
                   ["q\.Binh Chanh", "Huyen Binh Chanh"],
                   ["q\. Binh Chanh", "Huyen Binh Chanh"],
                   ["quan Binh Chanh", "Huyen Binh Chanh"],
                   ["quan\.Binh Chanh", "Huyen Binh Chanh"],
                   ["quan\. Binh Chanh", "Huyen Binh Chanh"],
                   ["Cu Chi", "Huyen Cu Chi"],
                   ["hCu Chi", "Huyen Cu Chi"],
                   ["h Cu Chi", "Huyen Cu Chi"],
                   ["h\.Cu Chi", "Huyen Cu Chi"],
                   ["h\. Cu Chi", "Huyen Cu Chi"],
                   ["huyen Cu Chi", "Huyen Cu Chi"],
                   ["huyen\.Cu Chi", "Huyen Cu Chi"],
                   ["huyen\. Cu Chi", "Huyen Cu Chi"],
                   ["CC", "Huyen Cu Chi"],
                   ["qCC", "Huyen Cu Chi"],
                   ["q CC", "Huyen Cu Chi"],
                   ["q\.CC", "Huyen Cu Chi"],
                   ["q\. CC", "Huyen Cu Chi"],
                   ["quan CC", "Huyen Cu Chi"],
                   ["quan\.CC", "Huyen Cu Chi"],
                   ["quan\. CC", "Huyen Cu Chi"],
                   ["CC", "Huyen Cu Chi"],
                   ["hCC", "Huyen Cu Chi"],
                   ["h CC", "Huyen Cu Chi"],
                   ["h\.CC", "Huyen Cu Chi"],
                   ["h\. CC", "Huyen Cu Chi"],
                   ["huyen CC", "Huyen Cu Chi"],
                   ["huyen\.CC", "Huyen Cu Chi"],
                   ["huyen\. CC", "Huyen Cu Chi"],
                   ["Hoc Mon", "Huyen Hoc Mon"],
                   ["hHoc Mon", "Huyen Hoc Mon"],
                   ["h Hoc Mon", "Huyen Hoc Mon"],
                   ["h\.Hoc Mon", "Huyen Hoc Mon"],
                   ["h\. Hoc Mon", "Huyen Hoc Mon"],
                   ["huyen Hoc Mon", "Huyen Hoc Mon"],
                   ["huyen\.Hoc Mon", "Huyen Hoc Mon"],
                   ["huyen\. Hoc Mon", "Huyen Hoc Mon"],
                   ["HM", "Huyen Hoc Mon"],
                   ["qHM", "Huyen Hoc Mon"],
                   ["q HM", "Huyen Hoc Mon"],
                   ["q\.HM", "Huyen Hoc Mon"],
                   ["q\. HM", "Huyen Hoc Mon"],
                   ["quan HM", "Huyen Hoc Mon"],
                   ["quan\.HM", "Huyen Hoc Mon"],
                   ["quan\. HM", "Huyen Hoc Mon"],
                   ["HM", "Huyen Hoc Mon"],
                   ["hHM", "Huyen Hoc Mon"],
                   ["h HM", "Huyen Hoc Mon"],
                   ["h\.HM", "Huyen Hoc Mon"],
                   ["h\. HM", "Huyen Hoc Mon"],
                   ["huyen HM", "Huyen Hoc Mon"],
                   ["huyen\.HM", "Huyen Hoc Mon"],
                   ["huyen\. HM", "Huyen Hoc Mon"]]
"""
# retrieve district from dump address
for i in range(0, len(addrListNoAccent)):
    addrListNoAccent[i].append('')
    for j in range(0, len(provinceList)):
        if addrListNoAccent[i][0] == '':
            break
        if re.search("HCM", addrListNoAccent[i][0], re.IGNORECASE):
            addrListNoAccent[i][1] = "Ho Chi Minh"
            break
        if re.search("Dien Bien Phu", addrListNoAccent[i][0], re.IGNORECASE):
            addrListNoAccent[i][1] = "Ho Chi Minh"
            break
        if re.search("Xa lo Ha Noi", addrListNoAccent[i][0], re.IGNORECASE):
            addrListNoAccent[i][1] = "Ho Chi Minh"
            break
        if re.search(provinceList[j], addrListNoAccent[i][0], re.IGNORECASE):
            # print("{0}\t{1}".format(provinceList[j], addrListNoAccent[i][0]))
            addrListNoAccent[i][1] = provinceList[j]
            break

# filter district in address HCM
for i in range(0, len(addrListNoAccent)):
    addrListNoAccent[i].append('')
    for j in range(0, len(districtListHCM)):
        if re.search(districtListHCM[j][0], addrListNoAccent[i][0], re.IGNORECASE):
            if addrListNoAccent[i][0] == "Ho Chi Minh":
                print("{0}\t{1}".format(districtListHCM[j][1], addrListNoAccent[i][0]))
                addrListNoAccent[i][2] = districtListHCM[j][1]
                break
            else:
                print("{0}\t{1}".format(districtListHCM[j][1], addrListNoAccent[i][0]))
                addrListNoAccent[i][1] = "Ho Chi Minh"
                addrListNoAccent[i][2] = districtListHCM[j][1]
                break


# export to aggregated list CSV
with open('aggregatedList.csv', 'w', encoding='utf-8', newline='') as csvFile:
    wr = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
    for i in range(0, len(addrListNoAccent)):
        # print(addrListNoAccent[i])
        wr.writerow(addrListNoAccent[i])
"""

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
