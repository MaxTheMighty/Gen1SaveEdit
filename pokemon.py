import sys
import math
import random
#ITEMS
dictionary={"nothing":0x00	,
"masterball":0x01	,
"ultraball":0x02	,
"greatball":0x03	,
"pokéball":0x04	,
"townmap":0x05	,
"bicycle":0x06	,
"?????":0x07	,
"safariball":0x08	,
"pokédex":0x09	,
"moonstone":0x0a	,
"antidote":0x0b	,
"burnheal":0x0c	,
"iceheal":0x0d	,
"awakening":0x0e	,
"parlyzheal":0x0f	,
"fullrestore":0x10	,
"maxpotion":0x11	,
"hyperpotion":0x12	,
"superpotion":0x13	,
"potion":0x14	,
"boulderbadge":0x15	,
"cascadebadge":0x16	,
"thunderbadge":0x17	,
"rainbowbadge":0x18	,
"soulbadge":0x19	,
"marshbadge":0x1a	,
"volcanobadge":0x1b	,
"earthbadge":0x1c	,
"escaperope":0x1d	,
"repel":0x1e	,
"oldamber":0x1f	,
"firestone":0x20	,
"thunderstone":0x21	,
"waterstone":0x22	,
"hpup":0x23	,
"protein":0x24	,
"iron":0x25	,
"carbos":0x26	,
"calcium":0x27	,
"rarecandy":0x28	,
"domefossil":0x29	,
"helixfossil":0x2a	,
"secretkey":0x2b	,
"?????":0x2c	,
"bikevoucher":0x2d	,
"xaccuracy":0x2e	,
"leafstone":0x2f	,
"cardkey":0x30	,
"nugget":0x31	,
"ppup*":0x32	,
"pokédoll":0x33	,
"fullheal":0x34	,
"revive":0x35	,
"maxrevive":0x36	,
"guardspec.":0x37	,
"superrepel":0x38	,
"maxrepel":0x39	,
"direhit":0x3a	,
"coin":0x3b	,
"freshwater":0x3c	,
"sodapop":0x3d	,
"lemonade":0x3e	,
"s.s.ticket":0x3f	,
"goldteeth":0x40	,
"xattack":0x41	,
"xdefend":0x42	,
"xspeed":0x43	,
"xspecial":0x44	,
"coincase":0x45	,
"oak'sparcel":0x46	,
"itemfinder":0x47	,
"silphscope":0x48	,
"pokéflute":0x49	,
"liftkey":0x4a	,
"exp.all":0x4b	,
"oldrod":0x4c	,
"goodrod":0x4d	,
"superrod":0x4e	,
"ppup":0x4f	,
"ether":0x50	,
"maxether":0x51	,
"elixer":0x52	,
"maxelixer":0x53	,
"hm01":0xc4	,
"hm02":0xc5	,
"hm03":0xc6	,
"hm04":0xc7	,
"hm05":0xc8	,
"tm01":0xc9	,
"tm02":0xca	,
"tm03":0xcb	,
"tm04":0xcc	,
"tm05":0xcd	,
"tm06":0xce	,
"tm07":0xcf	,
"tm08":0xd0	,
"tm09":0xd1	,
"tm10":0xd2	,
"tm11":0xd3	,
"tm12":0xd4	,
"tm13":0xd5	,
"tm14":0xd6	,
"tm15":0xd7	,
"tm16":0xd8	,
"tm17":0xd9	,
"tm18":0xda	,
"tm19":0xdb	,
"tm20":0xdc	,
"tm21":0xdd	,
"tm22":0xde	,
"tm23":0xdf	,
"tm24":0xe0	,
"tm25":0xe1	,
"tm26":0xe2	,
"tm27":0xe3	,
"tm28":0xe4	,
"tm29":0xe5	,
"tm30":0xe6	,
"tm31":0xe7	,
"tm32":0xe8	,
"tm33":0xe9	,
"tm34":0xea	,
"tm35":0xeb	,
"tm36":0xec	,
"tm37":0xed	,
"tm38":0xee	,
"tm39":0xef	,
"tm40":0xf0	,
"tm41":0xf1	,
"tm42":0xf2	,
"tm43":0xf3	,
"tm44":0xf4	,
"tm45":0xf5	,
"tm46":0xf6	,
"tm47":0xf7	,
"tm48":0xf8	,
"tm49":0xf9	,
"tm50":0xfa	,
"tm51":0xfb	,
"tm52":0xfc	,
"tm53":0xfd	,
"tm54":0xfe	,
"tm55":0xff
            }
