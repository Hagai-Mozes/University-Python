''' Exercise #8. Python for Engineers.'''
#########################################
# Question 1 - do not delete this comment
#########################################
class RoomError(Exception):
    #A subclass of Exception that defines a new error type
    #DO NOT change this class
    pass

class Room:
    def  __init__(self, floor, number, guests, clean_level, rank, satisfaction = 1.0):
        if type(rank)!=int or type(clean_level)!=int or (type(satisfaction)!=float and type(satisfaction)!= int):
            raise TypeError ("Argument type error")
        if not(10>=clean_level>=1 and 3>=rank>=1 and 5>=satisfaction>=1):
            raise ValueError ("Argument value error")
        self.floor=floor
        self.number=number
        self.guests=self.lower_lst(guests)
        self.clean_level=clean_level
        self.rank=rank
        self.satisfaction=float(satisfaction)
        

    def __repr__(self):
        if self.guests == []:
            guests_str = "empty"
        else:
            guests_str=""
            for i in self.guests[:-1]:
                guests_str+=i+", "
            guests_str+=self.guests[-1]
                        
        return "floor: " + str(self.floor) + "\nnumber: " + str(self.number) + "\nguests: " + guests_str + "\nclean_level: " + str(self.clean_level) + "\nrank: " + str(self.rank) + "\nsatisfaction: " + str(round(self.satisfaction,1))

    def lower_lst(self, lst):
        low = []
        for i in lst:
            low.append(i.lower())
        return low

    def is_occupied(self):
        if self.guests == []:
            return False
        else:
            return True
        

    def can_clean(self):
        return True
    
    def clean(self):
        if self.can_clean():
            self.clean_level=min(10,self.clean_level+self.rank)
        else:
            raise RoomError ("Room cannot be cleaned")

    def better_than(self, other):
        if isinstance(other,Room):
            if (self.rank,self.floor,self.clean_level)>(other.rank,other.floor,other.clean_level):
                return True
            else:
                return False
        else:
            raise TypeError ("Other must be an instance of Room")

    def check_in(self, guests):
        if self.is_occupied():
            raise RoomError ("Cannot check-in new guests to an occupied room")
        else:
            self.guests = self.lower_lst(guests)
            self.satisfaction=1.0
            

    def check_out(self):
        if self.guests==[]:
            raise RoomError ("Cannot check-out an empty room")
        else:
            self.guests = []
        
    def move_to(self, other):
        if not self.is_occupied():
            raise RoomError ("Cannot move guests from an empty room")
        elif other.is_occupied():
            raise RoomError ("Cannot move guests into an occupied room")
        else:
            other.guests = self.guests
            if other.better_than(self):
                other.satisfaction=min(5.0,self.satisfaction+1.0)
            else:
                other.satisfaction=self.satisfaction
            self.guests=[]
            

#########################################
# Question 2 - do not delete this comment
#########################################
class BudgetRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,\
                  rank=1, satisfaction=1.0, clean_stock=0):
        super().__init__(floor, number, guests, clean_level, rank, satisfaction)
        self.clean_stock=clean_stock
        
    def __repr__(self):
        return super().__repr__() + "\ntype: BudgetRoom\nclean_stock: " + str(self.clean_stock)

    def can_clean(self):
        if self.clean_stock > 0:
            return True
        else:
            return False
        
    def clean(self):
        super().clean()
        self.clean_stock -=1

    def check_in(self, guests):
        super().check_in(guests)
        self.clean_stock=0

    def move_to(self,other):
        super().move_to(other)
        if isinstance(other, BudgetRoom):
            other.clean_stock = self.clean_stock

    def grant_clean(self):
        if self.is_occupied():
            self.clean_stock +=1
            self.satisfaction = min(5.0,self.satisfaction+0.5)
        else:
            raise RoomError ("Cannot grant an empty room")

    def grant_snack(self):
        if self.is_occupied():
            self.satisfaction = min(5.0,self.satisfaction + 0.8)
            self.clean_level = max(1,self.clean_level-1)
        else:
            raise RoomError ("Cannot grant an empty room")
            
                 
