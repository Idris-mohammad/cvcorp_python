class Theater:
    def __init__(self,m,t):
        self.movie=m
        self.tickets=t
        self.tickets_booked=0
    def ticket_count(self,t):
        self.tickets_booked+=t
    def __str__(self):
        k=f'''movie:{self.movie}
tickets remaining:{self.tickets-self.tickets_booked}'''
        return k
T1=Theater("The  Odyssey",225)
print(T1)
T1.ticket_count(10)
print(T1)