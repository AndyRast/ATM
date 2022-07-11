# ATM
Python Code for ATM
Option #1: Your Own UML Diagram

Final Project
For your final project, you are going to create a UML diagram of your choice (e.g., Sequence, Class, Activity, etc.) for an automated teller machine (ATM). Your diagram should include the following:
•	The customer must pass authentication before withdrawing money.
•	Authentication is performed by checking a PIN.
•	The PIN can be correct or not.
•	Unsuccessful attempts are counted.
•	If the counter exceeds a limit, then the customer is rejected.
•	If the account balance is zero, then the account is closed.
Annotate your state box in one of two ways. For internal state transitions, use the following state box:
 
If a state transitions to itself, use the following notation in the state box:
•	entry/Action
•	exit/Action.
A transition from one state to another is a link arrow connecting the two states and is labeled with event, guard, or action. The "event" is the action that causes a state to transition to another; e.g., "CheckPin." The "guard" is a possible outcome of an event; e.g., "correct PIN" or "incorrect PIN". The "action" is the result of the outcome of an event; e.g., if the guard is "incorrect PIN" then the "action" may be something like "increment error counter." Format your transition labels as follows:
•	Event [guard] / action

![ATM Diagram](https://user-images.githubusercontent.com/90261217/178313320-778f1c97-a58a-4677-9f54-35cf89a6f343.jpg)
