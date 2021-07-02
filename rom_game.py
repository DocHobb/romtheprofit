import discord
import os
import random

client = discord.Client()
rule_list = [1,2,3,5,11,12,18,22,24,27,49,54]
rule_list_verbage = {1:"first",
        2:"second",
        3:"third",
        5:"fifth",
        11:"eleventh",
        12:"twelfth",
        18:"eighteenth",
        22:"twenty-second",
        24:"twenty-fourth",
        27:"twenty-seventh",
        49:"forty-ninth",
        54:"fifty-fourth"
        }
rules = {1:" the customer is always right!",
        2:" war is good for trade",
        3:" peace is good for trade",
        5:" everything has a price",
        11:" never question the customer",
        12:" everything is for sale",
        18:" everyone is a favorite customer",
        22:" the customer doesn't care to know everything",
        24:" knowledge is profit",
        27:" never tell where you get profit",
        49:" the dead can't profit, but you can profit from the dead",
        54:" the price is set"
        }
quote_list = [0,1,2,3,4,5]
'''   
random_number = random.choice(rule_list)
random_start = random.choice(quote_list)

random_answer = {0:"The " + rule_list_verbage[random_number] + " rule of profit is",
         1:"My friend, a small tidbit of wisdom for you. The  " + rule_list_verbage[random_number] + " rule of profit is" ,
         2:"How about this one? The " + rule_list_verbage[random_number] + " rule of profit is of course that",
         3:"Of course dear traveler. From my own book of profit. The  " + rule_list_verbage[random_number] + " rule of profit is",
         4:"Make sure you commit this one to memory dear friend! The " + rule_list_verbage[random_number] + " rule of profit is" ,
         5:"This one came to me in a great moment of inspiration. The " + rule_list_verbage[random_number] + " rule of profit is"
         }

answer = {0:"The " + rule_list_verbage[random_number] + " rule of profit is",
         1:"My friend, what have I told you. The " + rule_list_verbage[random_number] + " rule of profit is" ,
         2:"Why, the " + rule_list_verbage[random_number] + " rule of profit is of course that",
         3:"Oh, the " + rule_list_verbage[random_number] + " rule of profit? That would be that",
         4:"How could you forget the " + rule_list_verbage[random_number] + "rule of profit. Not very smart of you indeed. It is clearly" ,
         5:"OH that IS a good rule! Good rule indeed! It's a personal favorite you know. The " + rule_list_verbage[random_number] + " rule of profit is"
         }  
 '''        
         
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel()
    await channel.send("Hello! It is I, Rom of the Profit! I'm now online to share with you my wisdoms")
    await channel.send("For a list of help and commands, type $HELP")

