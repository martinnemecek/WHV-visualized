import re

remoteAndVeryRemotePostcodes = {
    'New South Wales': [
        2356, 2386, 2387, 2396, 2405, 2406, 2672, 2675, 2825, 2826, 2829, 2832, 2833, 2834, 2835, 2836, 
        2838, 2839, 2840, 2873, 2878, 2879, 2898, 2899
    ],
    'Northern Territory': list(range(800, 900)),  # All postcodes in Northern Territory are eligible
    'Queensland': [
        4025, 4183, 4417, 4418, 4419, 4420, 4422, 4423, 4426, 4427, 4428, 4454, 4461, 4462, 4465, 4467, 4468, 
        4470, 4474, 4475, 4477, 4478, 4479, 4480, 4481, 4482, 4486, 4487, 4488, 4489, 4490, 4491, 4492, 4493, 
        4494, 4496, 4497, 4680, 4694, 4695, 4697, 4699, 4700, 4701, 4702, 4703, 4704, 4705, 4706, 4707, 4709, 
        4710, 4711, 4712, 4713, 4714, 4717, 4720, 4721, 4722, 4723, 4724, 4725, 4726, 4727, 4728, 4730, 4731, 
        4732, 4733, 4735, 4736, 4737, 4738, 4739, 4740, 4741, 4742, 4743, 4744, 4745, 4746, 4750, 4751, 4753, 
        4754, 4756, 4757, 4798, 4799, 4800, 4801, 4802, 4803, 4804, 4805, 4806, 4807, 4808, 4809, 4810, 4811, 
        4812, 4814, 4815, 4816, 4817, 4818, 4819, 4820, 4821, 4822, 4823, 4824, 4825, 4828, 4829, 4830, 4840, 
        4841, 4842, 4843, 4844, 4845, 4846, 4847, 4848, 4849, 4850, 4852, 4854, 4855, 4856, 4858, 4859, 4860, 
        4861, 4865, 4868, 4869, 4870, 4871, 4872, 4873, 4874, 4875, 4876, 4877, 4878, 4879, 4880, 4881, 4882, 
        4883, 4884, 4885, 4886, 4887, 4888, 4890, 4891, 4892, 4895
    ],
    'Victoria': [
        3424, 3506, 3509, 3512, 3889, 3890, 3891, 3892
    ],
    'South Australia': [
        5220, 5221, 5222, 5223, 5302, 5303, 5304, 5440, 5576, 5577, 5582, 5583, 5602, 5603, 5604, 5605, 5606, 
        5607, 5611, 5630, 5631, 5632, 5633, 5640, 5641, 5642, 5650, 5651, 5652, 5653, 5654, 5655, 5660, 5661, 
        5670, 5671, 5680, 5690, 5713, 5715, 5717, 5719, 5720, 5722, 5723, 5724, 5725, 5730, 5731, 5732, 5733, 
        5734
    ],
    'Tasmania': [
        7139, 7255, 7256, 7257, 7466, 7467, 7468, 7469, 7470
    ],
    'Western Australia': [
        6161, 6335, 6336, 6337, 6338, 6341, 6343, 6346, 6348, 6350, 6351, 6352, 6353, 6355, 6356, 6357, 6358, 
        6359, 6361, 6363, 6365, 6367, 6368, 6369, 6373, 6375, 6385, 6386, 6418, 6419, 6420, 6421, 6422, 6423, 
        6424, 6425, 6426, 6427, 6428, 6429, 6431, 6434, 6436, 6437, 6438, 6440, 6443, 6445, 6446, 6447, 6448, 
        6450, 6452, 6466, 6467, 6468, 6470, 6472, 6473, 6475, 6476, 6477, 6479, 6480, 6484, 6487, 6488, 6489, 
        6490, 6515, 6517, 6518, 6519, 6536, 6605, 6606, 6608, 6609, 6612, 6613, 6614, 6616, 6620, 6623, 6625, 
        6627, 6628, 6630, 6631, 6632, 6635, 6638, 6639, 6640, 6731, 6733, 6798, 6799
    ]
}



remoteAndVeryRemotePostcodesSpecifiedWork = {
    'Queensland': [
        4406, 4416, 4498
    ],
    'Tasmania': [
        7215
    ]
}


northAustraliaSpecifiedWork = {
    'Queensland': [
        4472, 4478, 4481, 4482, 4680, 4694, 4695, 4697, 4699, 4700, 4701, 4702, 4703, 4704, 4705, 4706, 4707, 
        4709, 4710, 4711, 4712, 4713, 4714, 4717, 4720, 4721, 4722, 4723, 4724, 4725, 4726, 4727, 4728, 4730, 
        4731, 4732, 4733, 4735, 4736, 4737, 4738, 4739, 4740, 4741, 4742, 4743, 4744, 4745, 4746, 4750, 4751, 
        4753, 4754, 4756, 4757, 4798, 4799, 4800, 4801, 4802, 4803, 4804, 4805, 4806, 4807, 4808, 4809, 4810, 
        4811, 4812, 4814, 4815, 4816, 4817, 4818, 4819, 4820, 4821, 4822, 4823, 4824, 4825, 4828, 4829, 4830, 
        4849, 4850, 4852, 4854, 4855, 4856, 4858, 4859, 4860, 4861, 4865, 4868, 4869, 4870, 4871, 4872, 4873, 
        4874, 4875, 4876, 4877, 4878, 4879, 4880, 4881, 4882, 4883, 4884, 4885, 4886, 4887, 4888, 4890, 4891, 
        4892, 4895
    ],
    'Western Australia': [
        6537, 6642, 6646, 6701, 6705, 6707, 6710, 6711, 6712, 6713, 6714, 6716, 6718, 6720, 6721, 6722, 
        6725, 6726, 6728, 6740, 6743, 6751, 6753, 6754, 6758, 6760, 6762, 6765, 6770
    ],
    'Northern Territory': list(range(800, 900))  # All postcodes in Northern Territory are eligible
}


