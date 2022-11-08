'''
BUILD PLAN:
1. Open file directory with .JSON files
2. Loop while there is another .JSON file
3. Open indivdual .JSON
4. Read and convert .JSON to Python
5. Manually add color families
    1.primary color family
    2.primary color
    3.secondary color family
    4.secondary color
6. Convert data back to .JSON
7. Save the JSON and continue to next itteration

1. Make traits class


STATUS: Working as desried.
BUGS: None known.

HOW TO USE:
    1. Make sure par_dir isthe the correct parent directory, cur_dir is the directory with the current metadata files, new_dir will be the new file generated
'''

import os
import shutil
import json

#The Directory with the json folders
par_dir = r'C:\Users\jwsta\OneDrive\Desktop\Metadata'
cur_dir = par_dir + r'\currentMeta'
new_dir = par_dir + r'\newMeta'

#Check if new dir exists if it does replace, if it doesn't create
if os.path.exists(new_dir):
    shutil.rmtree(new_dir)
os.makedirs(new_dir)
            
#Initialize these values before run      
indentDepth = 4 #The ammount of spaces for each new heirarchy in the json
curFileNum = 1 #The initial number of the file i.e. 1.json -> 2.json
filePrefix = "" #any prefix desired in the outputfiles, this will come before the number i.e kai1.json -> kai2.json (this will only effect the output, not the input)

#dictionaries
accent_dic = {
    '00':'Bronze', 
    '01':'Silver', 
    '02':'Gold', 
    '03':'Base', 
    '04':'Iridescent',}

color_dicNames = {
    '00':'Base', 
    '01':'Solid', 
    '02':'Deep', 
    '03':'Metallic', 
    '04':'Base 2',
    '05':'Pastels',
    '06':'Stealth',
    '07':'Gradient',
    '08':'Cosmic',
    '09':'Pearl',
    '10':'Poly',
    '11':'Camo',
    '12':'Pro Gradient',
    '13':'Custom',
    '14':'Carbon Fibre',
    '15':'Camo 2',}

color_dicValue = {
    'Base':
        {
        '00':'Grey'}, 
    'Solid':
        {'00':'Grey',
         '01':'Blue',
         '02':'Green',
         '03':'Orange',
         '04':'Pink',
         '05':'Purple',
         '06':'Red',
         '07':'White',
         '08':'Yellow',
         '09':'Black'},
    'Deep':
        {'00':'Blue',
         '01':'Green',
         '02':'Pink',
         '03':'Purple',
         '04':'Red',},
    'Metallic':
        {'00':'Blue',
         '01':'Bronze',
         '02':'Amber',
         '03':'Green',
         '04':'Orange',
         '05':'Pink',
         '06':'Red',
         '07':'Silver',
         '08':'Gunmetal',},
    'Base 2':
        {'00':'Grey',
         '01':'Light Grey',
         '02':'White',},
    'Pastels':
        {'00':'Blue',
         '01':'Light Grey',
         '02':'Mint',
         '03':'Peach',
         '04':'Pink',
         '05':'Purple',},
    'Stealth':
        {'00':'Battleship',
         '01':'Desert',
         '02':'Forest Green',
         '03':'Gunmetal',
         '04':'Navy',
         '05':'Olive',
         '06':'Steel',
         '07':'Red Sand',
         '08':'Tank',},
    'Gradient':
        {'00':'Blues',
         '01':'Teal Ash',
         '02':'Greens',
         '03':'Oranges',
         '04':'Pastels',
         '05':'Ruby',
         '06':'Acid Ash',
         '07':'Pink Ash',
         '08':'Yellow Ash',
         '09':'Vapor',
         '10':'Bolt',
         '11':'Purple Flame',
         '12':'Marine',
         '13':'Droid',
         '14':'Arcee',
         '15':'Razorback',},
    'Cosmic':
        {'00':'Nebula',
         '01':'Cloud',
         '02':'Nova',
         '03':'Aurora',
         '04':'Orion',
         '05':'Eros',},
    'Pearl':
        {'00':'Golden',
         '01':'Rainbow',
         '02':'Pastels',
         '03':'Techno',
         '04':'Toxic',
         '05':'Slick',
         '06':'Solana',
         '07':'Acid Rain',
         '08':'Holo',
         '09':'Night City',
         '10':'Genesis',
         '11':'Dawn',},
    'Poly':
        {'00':'Green',
         '01':'Rainbow',
         '02':'Gradient',
         '03':'Blue',
         '04':'Pink',},
    'Camo':
        {'00':'Digi Black',
         '01':'Digi Green',
         '02':'Digi Grey',
         '03':'Digi Sand',
         '04':'Jungle Black',
         '05':'Jungle Green',
         '06':'Jungle Grey',
         '07':'Jungle Sand',},
    'Pro Gradient':
        {'00':'Fire',
         '01':'Holo',
         '02':'Flame',
         '03':'Rainbow',
         '04':'Slick',
         '05':'Solana',
         '06':'Dusk',
         '07':'Dawn',
         '08':'Night City',
         '09':'Genesis',
         '10':'Ember',},
    'Custom':
        {'00':'Red and Yellow',
         '01':'Royal and Cheese',
         '02':'Ming Dynasty',
         '03':'Blue Streak',
         '04':'Renewal',
         '05':'Hazard',
         '06':'Neon',
         '07':'Night Light',
         '08':'Green Fury',
         '09':'Purple People Eater',},
    'Carbon Fibre':
        {'00':'Carbon Fibre',},
    'Camo 2':
        {'00':'Digi Blue',
         '01':'Jungle Blue',},
    }
    
