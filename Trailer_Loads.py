#Weights for vehciles, these values are constant and do not change
import time
import sys
truck_dict = {'single': 14140, 'double': 16840, 'sleeper': 18500}
trailer_dict = {28: 16580, 36: 18840, 48: 22140, 53: 22140, 'dry': 21220}
wt_gear = 2500
wt_pallet = 50
wt_pallet_jack = 1000

#Variables to be updated by user input and to take on weights of the above values
truck_weight = 0
trailer_1_weight = 0
trailer_2_weight = 0
gear_weight = 0



# Load Weight
# Select Set Y/N:
#     If Yes:
#         Truck
#         Trailer 1
#         Trailer 2
#         Gear (Accounted for in final math)
#         Num of Pallets
#         Pallet Jack Y/N (Or just assume yes)
        
#     If No:
#         Truck
#         Trailer
#         Num of Pallets
#         Pallet Jack

load_weight = input('Please Enter Load Weight: ')

is_a_set = input('Is This a Set? Please Select: \n 1 for Yes \n 2 for No \n \n Please Type Your Selection: ')
if is_a_set == '1' or is_a_set == 2:
    print()
else:
    print()
    print()
    print('INVALID SELECTION')
    sys.exit()

#Branch #1 that selects all of the parts of a set of doubles
if is_a_set == '1':
    gear_weight += wt_gear
if is_a_set == '1':
    truck_select = input('What is the truck type: \n 1 = Single \n 2 = Tandem \n 3 = Sleeper \n Please Type Your Selection: ')
    if truck_select == '1':
        truck_weight += truck_dict['single']
    elif truck_select == '2':
        truck_weight += truck_dict['double']
    elif truck_select == '3':
        truck_weight += truck_dict['sleeper']
    else:
        print()
        print()
        print('INVALID SELECTION')
        sys.exit()
    print()
    print()
    trailer_1 = input('What is the trailer type: \n 1 = 28 ft Trailer \n 2 = 36 ft Trailer \n 3 = 48 ft Trailer \n 4 = 53 ft Trailer \n 5 = Dry Trailer \n Please Type Your Selection: ')
    if trailer_1 == '1':
        trailer_1_weight += trailer_dict[28]
    elif trailer_1 == '2':
        trailer_1_weight += trailer_dict[36]
    elif trailer_1 == '3':
        trailer_1_weight += trailer_dict[48]
    elif trailer_1 == '4':
        trailer_1_weight += trailer_dict[53]
    elif trailer_1 == '5':
        trailer_1_weight += trailer_dict['dry']
    else:
        print()
        print()
        print('INVALID SELECTION')
        sys.exit()    
    print()
    print()
    trailer_2 = input('What is the trailer type: \n 1 = 28 ft Trailer \n 2 = 36 ft Trailer \n 3 = 48 ft Trailer \n 4 = 53 ft Trailer \n 5 = Dry Trailer \n Please Type Your Selection: ')
    if trailer_2 == '1':
        trailer_2_weight += trailer_dict[28]
    elif trailer_2 == '2':
        trailer_2_weight += trailer_dict[36]
    elif trailer_2 == '3':
        trailer_2_weight += trailer_dict[48]
    elif trailer_2 == '4':
        trailer_2_weight += trailer_dict[53]
    elif trailer_2 == '5':
        trailer_2_weight += trailer_dict['dry']
    else:
        print()
        print()
        print('INVALID SELECTION')
        sys.exit()


#Branch #2 that selects all of the parts of a single trailer configuration    
elif is_a_set == '2':
    truck_select = input('What is the truck type: \n 1 = Single \n 2 = Tandem \n 3 = Sleeper \n Please Type Your Selection: ')
    if truck_select == str(1):
        truck_weight += truck_dict['single']
    elif truck_select == str(2):
        truck_weight += truck_dict['double']
    elif truck_select == str(3):
        truck_weight += truck_dict['sleeper']
    else:
        print()
        print()
        print('INVALID SELECTION')
        sys.exit()    
print()
print()
total_weight = truck_weight + trailer_1_weight + trailer_2_weight + gear_weight
print('The Combined Weight is: ' + str(total_weight))