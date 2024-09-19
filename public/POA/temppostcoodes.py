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
    
    "South Australia": "All postcodes in South Australia are eligible",
    
    "Tasmania": "All postcodes in Tasmania are eligible",
    
    "Western Australia": list(range(6041, 6045)) + list(range(6055, 6057)) + 
                        [6069, 6076] + list(range(6083, 6085)) + 
                        [6111] + list(range(6121, 6127)) + list(range(6200, 6800))
                        ,
    
    "Northern Territory": "All postcodes in Northern Territory are eligible",
    
    "Norfolk Island": "All postcodes in Norfolk Island are eligible"
}


print(eligible_postcodes)