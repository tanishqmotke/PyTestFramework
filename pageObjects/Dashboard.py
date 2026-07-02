from pageobjects.OrderHistory import OrderHistory


class Dashboard:
    
    def __init__(self,page):
        self.page = page
        self.navigate_to_Order = page.get_by_role("button",name="  ORDERS")
        
        
    def navigate_to_Orders(self):
        self.navigate_to_Order.click()
        order_History = OrderHistory(self.page)
        return order_History