#pokemon
pokemon= {"rhydon":0x01,
"kangaskhan":0x02,
"nidoran♂":0x03,
"clefairy":0x04,
"spearow":0x05,
"voltorb":0x06,
"nidoking":0x07,
"slowbro":0x08,
"ivysaur":0x09,
"exeggutor":0x0a,
"lickitung":0x0b,
"exeggcute":0x0c,
"grimer":0x0d,
"gengar":0x0e,
"nidoran♀":0x0f,
"nidoqueen":0x10,
"cubone":0x11,
"rhyhorn":0x12,
"lapras":0x13,
"arcanine":0x14,
"mew":0x15,
"gyarados"  :0x16,
"shellder"  :0x17,
"tentacool"  :0x18,
"gastly"  :0x19,
"scyther"  :0x1a,
"staryu"  :0x1b,
"blastoise"  :0x1c,
"pinsir"  :0x1d,
"tangela"  :0x1e,
"missingno"  :0x1f,
"missingno"  :0x20,
"growlithe"  :0x21,
"onix"  :0x22,
"fearow"  :0x23,
"pidgey"  :0x24,
"slowpoke"  :0x25,
"kadabra"  :0x26,
"graveler"  :0x27,
"chansey"  :0x28,
"machoke"  :0x29,
"mrmime"  :0x2a,
"hitmonlee"  :0x2b,
"hitmonchan"  :0x2c,
"arbok"  :0x2d,
"parasect"  :0x2e,
"psyduck"  :0x2f,
"drowzee"  :0x30,
"golem"  :0x31,
"missingno"  :0x32,
"magmar"  :0x33,
"missingno"  :0x34,
"electabuzz"  :0x35,
"magneton"  :0x36,
"koffing"  :0x37,
"missingno"  :0x38,
"mankey"  :0x39,
"seel"  :0x3a,
"diglett"  :0x3b,
"tauros"  :0x3c,
"missingno"  :0x3d,
"missingno"  :0x3e,
"missingno"  :0x3f,
"farfetch'd"  :0x40,
"venonat"  :0x41,
"dragonite"  :0x42,
"missingno"  :0x43,
"missingno"  :0x44,
"missingno"  :0x45,
"doduo"  :0x46,
"poliwag"  :0x47,
"jynx"  :0x48,
"moltres"  :0x49,
"articuno"  :0x4a,
"zapdos"  :0x4b,
"ditto"  :0x4c,
"meowth"  :0x4d,
"krabby"  :0x4e,
"missingno"  :0x4f,
"missingno"  :0x50,
"missingno"  :0x51,
"vulpix"  :0x52,
"ninetales"  :0x53,
"pikachu"  :0x54,
"raichu"  :0x55,
"missingno"  :0x56,
"missingno"  :0x57,
"dratini"  :0x58,
"dragonair"  :0x59,
"kabuto"  :0x5a,
"kabutops"  :0x5b,
"horsea"  :0x5c,
"seadra"  :0x5d,
"missingno"  :0x5e,
"missingno"  :0x5f,
"sandshrew"  :0x60,
"sandslash"  :0x61,
"omanyte"  :0x62,
"omastar"  :0x63,
"jigglypuff"  :0x64,
"wigglytuff"  :0x65,
"eevee"  :0x66,
"flareon"  :0x67,
"jolteon"  :0x68,
"vaporeon"  :0x69,
"machop"  :0x6a,
"zubat"  :0x6b,
"ekans"  :0x6c,
"paras"  :0x6d,
"poliwhirl"  :0x6e,
"poliwrath"  :0x6f,
"weedle"  :0x70,
"kakuna"  :0x71,
"beedrill"  :0x72,
"missingno"  :0x73,
"dodrio"  :0x74,
"primeape"  :0x75,
"dugtrio"  :0x76,
"venomoth"  :0x77,
"dewgong"  :0x78,
"missingno"  :0x79,
"missingno"  :0x7a,
"caterpie"  :0x7b,
"metapod"  :0x7c,
"butterfree"  :0x7d,
"machamp"  :0x7e,
"missingno"  :0x7f,
"golduck"  :0x80,
"hypno"  :0x81,
"golbat"  :0x82,
"mewtwo"  :0x83,
"snorlax"  :0x84,
"magikarp"  :0x85,
"missingno"  :0x86,
"missingno"  :0x87,
"muk"  :0x88,
"missingno"  :0x89,
"kingler"  :0x8a,
"cloyster"  :0x8b,
"missingno"  :0x8c,
"electrode"  :0x8d,
"clefable"  :0x8e,
"weezing"  :0x8f,
"persian"  :0x90,
"marowak"  :0x91,
"missingno"  :0x92,
"haunter"  :0x93,
"abra"  :0x94,
"alakazam"  :0x95,
"pidgeotto"  :0x96,
"pidgeot"  :0x97,
"starmie"  :0x98,
"bulbasaur"  :0x99,
"venusaur"  :0x9a,
"tentacruel"  :0x9b,
"missingno"  :0x9c,
"goldeen"  :0x9d,
"seaking"  :0x9e,
"missingno"  :0x9f,
"missingno"  :0xa0,
"missingno"  :0xa1,
"missingno"  :0xa2,
"ponyta"  :0xa3,
"rapidash"  :0xa4,
"rattata"  :0xa5,
"raticate"  :0xa6,
"nidorino"  :0xa7,
"nidorina"  :0xa8,
"geodude"  :0xa9,
"porygon"  :0xaa,
"aerodactyl"  :0xab,
"missingno"  :0xac,
"magnemite"  :0xad,
"missingno"  :0xae,
"missingno"  :0xaf,
"charmander"  :0xb0,
"squirtle"  :0xb1,
"charmeleon"  :0xb2,
"wartortle"  :0xb3,
"charizard"  :0xb4,
"missingno"  :0xb5,
"missingno"  :0xb6,
"missingno"  :0xb7,
"missingno"  :0xb8,
"oddish"  :0xb9,
"gloom"  :0xba,
"vileplume"  :0xbb,
"bellsprout"  :0xbc,
"weepinbell"  :0xbd,
"victreebel" :0xbe 
}
#types
types = {"normal":0x00 , 	
"fighting":0x01 ,	
"flying":0x02 ,	
"poison":0x03 ,	
"ground":0x04 ,	
"rock":0x05 ,	
"bug":0x07 ,	
"ghost":0x08 ,	
"fire":0x14 ,	
"water":0x15 ,	
"grass":0x16 ,	
"electric":0x17 ,	
"psychic":0x18 ,	
"ice":0x19 ,	
"dragon":0x1a }
#moves
moves = {"pound":1	,
"karatechop":2	,
"doubleslap":3	,
"cometpunch":4	,
"megapunch":5	,
"payday":6	,
"firepunch":7	,
"icepunch":8	,
"thunderpunch":9	,
"scratch":10	,
"visegrip":11	,
"guillotine":12	,
"razorwind":13	,
"swordsdance":14	,
"cut":15	,
"gust":16	,
"wingattack":17	,
"whirlwind":18	,
"fly":19	,
"bind":20	,
"slam":21	,
"vinewhip":22	,
"stomp":23	,
"doublekick":24	,
"megakick":25	,
"jumpkick":26	,
"rollingkick":27	,
"sandattack":28	,
"headbutt":29	,
"hornattack":30	,
"furyattack":31	,
"horndrill":32	,
"tackle":33	,
"bodyslam":34	,
"wrap":35	,
"takedown":36	,
"thrash":37	,
"double-edge":38	,
"tailwhip":39	,
"poisonsting":40	,
"twineedle":41	,
"pinmissile":42	,
"leer":43	,
"bite":44	,
"growl":45	,
"roar":46	,
"sing":47	,
"supersonic":48	,
"sonicboom":49	,
"disable":50	,
"acid":51	,
"ember":52	,
"flamethrower":53	,
"mist":54	,
"watergun":55	,
"hydropump":56	,
"surf":57	,
"icebeam":58	,
"blizzard":59	,
"psybeam":60	,
"bubblebeam":61	,
"aurorabeam":62	,
"hyperbeam":63	,
"peck":64	,
"drillpeck":65	,
"submission":66	,
"lowkick":67	,
"counter":68	,
"seismictoss":69	,
"strength":70	,
"absorb":71	,
"megadrain":72	,
"leechseed":73	,
"growth":74	,
"razorleaf":75	,
"solarbeam":76	,
"poisonpowder":77	,
"stunspore":78	,
"sleeppowder":79	,
"petaldance":80	,
"stringshot":81	,
"dragonrage":82	,
"firespin":83	,
"thundershock":84	,
"thunderbolt":85	,
"thunderwave":86	,
"thunder":87	,
"rockthrow":88	,
"earthquake":89	,
"fissure":90	,
"dig":91	,
"toxic":92	,
"confusion":93	,
"psychic":94	,
"hypnosis":95	,
"meditate":96	,
"agility":97	,
"quickattack":98	,
"rage":99	,
"teleport":100,
"nightshade":101,
"mimic":102,
"screech":103,
"doubleteam":104,
"recover":105,
"harden":106,
"minimize":107,
"smokescreen":108,
"confuseray":109,
"withdraw":110,
"defensecurl":111,
"barrier":112,
"lightscreen":113,
"haze":114,
"reflect":115,
"focusenergy":116,
"bide":117,
"metronome":118,
"mirrormove":119,
"self-destruct":120,
"eggbomb":121,
"lick":122,
"smog":123,
"sludge":124,
"boneclub":125,
"fireblast":126,
"waterfall":127,
"clamp":128,
"swift":129,
"skullbash":130,
"spikecannon":131,
"constrict":132,
"amnesia":133,
"kinesis":134,
"soft-boiled":135,
"highjumpkick":136,
"glare":137,
"dreameater":138,
"poisongas":139,
"barrage":140,
"leechlife":141,
"lovelykiss":142,
"skyattack":143,
"transform":144,
"bubble":145,
"dizzypunch":146,
"spore":147,
"flash":148,
"psywave":149,
"splash":150,
"acidarmor":151,
"crabhammer":152,
"explosion":153,
"furyswipes":154,
"bonemerang":155,
"rest":156,
"rockslide":157,
"hyperfang":158,
"sharpen":159,
"conversion":160,
"triattack":161,
"superfang":162,
"slash":163,
"substitute":164,
"struggle":165,


} 

