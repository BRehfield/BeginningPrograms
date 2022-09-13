from multiprocessing.connection import wait
from operator import truth
import random
from urllib import response

def roll(n):
        result = random.randint(1, n)
        return result

result = roll(20)


while True:
    

    name = input('Enter Your Name: ')
    print(f' Greetings {name}! Welcome to the 41st Millennium there is only war happy hunting!')

    start = input('Ready to fight for your god Emperor? yes or no?: ')
    
    if start == 'yes':
        print("Okay choose your Weapon and prepare for battle")
        
        if start == 'yes':
            print('Oh your just a newly conscripted grunt then your only choice is a lasgun good luck!')
            setting = input('Do you wish to go into the forest or into the city?: ')
    else:
        print('HERESY!!! You are now dead...')
        quit()


    if setting == 'forest':
        print('Welcome to mighty forest on the planet Catachan one of the most infamous Death Worlds out there. happy hunting!')
        
        if setting == 'forest':
            response = input('Would you like to go on a patrol or wait around in the middle of the forest? ')
            
            if  response == 'patrol':
                print('You ran into a hideous bear looking creature he is about to charge!! Shoot him!!!')
                print('roll the Die to see if you hit or miss.')
                
                if  response == 'patrol':
                    response = input("Type /roll to roll the dice. ")
                    
                    if response == '/roll':
                        print(result)
                        
                        if result >= 9:
                            print("You've successfully defeated the creature.")
                            print('Now that you have successfully completed your patrol you head back to the city to rest.')
                            print("GOOD JOB you have survived the first day.")
                            quit()
                        
                        else:
                            print("You've missed the creature and Died...")
                            quit()
  
            if response == 'wait':
                print("You wait around for hours until you where found by a NCO...")
                print("The NCO ask you why are you waiting around?")
                print("Lie about waiting around or tell him the truth.")
                response = input("Type lie or truth. ")
                
                if response == 'truth':
                    print(" Useless grunt...")
                    print("You're Dead...")
                    quit()

                if response == 'lie':
                    print('Okay head back to the city and find your command unit.')
                
                else:
                    quit()
   
   #---------------------------------------------------------------------------------------------------------- 
    
    if setting == 'city':
        print('Welcome to Ultima Segmentum the pride and joy of Catachan the most infamous Death World out there.')
        response = input('Where would you like to go to the down the street or down the alley? ')
        
        if response == 'street':
            print("You've ran into lost of foot traffic. It takes a long time to get through the city.")
            print("A couple Hours later however you have arrived at the command center.")
            response = input("Do you want to go inside the command center or do you wish to continue to the barracks? ")

            if response == 'barracks':
                print("You've arrived at the barracks and found your living arrangments a bunk bed...")
                response = input("do you wish to sleep or explore? type sleep or explore. ")
                
                if response == 'explore':
                    print('You take a look around and find nothing intresting.')
                    print('All of a sudden you get yelled at by an NCO who is giving orders.')
                    response = input("Do you want to listen and follow orders or run? Type follow or run. ")
                    
                    if response == "follow":
                        print("Good job for falling in line")
                        quit()
                    if response == "run":
                        print("Heretic!! You've been shot dead...")
                        quit()
                    
            if response == 'sleep':
                print('Good Night')
            
            else:
                quit()
        
    if response == 'alley':
        print("You wonder into a dark alley and run into a group of thugs who are looking to steal stuff.")
        response = input("Type /roll to kill them. ")
            
        if response == '/roll':
               print(result)
        
        if result >= 10:
            print("you've killed them all good job now make your way to the barracks.")
                    
        else:
            print("You've Died...")
            quit()