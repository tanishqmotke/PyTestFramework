
from playwright.sync_api import Playwright

create_order_payload = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}
class APIUtils:
    
    def user_login(self,playwright:Playwright,credentials):
        baserequest = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com")
        response = baserequest.post("/api/ecom/auth/login",
                         data=credentials
                         )
        assert response.status == 200
        print(response.json)
        response_body = response.json()
        token = response_body["token"]
        print(token)
        return token
    
    def create_order(self,playwright,credentials):
        token = self.user_login(playwright,credentials)
        create_order = playwright.request.new_context(base_url="https://www.rahulshettyacademy.com")
        response = create_order.post("/api/ecom/order/create-order",
                          data=create_order_payload,
                          headers={"Authorization":token,
                                  "Content-Type":"application/json"})
        
        assert response.ok
        create_order = response.json()
        order_id = create_order["orders"][0]
        print(order_id)
        return order_id