#---------methods---------

#input("Please enter the file directory of your pokemon save\n")
f = open(input("please enter save file directory"),'rb+')
array = bytearray(f.read())
print(array[0x2598])

opt = "";
#msg = "Please choose an option\n1) Change Name\n2) Change Rival Name\n3) Give items\n4) Change player ID\n5) Set pokemon in party\n6) Set Money\n7) Set Checksum and Save\n9) Or type STOP to stop";
options=["Change Name","Change Rival Name","Give Items","Change Player ID","Set Pokemon in Party","Set Money","Set Checksum and Save","Change Music","STOP"]
#--------------------PLAYER ID--------------------
def setPlayerID():
        playID = min(int(input("Please input a player ID\n")),50000)
        setTwoByte(0x2605,playID)
        
#--------------------SET ITEMS--------------------
def itemSet():
        count = [];
        items=[]
        ask = input("Please enter what items you want, limit 20\n")
        #Create list header to make sure you dont set items out of bounds
        count.append(min(99,int(input("Please enter the quantity\n"))))
        #ask for items and quantity 
        while(not len(items) == 20-array[0x25c9]):
                items.append(ask)
                ask = input("Please enter what item you want\n").replace(" ","").lower()
                if(ask.upper() == "STOP"):break
                count.append(min(99,int(input("Please enter the quantity\n"))))
        #add list header with count
        offset = array[0x25c9]*2
        
        print(array[0x25c9],' Items Detected, offset is',offset if array[0x25C9] > 0x0 else '')
        
        array[0x25C9]=len(items)+int(offset/2)
        print("Setting ",array[0x25C0], " to ", len(items)+int(offset/2), " at 0x25c9")
        print(items)
        print(count)
        for i in range(0,len(items)*2):
                        print("current index ",int(i))
                        if(i%2==0):
                                
                                print("Setting ", 0x25C9+i+offset," to ",dictionary[items[int(i/2)]]," at ",hex(0x25CA+i+offset))
                                array[0x25CA+i+offset]=dictionary[items[int(i/2)]]
                                
                        else:
                                print("Quantity ", 0x25C9+i+offset," to ",count[int(i/2)]," at ",hex(0x25CA+i+offset))
                                array[0x25CA+i+offset]=count[int(i/2)]
        
        else:
                
                array[len(items)*2+0x01+0x25C9+offset] = 0xFF
                print("Setting " , hex(len(items)*2+0x01+0x25C9+offset) , " to 0xFF (Terminator)")
                