regionalSpecifiedWork = {
    "New South Wales": list(range(2311, 2313)) + list(range(2328, 2412)) + 
                      list(range(2420, 2491)) + list(range(2536, 2552)) + 
                      list(range(2575, 2595)) + list(range(2618, 2740)) + 
                      list(range(2787, 2899)),
    
    "Victoria": [3139] + list(range(3211, 3335)) + list(range(3340, 3425)) + 
                list(range(3430, 3650)) + list(range(3658, 3750)) + [3753, 3756, 3758] + 
                [3762, 3764] + list(range(3778, 3782)) + [3783, 3797, 3799] + 
                list(range(3810, 3910)) + list(range(3921, 3926)) + 
                list(range(3945, 3975)) + [3979] + list(range(3981, 3997)),
    
    "Queensland": list(range(4124, 4126)) + [4133] + [4211] + list(range(4270, 4273)) + 
                  [4275, 4280, 4285, 4287] + list(range(4307, 4500)) + [4510, 4512] + list(range(4515, 4520)) + list(range(4522, 4900))
                  ,
    
    "South Australia": list(range(5000, 5799)),
    
    "Tasmania": list(range(7000, 7799)),
    
    "Western Australia": list(range(6041, 6045)) + list(range(6055, 6057)) + 
                        [6069, 6076] + list(range(6083, 6085)) + 
                        [6111] + list(range(6121, 6127)) + list(range(6200, 6800))
                        ,
    
    "Northern Territory": list(range(800, 900))
    
}


""" print(remoteAndVeryRemotePostcodes)
print(remoteAndVeryRemotePostcodesSpecifiedWork)
print(northAustraliaSpecifiedWork)
print(regionalSpecifiedWork) """



def group_postcodes_by_sum(dicts):
    value_mapping = [1, 2, 4, 8]  # Values assigned to each dictionary
    result = {i: [] for i in range(1, 16)}  # Initialize result dictionary with keys 1-15

    postcode_groups = {}

    for index, d in enumerate(dicts):
        for state, postcodes in d.items():
            for postcode in postcodes:
                if postcode in postcode_groups:
                    postcode_groups[postcode] += value_mapping[index]
                else:
                    postcode_groups[postcode] = value_mapping[index]

                # Check if the resulting group is out of range
                if postcode_groups[postcode] not in result:
                    raise ValueError(f"Error: Postcode {postcode} is trying to be assigned to an invalid group {postcode_groups[postcode]}.")

    # Populate the result dictionary
    for postcode, group in postcode_groups.items():
        result[group].append(postcode)
    
    return result

# Example usage
dict1 = {
    'Queensland': [4406, 4416, 4498,1],
    'Tasmania': [7215]
}

dict2 = {
    'Queensland': [4498, 4500,1],
    'Tasmania': [7215, 7216]
}

dict3 = {
    'Queensland': [4500, 4502,1],
    'Tasmania': [7216, 7218]
}

dict4 = {
    'Queensland': [4502, 4504],
    'Tasmania': [7218, 7220,1]
}


""" print(remoteAndVeryRemotePostcodes)
print(remoteAndVeryRemotePostcodesSpecifiedWork)
print(northAustraliaSpecifiedWork)
print(regionalSpecifiedWork) """

# Group postcodes based on the sum of the assigned values
postcode_dict = group_postcodes_by_sum([remoteAndVeryRemotePostcodes, remoteAndVeryRemotePostcodesSpecifiedWork, northAustraliaSpecifiedWork, regionalSpecifiedWork])

# Output the result
print(postcode_dict)


import re

def extract_placemarks_from_kml_and_save(kml_file, postcode_dict):
    # Open and read the KML file
    with open(kml_file, 'r', encoding='utf-8') as file:
        kml_content = file.read()

    # Initialize the result dictionary
    extracted_placemarks = {i: [] for i in postcode_dict.keys()}

    # Regular expression to find <Placemark>...</Placemark> blocks
    placemark_pattern = re.compile(r'<Placemark>(.*?)</Placemark>', re.DOTALL)

    # Iterate through each placemark block found in the KML
    for placemark in placemark_pattern.findall(kml_content):
        # Search for the <name> tag, which contains the postcode
        name_search = re.search(r'<name>\s*(\d+)\s*</name>', placemark)

        if name_search:
            # Extract and normalize the postcode (strip leading zeros)
            postcode = int(name_search.group(1).strip())

            # Check if this postcode is in the dictionary
            for group, postcodes in postcode_dict.items():
                if postcode in postcodes:
                    extracted_placemarks[group].append(placemark)
                    break  # Stop after finding the correct group

    # Create a KML file for each group
    for group, placemarks in extracted_placemarks.items():
        if placemarks:
            with open(f'{group}.kml', 'w', encoding='utf-8') as output_file:
                output_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                output_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
                output_file.write('<Document>\n')
                for placemark in placemarks:
                    output_file.write(f'<Placemark>{placemark}</Placemark>\n')
                output_file.write('</Document>\n')
                output_file.write('</kml>')

    return extracted_placemarks

""" # Example usage
postcode_dict = {
    1: [7215, 872],
    3: [4500],
    7: [7218, 7220]
} """

kml_file = './doc - Copy.kml'  # Provide the path to your KML file

# Extract the placemarks and save them to separate KML files
extract_placemarks_from_kml_and_save(kml_file, postcode_dict)