#Itterate through directory with all json files, if it is join it to the proper directory and load it
print('Starting opperation on: ' + cur_dir)

for file in os.listdir(cur_dir):
    if file.endswith('.json'):
    
        cur_file = os.path.join(cur_dir, file)
    
        with open(cur_file) as f: 
            data = json.load(f) 
            
            #get build code
            build_code = data['properties']['kaizen']['build_code']
            
            #get numbers for each attribute from build code
            head = build_code[0:2]
            chest = build_code[3:5]
            weapon = build_code[6:8]
            arm = build_code[9:11]
            family1 = build_code[13:15]
            color1 = build_code[16:18]
            family2 = build_code[21:23]
            color2 = build_code[24:26]
            full_body = build_code[28:30]
            accent = build_code[32:34]
            eye_color = build_code[35:37]
            eye_shape = build_code[38:40]
            background = build_code[41:43]
            decal = build_code[44:46]
            file_number = build_code[47:52]
            
            #print('Primary: ' + color_dicValue[color_dicNames[family1]][color1] + ' | Secondary: ' + color_dicValue[color_dicNames[family2]][color2] + ' | Accent: ' + accent_dic[accent])
            
            #map info 
            curTraits = data['attributes']
            
            '''
            START ATTEMPT TO HARDCODE NO SPACE
            newTraitAmm = 5
            
            newTrait1 = {'trait_type': 'Primary Color Family',
                          'value':color_dicNames[family1]}
            newTrait2 = {'trait_type': 'Primary Color',
                         'value':color_dicValue[color_dicNames[family1]][color1]}
            newTrait3 = {'trait_type': 'Secondary Color Family',
                         'value':color_dicNames[family2]}
            newTrait4 = {'trait_type': 'Secondary Color',
                         'value':color_dicValue[color_dicNames[family2]][color2]}
            newTrait5 = {'trait_type': 'Accent',
                         'value':accent_dic[accent]}'''
            
            
            newTraits = [{'trait_type': 'Primary Color Family',
                          'value':color_dicNames[family1]}, 
                        {'trait_type': 'Primary Color',
                         'value':color_dicValue[color_dicNames[family1]][color1]},
                        {'trait_type': 'Secondary Color Family',
                         'value':color_dicNames[family2]},
                        {'trait_type': 'Secondary Color',
                         'value':color_dicValue[color_dicNames[family2]][color2]},
                        {'trait_type': 'Accent',
                         'value':accent_dic[accent]}]
            
            #append new info to old info
            i = 0
            while i < len(newTraits):
                curTraits.append(newTraits[i])
                #print(newTraits[i])
                i += 1
            
            
            #set the new directory for the new file
            new_file = os.path.basename(f.name)
            new_file = os.path.join(new_dir, new_file)
            
            #Dump the information
            with open(new_file, 'w') as j:
                json.dump(data, j, indent=indentDepth)
            j.close()
                
            #Itterate file numbers
            curFileNum += 1

f.close()
print('Files generated at: ' + new_dir)
                    
                
