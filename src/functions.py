"""The create_shoe function takes a list of materials as input
and determines the type of shoe created based on those materials"""


def create_shoe(materials_list):
    shoe_type=''
    
    if 'leather' in materials_list and 'rubber' in materials_list:
        shoe_type = 'boots'
    elif'canvas'in materials_list and 'rubber' in materials_list:
        shoe_type = 'canvas'
    else:
        shoe_type = 'unknown'
    
    return {'type': shoe_type , 'materials' : materials_list}    


def main():
    # Determines the type of shoe created based on materials
    materials_1 =['leather','rubber']
    materials_2 =['canvas','rubber']
    materials_3 =['skin','rubber']

    
    shoe_1 = create_shoe(materials_1)
    shoe_2 = create_shoe(materials_2)
    shoe_3 = create_shoe(materials_3)
    i=0
    shoes = [shoe_1, shoe_2 ,shoe_3]
    for shoe in shoes:
        i = i + 1
        if shoe['type'] == 'unknown':
            print(f"Unknown shoe type for the materials : {shoe['materials']}")
        else:
            print(f"Shoe {i} is of type: {shoe['type']}")

if __name__ == '__main__':
    main()