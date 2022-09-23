import json

import xml.etree.ElementTree as ET

def checkinside(child):
    dic = {}
    try:
        child[0]
    except:
        return child.text
    for chil in child:

        try:
            chil[0]
            dic[chil.tag] = checkinside(chil)
        except:
            dic[chil.tag] = chil.text
            
    
    return dic

def convertToDic(file):
    name = file[0:-4]
    tree = ET.parse(file)
    root = tree.getroot()
    d={}
    iterator = 0
    for child in root:
        if child.tag not in d:
            d[child.tag] = checkinside(child) ## Essa função vai trazer texto caso não tenha children e vai chamar ela mesma caso tenha children.
            iterator = 1
        else:
            iterator += 1
            d[f'{child.tag}{iterator}'] = checkinside(child)

    json_data = json.dumps(d)
    newfile = open(f'{name}.json', 'w')
    newfile.write(json_data)
    
    
    
if __name__ == '__main__':
    file = input('choose the name of your file\n')
    convertToDic(file)