# Import the random library to use for the dice later
import random


# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    if combat_strength <= 0 or combat_strength >= 7:
        print("Hero cannot fight with 0 combat strength. Cannot exceed maximum strength of 6")
    elif m_health_points <= 0 or m_health_points >= 21:
        print("Monster must be alive, and not exceed the maximum health points 20")
    else:
        ascii_image = """
                                    @@   @@ 
                                    @    @  
                                    @   @   
                   @@@@@@          @@  @    
                @@       @@        @ @@     
               @%         @     @@@ @       
                @        @@     @@@@@     
                   @@@@@        @@       
                   @    @@@@                
              @@@ @@                        
           @@     @                         
       @@*       @                          
       @        @@                          
               @@                                                    
             @   @@@@@@@                    
            @            @                  
          @              @                  

      """
        print(ascii_image)
        print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
        if combat_strength >= m_health_points:
            # Player was strong enough to kill monster in one blow
            m_health_points = 0
            print("You have killed the monster")
        else:
            # Player only damaged the monster
            m_health_points -= combat_strength

            print("You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    if m_combat_strength <= 0 or m_combat_strength >= 7:
        print("Monster cannot fight with 0 combat strength. Cannot exceed maximum strength of 6")
    elif health_points <= 0 or health_points >= 21:
        print("Hero must be alive, and not exceed the maximum health points 20")
    else:
        ascii_image2 = """                                                                 
               @@@@ @                           
          (     @*&@  ,                         
        @               %                       
         &#(@(@%@@@@@*   /                      
          @@@@@.                                
                   @       /                    
                    %         @                 
                ,(@(*/           %              
                   @ (  .@#                 @   
                              @           .@@. @
                       @         ,              
                          @       @ .@          
                                 @              
                              *(*  *      
                 """
        print(ascii_image2)
        print("Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
        if m_combat_strength >= health_points:
            # Monster was strong enough to kill player in one blow
            health_points = 0
            print("Player is dead")
        else:
            # Monster only damaged the player
            health_points -= m_combat_strength
            print("The monster has reduced Player's health to: " + str(health_points))
    return health_points

