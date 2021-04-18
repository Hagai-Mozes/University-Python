""" Exercise #7. Python for Engineers."""


#########################################
# Question 1 - do not delete this comment
#########################################


class Beverage:
        def __init__(self, name, price, is_diet):
                self.name, self.is_diet = name, is_diet
                if price > 0:
                        self.price = price
                else:   
                        raise ValueError ("The price must be bigger then zero")
                
        def get_final_price(self, size="Large"):
                if size=="Large":
                        return self.price
                elif size=="XL":
                        return 1.25*self.price
                elif size=="Normal":
                        return 0.75*self.price
                else:
                        raise ValueError ("The size does not supported")
                        

#########################################
# Question 2 - do not delete this comment
#########################################


class Pizza:
        def __init__(self, name, price, calories, toppings):
                self.name, self.toppings = name, toppings
                if price>0 and calories>0:
                        self.price, self.calories = price, calories
                else:
                        raise ValueError ("Price and Toppings must be bigger then zero")

        def get_final_price(self, size="Family"):
                if size=="Family":
                        return self.price
                elif size=="XL":
                        return 1.15*self.price
                elif size=="Personal":
                        return 0.60*self.price

        def add_topping(self, topping, calories, price):
                if topping not in self.toppings:
                        self.toppings.append(topping)
                        self.price+=price
                        self.calories+=calories
                else:
                        raise ValueError (topping, "is already on the pizza")

        def remove_topping(self, topping, calories, price):
                if topping in self.toppings:
                        self.toppings.remove(topping)
                        self.price-=price
                        self.calories-=calories
                        if self.price<=0 or self.calories<=0:
                                raise ValueError ("The pizza price and calories must be bigger then zero") 
                else:
                        raise ValueError (topping, "is not on the pizza")


#########################################
# Question 3 - do not delete this comment
#########################################


class Meal:

        def __init__(self, beverage, pizza):
                self.beverage, self.pizza = beverage, pizza

        def get_final_price(self, beverage_size, pizza_size):
                return self.beverage.get_final_price(beverage_size) + self.pizza.get_final_price(pizza_size)

        def is_healthy(self):
                return (self.beverage.is_diet and (self.pizza.calories<1000))
