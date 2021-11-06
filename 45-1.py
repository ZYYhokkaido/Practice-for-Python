class Demo:
    def __getattr__(self,name):
        print("FishC")

    def __setattr__(self,name,value):
        return super().__setattr__(name,value)

    def __getattribute__(self,name):
        return super().__getattribute__(name)


