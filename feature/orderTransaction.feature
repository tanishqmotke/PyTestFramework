Feature: Order Transaction
        Test related to Order Transaction

@bddtest
Scenario Outline: Verify the Order Success message shown in details page
Given place the item order with <username> and <password>
And the user is on landing page
When I login to portal with <username> and <password>
And navigate to order page
Then select the orderId and order message is successfully displayeds
Examples:
    |username                 |password|
    |tanishqmotke110@gmail.com|Pass@123|
