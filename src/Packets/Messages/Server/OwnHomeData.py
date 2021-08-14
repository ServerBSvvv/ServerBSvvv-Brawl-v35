from Utils.Writer import Writer
from database.DataBase import DataBase


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        # sub_6BB088 start
        self.writeVInt(2021091) #Year * 1000 + day_of_year
        self.writeVInt(72152)
        self.writeVInt(5000)
        self.writeVInt(5000)
        self.writeVInt(122)
        self.writeVInt(200)
        self.writeVInt(99999)
        
        self.writeScID(28, 66) # Player icon
        self.writeScID(43, 3) # Player name color
        
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0) # boolean
        self.writeVInt(1000)
        self.writeVInt(26000)
        self.writeVInt(20)
        self.writeVInt(5699999)
        
        # sub_5705E4 start
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        # sub_5705E4 end
        
        self.writeByte(0) # 3 bools
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0) # v17 - Shop Array ?
        
        self.writeVInt(0) # v21 - Array
        
        self.writeVInt(200)
        self.writeVInt(0)
        
        self.writeVInt(0) # Array
        
        self.writeVInt(99999)
        self.writeVInt(0)
        
        self.writeScID(16, 0) # Menu Brawler
        
        self.writeString("RU")
        self.writeString("ServerBSvvv")
        
        self.writeVInt(1) # v26 - Array
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVInt(1) # v29 - Array
        self.writeVInt(0)
        self.writeScID(16, 0)
        self.writeVInt(0)
        
        self.writeVInt(1) # SeasonArray (v32)
        self.writeVInt(5)
        self.writeVInt(0) # Pass Tokens
        self.writeByte(1)
        self.writeVInt(5)
        self.writeByte(0)
        
        self.writeVInt(0) # v35 - Array
        
        self.writeByte(1) # boolean need set to true!!!
        self.writeVInt(0) # Quests Array
        
        self.writeByte(1) # boolean need set to true!!!
        self.writeVInt(0) # Pins Array
        
        self.writeByte(1) # Array ?????
        #self.writeVInt(1)
        self.writeVInt(100)
        self.writeVInt(10)
        self.writeVInt(30)
        self.writeVInt(3)
        self.writeVInt(80)
        self.writeVInt(10)
        self.writeVInt(40)
        self.writeVInt(1000)
        self.writeVInt(500)
        self.writeVInt(50)
        self.writeVInt(999900)
        self.writeVInt(0)
        
        self.writeInt(0)
        
        #sub_6BB088 end
        
        # sub_1B9CB8 start
        self.writeVInt(0)
        
        self.writeVInt(16) # v4
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 21, 22, 23, 24]:
            self.writeVInt(x)
        
        maps = [377, 7, 26]
        self.writeVInt(len(maps)) # Events
        
        for x in maps:
            self.writeVInt(0)
            if maps.index(x) == 0:
                self.writeVInt(7)
            else:
                self.writeVInt(maps.index(x) + 1)
            self.writeVInt(0)
            self.writeVInt(75992)
            self.writeVInt(10)
            
            self.writeScID(15, x)
            
            self.writeVInt(3)
            self.writeVInt(0)
            self.writeString()
            
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0) #modifier array
            
            self.writeVInt(0)
            self.writeVInt(0)
            
            self.writeByte(0) #ebanuty array
            
            self.writeVInt(0)
            
            self.writeByte(0)
        #Event end
        
        self.writeVInt(0) # empty events array
        
        self.writeVInt(0) #sub_457814
        self.writeVInt(0) #sub_457814
        self.writeVInt(0) #sub_457814
        self.writeVInt(0) #sub_457814
        
        self.writeByte(0) #boolean
        
        self.writeVInt(0) # Array v18
        
        self.writeVInt(0) # Array v21
        
        self.writeVInt(0) # Array v24
        
        self.writeVInt(0) # Array result
        # sub_1B9CB8 end
        
        self.writeInt(0) #LongLong
        self.writeInt(1)
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeByte(0) # boolean
        self.writeVInt(0)
        
        self.writeVInt(0) # Array result
        
        #LogicClientAvatar start
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(1)
        
        self.writeString("Guest")
        self.writeByte(1) #nameset
        self.writeInt(0)
        
        self.writeVInt(8) # commodity count
        
        self.writeVInt(400)
        for x in range(400):
            self.writeVInt(23)
            self.writeVInt(x)
            self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0) # trophies for rank
        self.writeVInt(0) # upgrade points
        self.writeVInt(0)
        self.writeVInt(47)
        for x in range(47):
            self.writeScID(16, x)
            self.writeVInt(665) # power level
        self.writeVInt(0)
        self.writeVInt(0)
        #commoditys end
        
        self.writeVInt(1000000000) # Gems
        self.writeVInt(0) # Free Gems?
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2) #result
        
        self.writeVInt(0) #timestamp end
        
        print("[*] Message OwnHomeData has been sent.")
