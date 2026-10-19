# # 1. wap to print two integer number:

# a=int(input("Enter a number first:"))
# b=int(input("Enter a number second:"))

# x="Darshan"
# y="Pratik"
# sum=x+y


class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
        
    def __str__(self):
        return f"{self.hr} {self.min} {self.sec}"
   
    def __add__(self,other):
    #     thr=self.hr+other.hr
    #     tmin=self.min+other.min
    #     tsec=self.sec+other.sec
    #   return Time(thr,tmin,tsec)
        tsec=self.sec+other.sec
        emin=tsec//60
        tsec=tsec%60
        tmin=self.min+other.min+emin
        ehr=tmin%60
        tmin=tmin%60
        thr=self.hr+other.hr+ehr
        return Time(thr,tmin,tsec)

t1=Time(12,33,55)
t2=Time(6,30,56)
a=t1+t2
print(a)