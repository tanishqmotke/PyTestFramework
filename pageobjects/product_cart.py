
class ProductCart:
    
    def __init__(self,page):
        self.page = page;
        self.products = ["Nokia Edge","Blackberry"]
        self.checkout_button = page.locator("a.nav-link.btn.btn-primary").filter(has_text="Checkout")

    def add_product_to_cart(self,product):
                product_name = self.page.locator("app-card").filter(has_text=product)
                product_name.get_by_role("button",name="Add").click()
    
    def checkout(self):
        return self.checkout_button
            