
class Product:
    """creates objects to represent different attributes of products available at the store"""
    def __init__(self, product_id, title, description, price, quantity_available):
        """initializes all data"""
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """returns product id"""
        return self._product_id

    def get_title(self):
        """returns title"""
        return self._title

    def get_description(self):
        """returns description of product"""
        return self._description

    def get_price(self):
        """returns price of product"""
        return self._price

    def get_quantity_available(self):
        """returns availability of product"""
        return self._quantity_available

    def decrease_quantity(self):
        """decreases quantity of product when it is bought by customer"""
        self._quantity_available -= 1


class Customer:
    """creates objects that give customer name and account number. Also identifies if they are a premium member"""

    def __init__(self, name, customer_id, premium_member):
        """initializes customer data"""
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        self._cust_cart = []

    def get_name(self):
        """returns name of customer"""
        return self._name

    def get_customer_id(self):
        """returns customer ID"""
        return self._customer_id

    def get_cart(self):
        """returns customer cart"""
        return self._cust_cart

    def cart(self):
        """collection of all items customer has added to their cart"""
        self._cust_cart = []

    def is_premium_member(self):
        """returns whether customer is a premium member. boolean"""
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """takes product ID and adds to cart"""
        self._cust_cart.append(product_id)

    def empty_cart(self):
        """empties customer cart"""
        self._cust_cart.clear()


class InvalidCheckoutError(Exception):            # exception class
    pass


