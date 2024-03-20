#Simple script that returns the list of all possible NTSA plates combination for vehicles in Kenya
# excluding letters resembling numbers and reserved plates such as 'KAF' and KDF
# Personalised, diplomatic, Ngos, county and National government plates have not been incorporated into this script
def possible_second_number_combinattion():
    alphabet_list_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'J', 'K', 'L', 'M', 'N','P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                     'Y', 'Z']

    compiled_number_combination = []

    for r in range(1,1000):
        for j in alphabet_list_a:
            compiled_number_combination.append(str(r).zfill(3) + j)
    return compiled_number_combination



def possible_first_segment_combination(the_possible_number):
    constant_plate_letter = 'K'

    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                     'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                     'Y', 'Z']

    compiled_name_combination = []

    #an empty list that will later on be populated to contain the first segment of plates
    all_vehicles = []

    for i in alphabet_list:
        for j in alphabet_list:

            #combining the constant plate letter with the two other letters to make the first 3 prefixes of the plate
            concat_plate = constant_plate_letter + i + j

            # exclude letters that resemble numbers
            if j != 'O' and j != 'I':
                # exclude the reserved plates
                if concat_plate != 'KAF' and concat_plate != 'KDF':
                    compiled_name_combination.append(concat_plate)

    for p in compiled_name_combination:
        for k in the_possible_number:
            vehicles = p + " "+ k
            all_vehicles.append(vehicles)
    return all_vehicles