#--------------------USER INPUT--------------------                
def askUsr():
        for i in range(len(options)):
                print(i+1,")",options[i])
        opt = input()
        if opt == "1":characterName()
        if opt == "2":rivalName()
        if opt == "3":itemSet()
        if opt == "4":setPlayerID()
        if opt == "5":setPoke()
        if opt == "6":setMoney()
        if opt == "7":checkSum()
        if opt == "8":changeSong()
        if opt.upper() == "STOP" or  "9":sys.exit()
#--------------------RANDOMIZE CURRENT SONG--------------------
def changeSong():
        songID = random.randrange(0x20)
        array[0x2607] = songID
#--------------------CONVERT ASCII TO POKEMON--------------------
def conv(a):
        return ord(a.upper())+0x3F
#--------------------CHARACTER NAME--------------------
def characterName():
        name = input("Please enter a character name, must be 7 or less characters\n")
        while(len(name) > 7):
                name = input("Name too long, has to be 7 or less\nPlease enter a 7 character name\n")
        name=name.upper()
        #Set hex values to characters
        for i in range(len(name)):
                
                print(hex(0x2598+i),"setting equal to",hex(ord(name[i])+0x3F)) 
               
                array[0x2598+i]=(ord(name[i])+0x3F)
        else:
                array[0x2598+i+1]=0x50
                print(array[0x2598+i+1])
        