class Store:
    """represents a store with functions to add members,products. allows product search. adds products to members
    cart and allows checkout of items"""

    def __init__(self):
        """initializes store data"""
        self._store_members = []
        self._store_inventory = []
        self._list_members_ID = []

    def inventory(self):
        """collection of products that are part of the store"""
        self._store_inventory = []

    def add_product(self, product):
        """takes a product object and adds it to the inventory"""
        self._store_inventory.append(product)

    def get_inventory(self):
        return self._store_inventory

    def membership(self):
        """collection of customers that are members of store"""
        self._store_members = []

    def get_member_ID(self):
        "returns list of member ID #s"
        return self._list_members_ID

    def add_member(self, member):
        """takes customer object and adds it to membership"""
        self._store_members.append(member)

    def get_membership(self):
        """returns store members as objects"""
        return self._store_members

    def get_product_from_id(self, product_id):
        """takes a product ID and returns the product with the matching ID. returns none if no matching id found"""

        self._list_products = self.get_inventory()                        # creates a new list for inventory
        self._list_product_ID = []                                        # creates an empty list for just ID numbers
        count = (len(self._list_products))                                # sets up a counter for while loop
        x = 0                                                             # variable to use in while loop
        while x != count:                                                 # while loop until end of list
            self._list_product_ID.append(self._list_products[x].get_product_id())   # creates list of just ID numbers
            x += 1

        match = False                                       # variable for loop
        count = (len(self._list_product_ID)-1)              # creates new count for while loop
        while match is False:                               # check product ID to inventory until variable is false
            if product_id == self._list_product_ID[count]:  # checks ID # passed against story inventory list
                match = True                                # if match is found, changes variable to stop loop
                return self._list_products[count]           # returns product at same location in list as ID # was found

            elif product_id != self._list_product_ID[count]:   # if ID number does not match at location checked
                count -= 1                                     # then reduces count but continues loop
                if count == -1:                                # checks to see if count has reached the end of the list
                    match = True                               # changes variable to stop loop
                    return None                                # returns none if match not found

    def get_member_from_id(self, customer_ID):
        """takes customer ID. returns customer with matching id. no matching id = returns special value NONE"""

        self._list_members = self.get_membership()                          # creates a new list for membership list
        self._list_members_ID = []                                          # creates an empty list for customer IDs
        count = (len(self._list_members))                                   # sets up a counter for while loop
        x = 0                                                              # variable to use in while loop
        while x != count:                                                  # while loop until end of list
            self._list_members_ID.append(self._list_members[x].get_customer_id())  # creates list of just ID numbers
            x += 1

        match = False
        count = (len(self._list_members_ID) - 1)               # creates new count for while loop
        while match is False:                            # check customer ID to membership list until variable is false
            if customer_ID == self._list_members_ID[count]:  # checks ID # passed against membership list
                match = True                             # if match is found, changes variable to stop loop
                return self._list_members[count]               # returns customer id at location in list ID # found
            elif customer_ID != self._list_members_ID[count]:  # if ID # does not match at specific location checked
                count -= 1                                  # then reduces count but continues loop
                if count == -1:                             # checks to see if count has reached the end of the list
                    match = True                            # changes variable to stop loop
                    return None                             # returns none if match not found

    def product_search(self, search):
        """takes search string. returns list of ID codes for products in inventory whose title or description
        contains search string. if not found returns an empty list"""

        list_products = self.get_inventory()                         # creates a new list for inventory
        list_product_ID = []                                            # creates an empty list for just ID numbers
        count = (len(list_products) - 1)                                # sets up a counter for while loop
        while count != -1:                                              # starts while loop until end of product list
            list_product_ID.append(list_products[count].get_product_id())  # creates list of just ID numbers
            count -= 1                                                  # decreases count by 1 to eventually stop loop

        list_titles = []                                            # creates an empty list for just titles
        count = (len(list_products) - 1)                            # sets up a counter for while loop
        while count != -1:                                          # sets up while loop until end of product list
            list_titles.append(list_products[count].get_title())    # creates list of just titles
            count -= 1                                              # decreases count by 1 to eventually stop loop

        search_match_ID = []                                # new list to add IDs to match the search entered
        match = False                                       # variable for loop
        count = (len(list_titles) - 1)                      # creates new count for while loop
        while match is False:                               # check product ID to inventory until variable is false
            if search.lower() in list_titles[count].lower().split():        # checks ID # passed against inventory list
                search_match_ID.append(list_product_ID[count])  # returns product at same location in list as ID # found
                count -= 1
                if count == -1:
                    match = True
            else:
                count -= 1                                      # then reduces count but continues loop
                if count == -1:                                 # checks to see if count has reached the end of the list
                    match = True                                # changes variable to stop loop

        list_descriptions = []                                              # creates an empty list for just titles
        count = (len(list_products) - 1)                                    # sets up a counter for while loop
        while count != -1:                                                  # while loop until end of list
            list_descriptions.append(list_products[count].get_description())  # creates list of just titles
            count -= 1                                                      # decreases count by 1 to eventually stop loop

        match = False                                                       # variable for loop
        count = (len(list_descriptions) - 1)                                # creates new count for while loop
        while match is False:                                               # loop to check product ID to store inventory until variable is false
            if search.lower() in list_descriptions[count].lower().split():  # checkes ID # passed against store inventory list
                search_match_ID.append(list_product_ID[count])              # returns product at same location in list as ID # was found
                count -= 1
                if count == -1:
                    match = True
            else:                                           # if ID number does not match at specific location checked
                count -= 1                                  # then reduces count but continues loop
                if count == -1:                             # checks to see if count has reached the end of the list
                    match = True                            # changes variable to stop loop

        if search_match_ID == []:                           # return none if search comes back with nothing
            return None

        else:
            final_search_list = []                           # create a final search list without duplicates
            for id in search_match_ID:                       # iterate through all values in original search list
                if id not in final_search_list:         # if a value is not in final search list, then it is added
                    final_search_list.append(id)
        return final_search_list                             # returns final search list without duplicates

    def add_product_to_member_cart(self, product_id, customer_id):
        """add product to member's cart"""

        ID = self.get_product_from_id(product_id)           # gets product object from product id
        if ID is None:                                      # confirms that product is found
            return ("product ID not found")                 # returns statement if product not found

        member = self.get_member_from_id(customer_id)           # gets customer object from customer ID
        if member is None:                                      # confirms that member is found
            return ("member ID not found")                      # returns statement if member is not found

        if ID.get_quantity_available() == 0:                    # confirms that at least 1 of this item is in stock
            return ("product out of stock")

        member.add_product_to_cart(product_id)                  # adds product to customer cart
        return ("Product added to cart")                        # returns statement that product was added

    def check_out_member(self, customer_id):
        """checks member's cart out. confirms products are in stock and member exists. clears cart after checkout.
        returns price of cart"""

        member = self.get_member_from_id(customer_id)           # gets customer object from ID #
        if member is None:
            raise InvalidCheckoutError                                # raises exception if member not found

        premium = member.is_premium_member()                    # identifies if member is premium

        items_for_checkout = member.get_cart()                  # calls list of member's product ID's for checkout
        final_checkout = []                                     # new list of ID's for final checkout
        for items in items_for_checkout:                        # for ID #s in cart
            quantity = self.get_product_from_id(items).get_quantity_available()      # get quantity left for each item
            if quantity > 0:                                    # confirms that items are in stock
                final_checkout.append(items)                    # makes new list of all items that are in stock
                self.get_product_from_id(items).decrease_quantity()     # decreases quantity of items being bought

        prices = []                                              # new list for prices of items in cart
        for items in final_checkout:                             # for list to added prices of items to new price list
            prices.append(self.get_product_from_id(items).get_price())

        price = sum(prices)                                      # takes sum of all prices in price list

        if premium is True:                               # checks if customer is a premium member
            final_price = price                           # if customer is premium, returns price w/o shipping charge
            member.empty_cart()                           # empties customer cart after checkout
        else:
            final_price = (price + (price * .07))         # adds shipping charge if customer is not premium
        member.empty_cart()                               # empties customer cart after checkout
        return final_price                                # returns final price at checkout


def main():
    try:
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Customer("Yinsheng", "QWF", False)
        my_store = Store()
        my_store.add_product(p1)
        my_store.add_member(c1)
        my_store.add_product_to_member_cart("889", "QWF")
        my_store.check_out_member("QWF")
    except InvalidCheckoutError:
        print("Member number not found")


if __name__ == '__main__':
    main()
