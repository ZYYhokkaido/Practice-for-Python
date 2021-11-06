class ticket:
    money=100
    def __init__(self,Weekend=False,Child=False):
        if Weekend==True:
            self.w=1.2
        else:
            self.w=1

        if Child==True:
            self.discount=0.5
        else:
            self.discount=1

    def calMoney(self,num):
        return self.money*self.w*self.discount*num

adult=ticket()
child=ticket(Child=True)

print("2个成年人加1个儿童的票价为%.2f"%(adult.calMoney(2)+child.calMoney(1)))
    


    