#--------------------RIVAL NAME-------------------- 
def rivalName():
        name = input("Please enter a character name, must be 7 or less characters\n")
        while(len(name) > 7):
                name = input("Name too long, has to be 7 or less\nPlease enter a 7 character name\n")
        name=name.upper()
        #Set hex values to characters
        for i in range(len(name)):
                
                print(hex(0x25F6+i),"setting equal to",hex(ord(name[i])+0x3F)) 
               
                array[0x25F6+i]=(ord(name[i])+0x3F)
        else:
                array[0x25F6+i+1]=0x50
                print(array[0x25F6+i+1])
        
#--------------------PLAYER ID--------------------
def setPlayerID():
        playID = min(int(input("Please input a player ID\n")),50000)
        setTwoByte(0x2605,playID)
       
#--------------------SET POKEMON--------------------
def setPoke():
        
        if(array[0x2F2C] > 0):
                print("Pokemon found:")
                for i in range (array[0x2F2C]):
                        
                        print(list(pokemon.keys())[list(pokemon.values()).index(array[0x2F2D+i])],"in slot",i+1)
                        #print("The pokemon in slot",i,"is",pokemon[array[0x2F2C+i]])
        slot = int(input("Which slot to add pokemon? (Will overwrite pokemon if it exists)"))
        offset = (slot-1)*0x2C
        
        if(slot<=array[0x2F2C]+1):
                offset = (slot-1)*0x2C
                print("Valid location, offset is now",offset)
                currentSlot = slot
        else:
                print("Spot before it empty, put it after last pokemon")
                offset = (0x2C*(array[0x2F2C]))
                print("Offset is now",(0x2C*(array[0x2F2C])))
                currentSlot = array[0x2F2C]+1
                
        print("Current Slot is",currentSlot)
        #print("Value at", hex(0x2F34+offset), "is", array[0x2F34+offset])
        location = 0x2F34+offset
        #update party count correctly
        if(slot-array[0x2F2c] <= 1):
               print("Party count unchangeed,its now",array[0x2F2C])
        else:
               print("Slot empty")
               array[0x2F2C] = array[0x2F2C] + 0x01
               print("Updating party count",array[0x2F2C])
        poke = input("Please enter the name of a pokemon\n").replace(" ","").lower()
        #header data
        #set party species ID
        #print(0x2fd+int(offset/0x2C))
        array[0x2f2d+int(offset/0x2C)] = pokemon[poke]
        array[0x2f2d+int(offset/0x2C)+1] = 0xFF
       
        print("Setting index slot at" , hex(0x2f2d+int(offset/0x2C)), "to" , pokemon[poke])
        #print("Currently at slot",slot,"modifying data from",hex(0x2F34+offset),"to",hex(0x2F34+0x2B+offset))
        #--main data--
        print("Setting main index")
        array[location] = pokemon[poke]
        #setting hp
        hp = int(input("Please enter the current HP\n"))
        if(hp > 255):
                binary = bin(hp)[2:]
                num1 = int((binary[:len(binary)%8]),2)
                num2 = int((binary[len(binary)%8:]),2)
                array[location+0x01]=num1
                array[location+0x02]=num2
        else:
                array[location+0x02]=hp
        #set level
        level = min(255,int(input("Please enter the desired level\n")))
        array[location+0x03] = level
        array[location+0x21] = level
        print("Skipping status condition")
        #types
        ty1 = types[input("Please enter the first type\n").lower().replace(" ","")]
        ty2 = types[input("Please enter the second type\n").lower().replace(" ","")]
        array[location+0x05] = ty1
        array[location+0x06] = ty2
        print("Skipping catch rate\n")
        #moves
        print("Please enter the four moves you want\n")
        for i in range(location+0x08,location+0x0C):
                p = moves[input("Please enter a move\n").replace(" ","").lower()]
                array[i]: p
                print("Set",hex(i),"to",p)
        #original trainer id number
        playerID = min(65534,int(input("Please enter a 5 digit Original Trainer ID\n")))
        idbinary = bin(playerID)[2:]
        num1 = int((idbinary[:len(idbinary)%8]),2)
        num2 = int((idbinary[len(idbinary)%8:]),2)
        array[location+0x0C] = num1
        array[location+0x0D] = num2
        print("Skipping XP, might come back to it\n")
        print("I dont wanna do IV's,EV's, ill come back to it")
        print("Input PP Values for each moves")
        for i in range(location+0x1D,location+0x21):
                pp = int(input("Please enter a PP value\n"))
                array[i] = min(255,pp)
                print("Setting",hex(i),"to",pp)
        hpMax = int(input("Please enter the maximum HP\n"))
        setTwoByte(location+0x22,hpMax)

        attack = int(input("Please enter Attack stat\n"))
        setTwoByte(location+0x24,attack)

        defense = int(input("Please enter Defense stat\n"))
        setTwoByte(location+0x26,defense)

        speed = int(input("Please enter Speed stat\n"))
        setTwoByte(location+0x28,speed)

        special = int(input("Please enter Special stat\n"))
        setTwoByte(location+0x2A,special)


        #Trainer name        
        nameLoc = 0x303C+(0xB*(currentSlot-1))
        print(hex(nameLoc))
        nameIn = input("Please input the original trainers name, limit 10 characters\n").upper().replace(" ","")
        
        for i in range(len(nameIn)):
                array[nameLoc+i] = conv(nameIn[i])
                print("Setting",hex(nameLoc+i), "to", conv(nameIn[i]))
        else:
                array[nameLoc+i+1] = 0x50

        #Pokemon name
        pkLoc = 0x307E+(0xB*(currentSlot-1))
        print(hex(pkLoc))
        pkName = input("Please input the pokemon name, limit 10 characters\n").upper().replace(" ","")
        for i in range(len(pkName)):
                array[pkLoc+i] = conv(pkName[i])
                print("Setting",hex(pkLoc+i), "to", conv(pkName[i]))
        else:

                array[pkLoc+i+1] = 0x50
                print("Set",hex(pkLoc+i+1),"to",hex(0x50))
        