@client.event
async def on_disconnect():
    await client.get_channel().send("I am off to go seek more wares, all the better to sell to you later")

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content.startswith("$HELP"):
        await message.channel.send(
        """
        Current Capabilities and Rules of Rom

        1. Always start your sentence with "Rom" (I.e 'Rom, what is....')

        2. Rom can currently recite any of the known rules or a random rule

        3. Rom can not take integers. He will respond to "1st, first, one, etc." but not "1"

        Ex: 
        "Rom give me any rule"
        "Rom give me a random rule"
        "Rom, what is rule eleven?"
        "Rom give me the forty-ninth rule please"
        
        To list the rules:
        $LIST
        or ask Rom for a list of the rules (You must use the words rom and list)
        """
        )
        
    if message.content.startswith("$LIST"):
        await message.channel.send("""
        Dear traveler, these are the Rules of Profit that we have shared so far
        1,2,3,5,11,12,18,22,24,27,49,54
        You may ask me to share them with you at any time!
        """)
 
    random_number = random.choice(rule_list)
    random_start = random.choice(quote_list)
    test = message.content.lower()
    if test.startswith('rom'):
        if " one" in test:
            random_number = 1
        elif " first" in test:
            random_number = 1 
        elif " 1st" in test:
            random_number = 1
        elif " two" in test:
            random_number = 2 
        elif " second" in test:
            random_number = 2
        elif "2nd" in test:
            random_number = 2            
        elif " three" in test:
            random_number = 3
        elif "3rd" in test:
            random_number = 3
        elif " third" in test:
            random_number = 3
        elif " five" in test:
            random_number = 5
        elif "5th" in test:
            random_number = 5
        elif " fifth" in test:
            random_number = 5
        elif " eleven" in test:
            random_number = 11
        elif "11th" in test:
            random_number = 11
        elif " eleventh" in test:
            random_number = 11
        elif " twelve" in test:
            random_number = 12
        elif "12th" in test:
            random_number = 12
        elif "twelfth" in test:
            random_number = 12
        elif "twelf" in test:
            random_number = 12            
        elif " eighteen" in test:
            random_number = 18
        elif "18th" in test:
            random_number = 18
        elif "eighteenth" in test:
            random_number = 18
        elif " twenty-second" in test:
            random_number = 22
        elif "22nd" in test:
            random_number = 22
        elif "twentysecond" in test:
            random_number = 22
        elif "twentytwo" in test:
            random_number = 22
        elif "twenty-two" in test:
            random_number = 22
        elif " twenty-fourth" in test:
            random_number = 24
        elif "24th" in test:
            random_number = 24
        elif "twenty-forth" in test:
            random_number = 24
        elif "twentyfour" in test:
            random_number = 24
        elif"twenty-four" in test:
            random_number = 24
        elif "twentyfourth" in test:
            random_number = 24
        elif " twenty-seventh" in test:
            random_number = 27
        elif "27th" in test:
            random_number = 27
        elif "twenty-seven" in test:
            random_number = 27
        elif "twentyseventh"  in test:
            random_number = 27
        elif "twentyseven" in test:
            random_number = 27
        elif " forty-ninth" in test:
            random_number = 49
        elif "49th" in test:
            random_number = 49
        elif "fortyninth" in test:
            random_number = 49
        elif "fourtyninth" in test:
            random_number = 49
        elif "fourty-ninth" in test:
            random_number = 49
        elif "fourtynine" in test:
            random_number = 49
        elif "fortynine" in test:
            random_number = 49
        elif "forty-nine" in test:
            random_number = 49
        elif "fourty-nine" in test:
            random_number = 49
        elif " fifty-fourth" in test:
            random_number = 54
        elif "54th" in test:
            random_number = 54            
        elif "fiftyforth" in test:
            random_number = 54 
        elif "fiftyfourth" in test:
            random_number = 54 
        elif "fifty-fourth" in test:
            random_number = 54 
        elif "fifty-forth" in test:
            random_number = 54
        elif "fiftyfour" in test:
            random_number = 54
        elif "fifty-four" in test:
            random_number = 54
        random_answer = {0:"The " + rule_list_verbage[random_number] + " rule of profit is",
                 1:"My friend, a small tidbit of wisdom for you. The  " + rule_list_verbage[random_number] + " rule of profit is" ,
                 2:"How about this one? The " + rule_list_verbage[random_number] + " rule of profit is of course that",
                 3:"Of course dear traveler. From my own book of profit. The  " + rule_list_verbage[random_number] + " rule of profit is",
                 4:"Make sure you commit this one to memory dear friend! The " + rule_list_verbage[random_number] + " rule of profit is" ,
                 5:"This one came to me in a great moment of inspiration. The " + rule_list_verbage[random_number] + " rule of profit is"
                 }

        answer = {0:"The " + rule_list_verbage[random_number] + " rule of profit is",
                 1:"My friend, what have I told you. The " + rule_list_verbage[random_number] + " rule of profit is" ,
                 2:"Why, the " + rule_list_verbage[random_number] + " rule of profit is of course that",
                 3:"Oh, the " + rule_list_verbage[random_number] + " rule of profit? That would be that",
                 4:"How could you forget the " + rule_list_verbage[random_number] + " rule of profit. Not very smart of you indeed. It is clearly" ,
                 5:"OH that IS a good rule! Good rule indeed! It's a personal favorite you know. The " + rule_list_verbage[random_number] + " rule of profit is"
                 }
              
        if random_number in rule_list:
            #await message.channel.send(answer[random_start] + rules[random_number])
            messager = answer[random_start] + rules[random_number]
        
        if "list" in test:
            messager = ("""
            Dear traveler, these are the Rules of Profit that we have shared so far
            1,2,3,5,11,12,18,22,24,27,49,54
            You may ask me to share them with you at any time!
            """)
        elif "random" in test:
            #await message.channel.send(random_answer[random_start] + rules[random_number])
            messager = random_answer[random_start] + rules[random_number]
        elif "any" in test:
            messager = random_answer[random_start] + rules[random_number]
            #await message.channel.send(random_answer[random_start] + rules[random_number])  
        
        await message.channel.send(messager)
        #await message.channel.send(random_number)

client.run("")