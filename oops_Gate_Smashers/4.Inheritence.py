class OTTSubscription:
    def __init__(self,subscription_id, plan, total_payment):
        self.id = subscription_id
        self.plan = plan
        self.payment = total_payment

    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribed to the {self.plan} plan")

    def unsubscribe(self):
        print(f"Subscriber with {self.id} id Unsubscribed to the {self.plan} plan")



class PremiumSubscription(OTTSubscription):   #parent class is written in brackets
    def __init__(self, subscription_id, plan, total_payment, screens):
        super().__init__(subscription_id,plan,total_payment)   #' super().__init__ ' is used to inherit properties of parent class
        self.max_screens = screens

    def set_max_screens(self,screens):
        self.max_screens = screens
        print(f"maximum screen set to {self.max_screens} in the Premium Plan")

    

netflix = PremiumSubscription(1212, "yearly", 999, 4)
netflix.subscribe()
netflix.set_max_screens(4)





#parent class also called as super-class

#child class also called as sub-class has the ability to use every property and 
#method of the parent class and also has its own unique properties

#parent cannot use properties of child