#--------------------TWO BYTE SET--------------------

def setTwoByte(loc, value):
        
        if(value > 255):
                        binary = bin(value)[2:]
                        value1 = int((binary[:len(binary)%8]),2)
                        value2 = int((binary[len(binary)%8:]),2)
                        array[loc]=value1
                        array[loc+0x01]=value2
                        print("Value greater 255, set",hex(loc),"to",value1,"and",hex(loc+0x01),"to",value2)
        else:
                        array[loc+0x01]=value
                        print("Set",hex(loc+0x01),"to",value)


#--------------------SET MONEY--------------------







def setMoney():
        money = input("Please enter a 6 digit number\n")
        while(len(money) > 6):
                money = input("The number you input was too large\nPlease enter a 6 digit number\n")
        money = str(money).zfill(6)
        
        for i in range(0,6,2):
                array[0x25F3+int(i/2)] = int(format(int(money[i]),"04b") + format(int(money[i+1]),"04b"),2)
                print("setting",hex(0x25F3+int(i/2)),"to",int(format(int(money[i]),"04b") + format(int(money[i+1]),"04b"),2))
        
#if(opt=="3"):


#--------------------CHECKSUM+WRITE--------------------
def checkSum():
        
        print("Calculating Checksum")
        sum = 0xff
        for c in array[0x2598:0x3523]:
                sum-=c
                array[0x3523] = sum&0xff
       
        f.seek(0,0)
        print("Writing")
        f.write(array)
        f.close()
        print("Done")
        
#--------------------RUNNER--------------------

while(True):
        askUsr()
