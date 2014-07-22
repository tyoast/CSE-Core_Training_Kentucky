from __future__ import print_function
''' 
PrisonerDilemma.py allows hard-coding different strategies
for the Iterative Prisoners Dilemma, the canonical game of game-theory.
Each strategy plays 100 to 200 rounds against each other strategy.
The results of all previous rounds within a 100-200 round stretch are known
to both players. 

play_tournament() executes the tournament and stores output in tournament.txt

Players should each code their strategies in their assigned section of code.

'''

import random
def play_round(player1, player2, history1, history2, score1, score2):
    '''
    Calls the get_action() function which will get the characters
    'c' or 'b' for silent or betray for each player.
    The hitsory is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 4-tuple with updated histories and scores
    (history1, history2, score1, score2)
    '''
    
    REWARD = 200 # when both players collude
    TEMPTATION = 300 # when you betray your partner
    SUCKER = -100 # when your partner betrays you
    PUNISHMENT = 0 # when both players betray each other
    # Keep T > R > P > S to be a Prisoner's Dilemma
    # Keep 2R > T + S to be an Iterative Prisoner's Dilemma
    
    #Get the two players' actions and remember them.
    action1 = get_action(player1, history1, history2, score1, score2)
    action2 = get_action(player2, history2, history1, score2, score1)
   
    #Append the actions to the previous histories, to return
    new_history1 = history1 + action1
    new_history2 = history2 + action2
    
    
    #Change scores based upon player actions
    if action1 not in ('c','b') or action2 not in ('c','b'):
    # Do nothing if someone's code returns an improper action
        new_score1 = score1
        new_score2 = score2
        new_score7 = score7
        
    else: 
    #Both players' code provided proper actions
        if action1 == 'c':
            if action2 == 'c':
                # both players collude; get reward
                new_score1 = score1 + REWARD
                new_score2 = score2 + REWARD
            else:
                # players 1,2 collude, betray; get sucker, tempation
                new_score1 = score1 + SUCKER
                new_score2 = score2 + TEMPTATION
        else:
            if action2 == 'c':
                # players 1,2 betray, collude; get tempation, sucker
                new_score1 = score1 + TEMPTATION
                new_score2 = score2 + SUCKER                       
            else:
                # both players betray; get punishment   
                new_score1 = score1 + PUNISHMENT
                new_score2 = score2 + PUNISHMENT
                    
    #send back the updated histories and scores
    return (new_history1, new_history2, new_score1, new_score2)
   
def play_iterative_rounds(player1, player2):
    '''
    Plays a random number of rounds (between 100 and 200 rounds) 
    of the iterative prisoners' dilemma between two strategies.
    identified in the parameters as integers.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600) 
    but with much longer strings 
    '''
    number_of_rounds = random.randint(100,200)
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        moves1, moves2, score1, score2 = \
            play_round(player1, player2, moves1, moves2, score1, score2)
    return (moves1, moves2, score1, score2)

def get_action(player, history, opponent_history, score, opponent_score):
    '''Gets the strategy for the player, given their own history and that of
    their opponent, as well as the current scores within this pairing.
    The parameters history and opponenet history are strings with one letter
    per round that has been played so far: either an 'c' for collude or a 'b' for 
    betray. The function should return one character, 'c' or 'b'. 
    The history strings have the first round between these two players 
    as the first character and the most recent round as the last character.'''
      
    #This example player always colludes
    if player == 0:
        return 'c'
    
    #This example player always betrays.      
    elif player == 1:
        return 'b'
    
    #This example player is silent at first and then 
    #only betrays if they were a sucker last round.
    elif player == 2:
        if len(opponent_history)==0: #It's the first round: collude
            return 'c'
        elif history[-1]=='c' and opponent_history[-1]=='b':
            return 'b' # betray is they were sucker last time
        else:
            return 'c' #otherwise be silent

    # EACH STUDENT TEAM CAN CHANGE ONE OF THESE elif SEGMENTS OF CODE.

    #
    elif player == 3:
        return 'c'
        
    #
    elif player == 4:
        return 'c'
        
    #
    elif player == 5:
        return 'c'
        
    #
    elif player == 6:
        return 'c'
        
    #
    elif player == 7:
        #This example player is silent at first and then 
    #only betrays if they were a sucker last round.
        if len(opponent_history)==0: #It's the first round: collude
            return 'c'
        elif history[-1]=='c' and opponent_history[-1]=='b':
            return 'b' # betray is they were sucker last time
        else:
            return 'c' #otherwise be silent

       
        
    #
    elif player == 8:
        return 'c'
        
    #
    elif player == 9:
        return 'c'
        
    #
    elif player == 10:
        return 'c'
        
    #
    elif player == 11:
        return 'c'

    #
    elif player == 12:
        return 'c'
        
def play_tournament(num_players):
    #create a list of zeros, one per player
    scores = []
    for i in range(num_players):
        scores += [0]
    
    
    #EACH STUDENT TEAM CAN CHANGE ONE OF THESE LINES:
    # Give a name to your algorithm here
    teams = ['loyal',#0
             'backstabber',#1
             'loyal vengeful',#2
             '',#3
             '',#4
             '',#5
             '',#6
             'Play Nice',#7
             '',#8
             '',#9
             '',#10
             '',#11
             '',#12
             '']#13    
             
            
    #create a file for the round-by-round results
    results = open('tournament.txt','w')
    for player1 in range(num_players):
        for player2 in range(player1):
            # play a game between the two
            moves1, moves2, score1, score2 = \
                play_iterative_rounds(player1, player2)
            
            # store the results in the file
            if (num_players != 7):
                score1 = 0
                score2 = 0
            
            results.write(str(score1) + ' vs. ' + str(score2)+'\n')
            results.write(moves1+'\n')
            results.write(moves2+'\n')
            results.write('\n')
            
            #accumulate the results for the two players
            scores[player1] += score1*1.0/len(moves1)
            scores[player2] += score2*1.0/len(moves2)
            
    #report the results on screen        
    for player in range(num_players):
        print('player ' + str(player) , ': ' , 
               str(scores[player]) , ' points-- ',
               teams[player])
    