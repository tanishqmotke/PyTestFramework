from pageobjects.OrderSummary import OrderSummary
class OrderHistory:
    
    def __init__(self,page):
        self.page = page
    
    def click_on_OrderId_view_button(self,order_id):
        order_id_position = self.page.locator("tr").filter(has_text=order_id)
        order_id_position.locator("td").get_by_role("button",name="View").click()
        orderSummary = OrderSummary(self.page)
        return orderSummary