class LegacyRoom(Room):
    def  __init__(self, floor, number, guests, clean_level,\
                  rank=2, satisfaction=1.0,\
                  minibar_drinks = 2, minibar_snacks = 2):
        super().__init__(floor, number, guests, clean_level, rank, satisfaction)
        self.minibar_drinks, self.minibar_snacks = minibar_drinks, minibar_snacks 

    def __repr__(self):
        return super().__repr__() + "\ntype: LegacyRoom\nminibar_drinks: " + str(self.minibar_drinks) + "\nminibar_snacks: " + str(self.minibar_snacks)

    def check_in(self,guests):
        super().check_in (guests)
        self.minibar_drinks, self.minibar_snacks = 2, 2  

    def add_drinks(self, quantity):
        self.minibar_drinks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.2*quantity)
    
    def add_snacks(self, quantity):
        self.minibar_snacks += quantity
        self.satisfaction = min(5.0, self.satisfaction + 0.3*quantity)
        self.clean_level = max(1, self.clean_level - 1)
       
#########################################
# Question 3 - do not delete this comment
#########################################
class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms=rooms
            
    def __repr__(self):
        budget_count, legacy_count, rooms_count, occ_count = 0,0,0,0
        for i in self.rooms:
            if isinstance(i,BudgetRoom):
                budget_count+=1
            elif isinstance(i,LegacyRoom):
                legacy_count+=1
            else:
                rooms_count+=1

            if i.is_occupied():
                occ_count+=1
            
        return self.name + " hotel has:\n" + str(budget_count) + " BudgetRooms\n" + str(legacy_count) + " LegacyRooms\n" + str(rooms_count) + " other room types\n" + str(occ_count) + " occupied rooms"
                              
    def check_in(self, guests, rank):
        for room in self.rooms:
            if (not room.is_occupied()) and (room.rank == rank):
                room.check_in(guests)
                return room
        return None

    def check_out(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                room.check_out()
                return room
        return None
    

    def upgrade(self, guest):
        for room in self.rooms:
            if guest.lower() in room.guests:
                for better in self.rooms:
                    if better.better_than(room):
                        try:
                            room.move_to(better)
                            return better
                        except RoomError:
                            next
                return None
        return None

#########################################
# Question 3 supplement - do not delete this comment
#########################################
def test_hotel():
    rooms = [BudgetRoom(15, 140, [], 5), LegacyRoom(12, 101, ["Ronen", "Shir"], 6),\
             BudgetRoom(1, 2, ["Liat"], 7), Room(2, 23, [], 6, 3)]
    h = Hotel("Dan",rooms)
    test_sep = '\n------------------'
    print ('CALL: h.upgrade("Liat")\n', h.upgrade("Liat"), test_sep, sep="")
    print ('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep,  sep="")
    print ('CALL: h.check_out("Ronen")\n', h.check_out("Ronen"), test_sep, sep="")
    print ('CALL: h.check_in(["Alice", "Wonder"], 2)\n', h.check_in(["Alice", "Wonder"], 2), test_sep, sep="")
    print ('CALL: h.check_in(["Alex"], 3)\n', h.check_in(["Alex"], 3), test_sep, sep="")
    print ('PRINT h:\n', h, test_sep, sep="")
    print ('CALL: h.check_in(["Oded", "Shani"], 3)\n', h.check_in(["Oded", "Shani"], 3), test_sep, sep="")
    print ('CALL: h.check_in(["Oded", "Shani"], 1)\n', h.check_in(["Oded", "Shani"], 1), test_sep, sep="")
    print ('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print ('CALL: h.check_out("Liat")\n', h.check_out("Liat"), test_sep, sep="")
    print ('PRINT h:\n', h, test_sep, sep="")
test_hotel()


#########################################
# Main code - do not delete this comment
# You can add more validation cases below
#########################################

##test_hotel() 
## After you are done implenting all classes and methods, you may comment-in the call to test_hotel() and compare the results with the content of test_hotel_output.txt
