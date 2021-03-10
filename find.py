import json
def findpath(airport):
    terminal=[]
    pic=[]
    with open('static/air.json',encoding='utf-8',errors='ignore') as data_file:
        data=json.load(data_file,strict=False)
        findairport=data[airport]
        for i,j in findairport.items():
            terminal.append(i)
            pic.append(j)
    data_file.close()
    return terminal,pic
def find_object_path(airport):
    terminal=[]
    pic=[]
    with open('static/car-park.json',encoding='utf-8',errors='ignore') as data_file:
        data=json.load(data_file,strict=False)
        findairport=data[airport]
        for i,j in findairport.items():
            terminal.append(i)
            pic.append(j)
    data_file.close()
    return terminal,pic
def find_airport_size(terminal):
    with open('static/airport-size.json',encoding='utf-8',errors='ignore') as data_file:
        data=json.load(data_file,strict=False)
        size=data[terminal]
        return size
def find_parking_size(terminal):
    with open('static/car-park-size.json',encoding='utf-8',errors='ignore') as data_file:
        data=json.load(data_file,strict=False)
        size=data[terminal]
        return size

        
            
            
            
