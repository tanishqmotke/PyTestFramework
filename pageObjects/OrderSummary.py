from playwright.sync_api import expect

class OrderSummary:
    
    def __init__(self,page):
        self.page = page
    
    def validate_summary(self):
        expect(self.page.get_by_text("ORDER SUMMARY")).to_be_visible()
        