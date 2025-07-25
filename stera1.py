import pygame
import sys
import time
import math
import random

path = "O:\\setera\\"

countries_and_territories = [
    ("Afghanistan", "Afghánistán"),
    ("Albania", "Albánie"),
    ("Algeria", "Alžírsko"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Antigua and Barbuda", "Antigua a Barbuda"),
    ("Argentina", "Argentina"),
    ("Armenia", "Arménie"),
    ("Australia", "Austrálie"),
    ("Austria", "Rakousko"),
    ("Azerbaijan", "Ázerbájdžán"),
    ("Bahamas", "Bahamy"),
    ("Bahrain", "Bahrajn"),
    ("Bangladesh", "Bangladéš"),
    ("Barbados", "Barbados"),
    ("Belarus", "Bělorusko"),
    ("Belgium", "Belgie"),
    ("Belize", "Belize"),
    ("Benin", "Benin"),
    ("Bhutan", "Bhútán"),
    ("Bolivia", "Bolívie"),
    ("Bosnia and Herzegovina", "Bosna a Hercegovina"),
    ("Botswana", "Botswana"),
    ("Brazil", "Brazílie"),
    ("Brunei", "Brunej"),
    ("Bulgaria", "Bulharsko"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burundi", "Burundi"),
    ("Cambodia", "Kambodža"),
    ("Cameroon", "Kamerun"),
    ("Canada", "Kanada"),
    ("Cape Verde", "Kapverdy"),
    ("Central African Republic", "Středoafrická republika"),
    ("Chad", "Čad"),
    ("Chile", "Chile"),
    ("China", "Čína"),
    ("Colombia", "Kolumbie"),
    ("Comoros", "Komory"),
    ("Congo (Congo-Brazzaville)", "Kongo (Brazzaville)"),
    ("Congo (Congo-Kinshasa)", "Kongo (Kinshasa)"),
    ("Costa Rica", "Kostarika"),
    ("Croatia", "Chorvatsko"),
    ("Cuba", "Kuba"),
    ("Cyprus", "Kypr"),
    ("Czech Republic", "Česká republika"),
    ("Denmark", "Dánsko"),
    ("Djibouti", "Džibutsko"),
    ("Dominica", "Dominika"),
    ("Dominican Republic", "Dominikánská republika"),
    ("East Timor (Timor-Leste)", "Východní Timor (Timor-Leste)"),
    ("Ecuador", "Ekvádor"),
    ("Egypt", "Egypt"),
    ("El Salvador", "Salvador"),
    ("Equatorial Guinea", "Rovníková Guinea"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonsko"),
    ("Eswatini", "Eswatini"),
    ("Ethiopia", "Etiopie"),
    ("Fiji", "Fidži"),
    ("Finland", "Finsko"),
    ("France", "Francie"),
    ("Gabon", "Gabon"),
    ("Gambia", "Gambie"),
    ("Georgia", "Gruzie"),
    ("Germany", "Německo"),
    ("Ghana", "Ghana"),
    ("Greece", "Řecko"),
    ("Grenada", "Grenada"),
    ("Guatemala", "Guatemala"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bisau"),
    ("Guyana", "Guyana"),
    ("Haiti", "Haiti"),
    ("Honduras", "Honduras"),
    ("Hungary", "Maďarsko"),
    ("Iceland", "Island"),
    ("India", "Indie"),
    ("Indonesia", "Indonésie"),
    ("Iran", "Írán"),
    ("Iraq", "Irák"),
    ("Ireland", "Irsko"),
    ("Israel", "Izrael"),
    ("Italy", "Itálie"),
    ("Ivory Coast", "Pobřeží slonoviny"),
    ("Jamaica", "Jamajka"),
    ("Japan", "Japonsko"),
    ("Jordan", "Jordánsko"),
    ("Kazakhstan", "Kazachstán"),
    ("Kenya", "Keňa"),
    ("Kiribati", "Kiribati"),
    ("Kosovo", "Kosovo"),
    ("Kuwait", "Kuvajt"),
    ("Kyrgyzstan", "Kyrgyzstán"),
    ("Laos", "Laos"),
    ("Latvia", "Lotyšsko"),
    ("Lebanon", "Libanon"),
    ("Lesotho", "Lesotho"),
    ("Liberia", "Libérie"),
    ("Libya", "Libye"),
    ("Liechtenstein", "Lichtenštejnsko"),
    ("Lithuania", "Litva"),
    ("Luxembourg", "Lucembursko"),
    ("Madagascar", "Madagaskar"),
    ("Malawi", "Malawi"),
    ("Malaysia", "Malajsie"),
    ("Maldives", "Maledivy"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Marshall Islands", "Marshallovy ostrovy"),
    ("Mauritania", "Mauritánie"),
    ("Mauritius", "Mauricius"),
    ("Mexico", "Mexiko"),
    ("Micronesia", "Mikronésie"),
    ("Moldova", "Moldavsko"),
    ("Monaco", "Monako"),
    ("Mongolia", "Mongolsko"),
    ("Montenegro", "Černá Hora"),
    ("Morocco", "Maroko"),
    ("Mozambique", "Mosambik"),
    ("Myanmar (Burma)", "Myanmar (Barma)"),
    ("Namibia", "Namibie"),
    ("Nauru", "Nauru"),
    ("Nepal", "Nepál"),
    ("Netherlands", "Nizozemsko"),
    ("New Zealand", "Nový Zéland"),
    ("Nicaragua", "Nikaragua"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigérie"),
    ("North Korea", "Severní Korea"),
    ("North Macedonia", "Severní Makedonie"),
    ("Norway", "Norsko"),
    ("Oman", "Omán"),
    ("Pakistan", "Pákistán"),
    ("Palau", "Palau"),
    ("Palestine", "Palestina"),
    ("Panama", "Panama"),
    ("Papua New Guinea", "Papua-Nová Guinea"),
    ("Paraguay", "Paraguay"),
    ("Peru", "Peru"),
    ("Philippines", "Filipíny"),
    ("Poland", "Polsko"),
    ("Portugal", "Portugalsko"),
    ("Qatar", "Katar"),
    ("Romania", "Rumunsko"),
    ("Russia", "Rusko"),
    ("Rwanda", "Rwanda"),
    ("Saint Kitts and Nevis", "Svatý Kryštof a Nevis"),
    ("Saint Lucia", "Svatá Lucie"),
    ("Saint Vincent and the Grenadines", "Svatý Vincenc a Grenadiny"),
    ("Samoa", "Samoa"),
    ("San Marino", "San Marino"),
    ("Sao Tome and Principe", "Svatý Tomáš a Princův ostrov"),
    ("Saudi Arabia", "Saúdská Arábie"),
    ("Senegal", "Senegal"),
    ("Serbia", "Srbsko"),
    ("Seychelles", "Seychely"),
    ("Sierra Leone", "Sierra Leone"),
    ("Singapore", "Singapur"),
    ("Slovakia", "Slovensko"),
    ("Slovenia", "Slovinsko"),
    ("Solomon Islands", "Šalamounovy ostrovy"),
    ("Somalia", "Somálsko"),
    ("South Africa", "Jihoafrická republika"),
    ("South Korea", "Jižní Korea"),
    ("South Sudan", "Jižní Súdán"),
    ("Spain", "Španělsko"),
    ("Sri Lanka", "Srí Lanka"),
    ("Sudan", "Súdán"),
    ("Suriname", "Surinam"),
    ("Sweden", "Švédsko"),
    ("Switzerland", "Švýcarsko"),
    ("Syria", "Sýrie"),
    ("Taiwan", "Tchaj-wan"),
    ("Tajikistan", "Tádžikistán"),
    ("Tanzania", "Tanzanie"),
    ("Thailand", "Thajsko"),
    ("Togo", "Togo"),
    ("Tonga", "Tonga"),
    ("Trinidad and Tobago", "Trinidad a Tobago"),
    ("Tunisia", "Tunisko"),
    ("Turkey", "Turecko"),
    ("Turkmenistan", "Turkmenistán"),
    ("Tuvalu", "Tuvalu"),
    ("Uganda", "Uganda"),
    ("Ukraine", "Ukrajina"),
    ("United Arab Emirates", "Spojené arabské emiráty"),
    ("United Kingdom", "Spojené království"),
    ("United States", "Spojené státy"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistan", "Uzbekistán"),
    ("Vanuatu", "Vanuatu"),
    ("Vatican City", "Vatikán"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Yemen", "Jemen"),
    ("Zambia", "Zambie"),
    ("Zimbabwe", "Zimbabwe"),

    # Nezávislá/okupovaná/závislá území často zahrnovaná v Seterra
    ("Greenland", "Grónsko"),
    ("Puerto Rico", "Portoriko"),
    ("Western Sahara", "Západní Sahara"),
    ("Hong Kong", "Hongkong"),
    ("Macau", "Macao"),
    ("Faroe Islands", "Faerské ostrovy"),
    ("French Guiana", "Francouzská Guyana"),
    ("Guadeloupe", "Guadeloupe"),
    ("Martinique", "Martinik"),
    ("Réunion", "Réunion"),
    ("New Caledonia", "Nová Kaledonie"),
    ("French Polynesia", "Francouzská Polynésie"),
    ("Gibraltar", "Gibraltar"),
    ("Bermuda", "Bermudy"),
    ("Cayman Islands", "Kajmanské ostrovy"),
    ("Falkland Islands", "Falklandy"),
    ("British Virgin Islands", "Britské Panenské ostrovy"),
    ("U.S. Virgin Islands", "Americké Panenské ostrovy"),
    ("Guam", "Guam"),
    ("Northern Mariana Islands", "Severní Mariany"),
    ("American Samoa", "Americká Samoa"),
    ("Cook Islands", "Cookovy ostrovy"),
    ("Niue", "Niue"),
    ("Aruba", "Aruba"),
    ("Curacao", "Curaçao"),
    ("Sint Maarten", "Sint Maarten"),
    ("Bonaire", "Bonaire"),
    ("Saint Pierre and Miquelon", "Saint-Pierre a Miquelon"),
    ("Tokelau", "Tokelau"),
    ("Wallis and Futuna", "Wallis a Futuna"),
    ("Mayotte", "Mayotte"),
    ("Saint Helena", "Svatá Helena"),
    ("Anguilla", "Anguilla"),
    ("Montserrat", "Montserrat"),
    ("Turks and Caicos Islands", "Turks a Caicos"),
    ("British Indian Ocean Territory", "Britské indickooceánské území"),
    ("Christmas Island", "Vánoční ostrov"),
    ("Norfolk Island", "Norfolk"),
    ("Pitcairn Islands", "Pitcairnovy ostrovy")
]


countries_coordinates_central_america = [
    
    
    ("Costa Rica", 9.7489, -83.7534),
    ("Cuba", 21.5218, -77.7812),
    
    ("Dominican Republic", 18.7357, -70.1627),
    ("El Salvador", 13.7942, -88.8965),
    
    ("Guatemala", 15.7835, -90.2308),
    ("Haiti", 18.9712, -72.2852),
    ("Honduras", 13.9094, -83.4286),
    ("Jamaica", 18.1096, -77.2975),
    ("Nicaragua", 12.8654, -85.2072),
    ("Panama", ),
    
    
    
]

countries_coordinates = [
[ #north america
    ("United States", 560, 533),
    ("Canada", 529, 351),
    ("Mexico", 541, 724)
],
[# stredni amerika
("Belize", 445, 341),
("Guatemala", 421, 370),
("El Salvador", 440, 395),
("Honduras",474, 377),
("Nicaragua",509, 408),
("Costa Rica",524, 462),
("Panama",569, 485),
("Cuba",612, 262),
("Haiti",714, 303),
("Dominican repiblic",738, 305),
("Jamaica",630, 317),
("Puerto Rico",808, 308),
("Antigua and Barbuda", 881, 318),
("Bahamas", 615, 206),
("Barbados", 924, 382),
("Dominica", 891, 349),
("Grenada", 892, 404),
("Trinidad and Tobago", 902, 430),
("Saint Kitts and Nevis", 865, 318),
("Saint Lucia", 900, 372),
("Saint Vincent and the Grenadines", 898, 385)
],
[# jižní amerika
("Brasil", 440, 317),
("Colombia", 177, 113),
("Venezuela", 248, 92),
("Guyana", 336, 113),
("Surinam", 364, 130),
("French Guyana", 396, 138),
("Ecuador", 116, 187),
("Peru", 148, 268),
("Bolivia", 271, 344),
("Paraguay", 322, 417),
("Chile", 206, 511),
("Argentina", 269, 530),
("Uruguay", 333, 522),
("Falklands", 284, 699)
],


[# oceanie
("Australia", 218, 454),
("New Zealand", 589, 613),
("Fiji", 596, 363),
("Papua new Guinea",310, 273),
("Tonga",681, 371),
("Kiribati",578, 231),
("Nauru",492, 223),
("Vanuatu", 505, 360),
("Marshal islands", 516, 128),
("Palau",233, 171),
("Micronesia",360, 173),
("Tuvalu",591, 296),
("Sollomon islands",441, 295),
("Samoa",679, 332)
],


[# asie
("China (PRC)", 573, 366),
("  Israel and/or West bank and Gaza  ", 100, 361  ),
("  Bangladesh  ", 476, 424 ),
("  Thailand  ", 560, 493  ),
("   Armenia ",  156, 295 ),
("   Korea ", 693, 310  ),
("   United Arab Emirates ", 236, 425  ),
("   Afghanistan ",  303, 338 ),
("  Jordan  ",  113, 371 ),
("  East Timor  ",  739, 682 ),
("   Kazakhstan ",284, 237   ),
("   Turkmenisan ", 255, 303  ),
("  Philippines  ",   715, 517),
("    Vietnam",  613, 509 ),
("   Uzbekistan ",  275, 280 ),
("   Indonesia ", 614, 665  ),
("  Singapoure  ", 588, 600  ),
("  Russia (Omsk)  ",  308, 171 ),
("   Iran ",  210, 327 ),
("  Bahrain  ", 204, 408  ),
("  Kyrgyzstan  ", 349, 281  ),
(" Myanmar   ", 522, 452  ),
("   Bhutan ",  476, 395 ),
("   Nepal ", 430, 392  ),
("  Japan  ", 774, 325  ),
("  Oman  ",  259, 431 ),
("Saudi Arabia    ", 175, 430  ),
("  Iraq  ",  156, 351 ),
(" Laos   ",  565, 456 ),
(" Malaysia   ", 575, 579  ),
("    Cambodia",  584, 513 ),
("  Türkiye  ",   83, 301),
(" China (ROC)   ", 686, 422  ),
("  Mongolia  ",512, 235   ),
("  Yemen  ",  173, 495 ),
("  Azerbaijan  ",  182, 294 ),
(" Brunei   ", 661, 573  ),
(" Georgia   ",  141, 276 ),
("  India  ", 396, 407  ),
("  Sri Lanka  ", 422, 553  ),
(" Pakistan   ", 343, 355  ),
(" Lebanon   ",  106, 344 ),
(" Qatar   ", 217, 415  ),
("  Syria  ",122, 333   ),
("   Kuwait ",  185, 382 ),
("  The Maledives  ", 365, 575  )

],

[# evropa
("Czechia", 404, 487)
],
[# afrika
("Somalia", 706, 367)
]
]

def scaling(image, af_proportions, pomer, velikost):
    
    if af_proportions > pomer: 
        imagee = pygame.transform.scale(image, (velikost[0], velikost[0]/af_proportions))

    elif af_proportions == pomer:
        imagee = pygame.transform.scale(image, (velikost[0], velikost[1]))

    else:
        imagee = pygame.transform.scale(image, (velikost[1]*af_proportions, velikost[1])) 

    return imagee

uhadnute_zeme = []

def update_cur_count(guessed):
    if guessed != 0:
        uhadnute_zeme.append(guessed)
        #nova_zeme = uhadnute_zeme[random.randint(0,len(uhadnute_zeme))]
    nova_zeme = countries_coordinates[random.randint(0,len(countries_coordinates)-1)]
    nova_zeme = nova_zeme[random.randint(0,len(nova_zeme)-1)]
    nova_zeme = nova_zeme[0].strip()

    while nova_zeme in uhadnute_zeme:
        nova_zeme = countries_coordinates[random.randint(0,len(countries_coordinates)-1)]
        nova_zeme = nova_zeme[random.randint(0,len(nova_zeme)-1)]
        nova_zeme = nova_zeme[0].strip()

    return nova_zeme
    

#Sizes_NA = [83.0337814, 14.53144]

# Initialize pygame
pygame.init()

barva_pozadí_typ = 1
co = 0.5

velikost = [1000, 800] #delka obrazovky, výška obrazovky
pomer = velikost[0] / velikost[1]
width = velikost[0]
height = velikost[1]
# Set up the display
screen = pygame.display.set_mode((velikost[0], velikost[1]))  # Screen size: 800x600
pygame.display.set_caption('Seterra ultimate challange')

teckaa = pygame.image.load(f'{path}dot.jpg').convert_alpha()
tecka = pygame.transform.scale(teckaa, (10, 10))

mys = False

continents = []
continents_prop = []
continents_name = [ "North-america.svg", "central_america.gif", "South-america.svg", "Oceania.png", "Asia.png", "Europe.png", "Africa.svg"]
# Load the image (make sure the image is in the same folder as the script or provide the full path)
pathh = f"{path}"
for i in range(len(continents_name)):
    continents.append(pygame.image.load(f'{pathh}{continents_name[i]}').convert_alpha()) 
    continents_prop.append(continents[i].get_width() / continents[i].get_height())
    continents[i]=scaling(continents[i], continents_prop[i], pomer, velikost)

game_state = 1 
#1 - kontinety, výběr státu
#2 - vlajky - výběr vlajky státu
#3 - provincie státu (jen u vybraných)
#4 - vlajky provincií (jen u vybraných)
#5 - města
current_country = update_cur_count(0) #aktuálně hádaná země
print(f"Klikni na {current_country}")

displayed_continent = 0
mouse_cool_down = time.time()
posledni_hadana_zeme = "idk"
posledni_spravne_kliknuti = 0
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if game_state == 1:
                if event.key == pygame.K_LEFT: displayed_continent -= 1
                if event.key == pygame.K_RIGHT: displayed_continent += 1
                displayed_continent = displayed_continent % len(continents)
        
        if event.type == pygame.MOUSEBUTTONDOWN and (time.time()-mouse_cool_down)>0.5:
            
            print(pygame.mouse.get_pos())

            mys_pos = pygame.mouse.get_pos()
            mys = True
            
        else: mys = False

    
    time_stamp = time.time()
    
    if barva_pozadí_typ == 1:
        color_value1 = int(abs(((time_stamp* 7*co) % 510)-255))  # Wrap around the time value to stay within range
        color_value2 = int(abs(((time_stamp*11*co) % 510)-255))
        color_value3 = int(abs(((time_stamp*13*co) % 510)-255))
    
    if barva_pozadí_typ == 2:
        color_value1 = int(abs(((time_stamp*10*co) % 510)-255))  # Wrap around the time value to stay within range
        color_value2 = int(abs(((time_stamp*10*co) % 510)-255))
        color_value3 = int(abs(((time_stamp*10*co) % 510)-255))

    if barva_pozadí_typ == 3:
        color_value1 = 245 
        color_value2 = 118
        color_value3 = 52
        # Fill the screen with a color (optional)
    screen.fill((int(color_value1), int(color_value2), int(color_value3)))  # White background with time-dependent blue channel

    if game_state == 1:
        image_rect = continents[displayed_continent].get_rect()
        image_rect.center = (velikost[0]/2,velikost[1]/2)
        screen.blit(continents[displayed_continent], (0, 0))

        for i in countries_coordinates[displayed_continent]:
            screen.blit(tecka, (i[1]-5, i[2]-5))
        
        kliknuto = -1
        """for i in countries_coordinates[displayed_continent]:
            if mys == True and mys_pos[0] in range(i[1]-5, i[1]+5) and mys_pos[1] in range(i[2]-5, i[2]+5):
                kliknuto = i[0]"""

        if mys == True:
            mouse_cool_down = time.time()
            for i in countries_coordinates[displayed_continent]:
               
                if math.sqrt((mys_pos[0]-i[1])**2 + (mys_pos[1]-i[2])**2) < 10:
                    
                    kliknuto = i[0]

        if kliknuto !=-1 and (time.time()-posledni_spravne_kliknuti)>0.5:
            
            if kliknuto == current_country:
                print("Správně!")
                current_country = update_cur_count(kliknuto)
                print(f"Klikni na {current_country}")
                posledni_spravne_kliknuti = time.time()

            elif kliknuto != posledni_hadana_zeme: 
                print(f"Špatně, to byl/a/o {kliknuto}")
                posledni_hadana_zeme = kliknuto

        
            

        

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
