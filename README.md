## E-WALLET PAYMENT SYSTEM

###  Introduction
Traditional brick-and-mortar banking offers customers a personal dimension. Customers visit the bank, converse with the financial advisors or representatives who can help them manage their accounts, and get answers to their queries. While this can be more reassuring to many customers, online banking has its own benefits that traditional banks cannot provide. These drawbacks are addressed and implemented via the employed E-Payment Systems. The Wallet E-Payment System is a standard electronic or online payment system that meets users' expectations for convenience in payment transactions from anywhere and at any time. Online payments are likely to be vulnerable to fraudulent activities and technical disturbances. It can be challenging to provide optimal infrastructure and services for processing these payments. The primary objective of deploying this system is to provide users and service providers with a safe and convenient platform to make payments online, ensuring financial security. This way, time and cost-effectiveness are also guaranteed, which in turn activates more users to utilize it. The collaboration with existing payment systems like service providers and bank applications (which serve as a source of funds) allows for a seamless experience for users.

### Implementation
Create a Wallet database to store User information and to track their transaction in a Wallet application system, ensuring user convenience without any mobility. Wallet Database is cosidered to be a payment network comprising of User information, user accounts, bank account information and transactions and statements. Each customer using the Wallet application is uniquely identified by their SSN. Each user with the Bank
account linked to the Wallet application is recognized by the BankID and Bank Account Number. The application supports two types of actions, i.e., Send Transaction and Request Money Transaction each of which are identified uniquely by their Send Transaction ID and Request Transaction ID respectively. To expand on the basis of how and through which data the transactions are being processed, is by using their Identifer
fields which can be either their phone number or email address. Extra information is stored in a additional information to ensure the alternative way to address actions if the primary information fails.

### Enhanced Entity Relationship Design
![image](https://github.com/user-attachments/assets/79f3adf8-6ec9-4357-a9fc-e1724a17d61a)

### Relational Schema (Logical Database Design)
![image](https://github.com/user-attachments/assets/e63458b0-feaa-44b6-b3ac-e762767e2ec9)

### Application Design: Functionalities
I used MYSQL to run the SQL commands that create, insert and populate the relations required to store data in the “Wallet” database. Connection to the database is practiced in VisualStudio Code using Python programming while depicting the application front view using the Tkinter framework displaying each functionality on a separate frame or window.
![image](https://github.com/user-attachments/assets/b3b2dbad-821d-42fb-860c-60935c69ee3f)

A Beginner Login - Registration Window is ensured to activate new customers to register using the Wallet Application and current customers to perform necessary actions through Login.
![image](https://github.com/user-attachments/assets/02ede90b-8fde-4f18-8615-41fdb57e3dff)

The Wallet User is enabled to the plethora of basic and related options as part of the Main Menu, where he or she can look into their profile (MyWallet Account), Actions to perform (SEND to and REQUEST from), (MyWallet Statements), Search Transactions. If the user has reached task completion, he or she can logout via Sign out option.
![image](https://github.com/user-attachments/assets/45184e92-b28c-4f57-987a-58753fb6a4ce)

MyWallet Account is expanded to various functionalities where the user can view and modify their account information, their mode of transaction via phone number or email address. Moreover, the user can add or remove bank accounts, keeping an account as primary or default.
![image](https://github.com/user-attachments/assets/7c2bf038-a9a8-46c8-9370-88102d17415d)

![image](https://github.com/user-attachments/assets/ea88b5e6-c80c-4005-a0d6-ccfc31dce2af)

![image](https://github.com/user-attachments/assets/c818a210-062e-40c2-b1c5-c00e2eae61ac)

![image](https://github.com/user-attachments/assets/48646dfc-afb0-440a-8d6b-4cacad579410)

![image](https://github.com/user-attachments/assets/b5d2778d-0b9e-4487-a347-c5c16ef4e798)

![image](https://github.com/user-attachments/assets/e2fd841b-5474-42b2-82c7-d2845ca4db1e)

Send to and Request From actions are enabled as options of Main Menu that allow the user to send amount to a user on a phone number or email_address linked to the account where the money can be transferred. If transferred, we enabled a special functionality that ensures the status of receiving money within 15 days. If the destination account user fails to accept the transaction, the transaction will be cancelled and the
amount will be credited back to the source account.
![image](https://github.com/user-attachments/assets/1f7d3a2a-ee6b-45c9-8659-8859f9be4099)

![image](https://github.com/user-attachments/assets/8990e300-1ff9-4a2a-9fbe-42f287fa7cbb)

Additionally, MyWallet Statement Window enables the user to look into various interesting functionalities that can display the total amount of money they sent or received in a range of dates or in a specific month with a basic numeric value. Also, the maximum amount transactions that go out or come in per month. Wallet Application can also show the maximum total amount of money sent or received referred to as the BEST
USERS from all our Wallet Users.
![image](https://github.com/user-attachments/assets/6ac11bc7-ce36-4d09-9040-c713875b1aa2)

![image](https://github.com/user-attachments/assets/97bf0547-9bfc-4cc8-8d71-0c13b7f07064)

![image](https://github.com/user-attachments/assets/766ef565-e63d-40ed-a480-9cf92e560cb5)

![image](https://github.com/user-attachments/assets/23cc129c-9ded-4243-8a82-039001fe38ad)











