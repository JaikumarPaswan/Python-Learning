class Remote:
    pass

class Player:  #Encapsulation:- The function of player is capsuled in a class. So this is Encapsulation
    def moveRight(self):
        pass
    
    def moveLeft(self):
        pass

    def moveTop(self):
        pass

remote1 = Remote() #object
player1 = Player()

if(remote1.isLeftPressed()): #abstraction
    player1.moveLeft()