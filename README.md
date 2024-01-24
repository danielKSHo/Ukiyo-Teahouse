# Ukiyo Teahouse (Tested and Works in Python 3.10.1)
A japanese restaurant system built using python

## Terminal Commands (Installing Modules)
pip install tkcalendar (for getting booking date)

pip install pillow (for food images)

## Main Functions 

1. Login
2. Reset Account Password
3. Create Customer Account
4. Create Customer Booking
5. View Customer Invoices
6. Create Staff Account
7. Create Job Role
8. View Staff Account Details

### Login

There are 2 ways to bypass the login system:

Use a Staff Account Username and Password (in StaffAccount.txt)

#### Example
Username: Draken12

Password: NDS

##### OR

Use a Customer Account Username and Password (in CustomerAccount.txt)

#### Example:
Username: Olivia53

Password: DND

#

### Staff Account
When logged in using a Staff Account, the user can either:
- (6) Create a customer booking by clicking on the "Make a Booking" button,
- (5) View existing customer invoices by clicking on the "Customer Invoice History" button,
- (7) Create a job role by clicking on the "Job Roles" button,

##### OR

- (8) View Staff Details by clicking on the "Staff Account Details" button.

### Create Staff Account
(6) On the staff screen, there is a "Create Staff Account" button.
The user can enter staff details and login details to create a new staff account.
(1) The user can use the new staff account to login like how an existing staff account works.

### View Invoices
(5) This will then display all of the customer invoices denoted by B#
(Primary key for CustomerBooking.txt and CustomerDetails.txt).
Users can select a specific booking number and view it.
Other buttons in the Staff Account do not work currently.

#

### Customer Account
When logged in using a Customer Account, the user can either: 
- (4) Create a customer booking by clicking on the "Make a Booking" button
##### OR
- (5) View existing customer invoices by clicking on the "Customer Invoice History" button.

### Create Customer Booking
(4) Making a booking requires the user to fill in booking details and select food for the order.
Ordering uses a cart system.
The user has to select 1 of each type of food from the menu on the cart screen
(also located on the start screen for quick access).
Each food type is denoted by the following:
- A - Appetisers
- B - Mains
- C - Desserts
- D - Drinks
The quantity of each food type can be altered.
The booking is made when the order is submitted.

### View Invoices
(5) Viewing customer invoices in a customer account is similar to viewing in a staff account.
However, only the invoices that are made with the corresponding CustomerID 
as the customer account will be shown and allowed to be viewed.

#

### Reset Password
(2) On the login screen from the start screen, there is a "Reset Password" button.
This uses the backup key (last element/index[3] in CustomerAccount.txt)
to allow the user to overwrite the current customer password for the inputted customer username.

(1) The user can use the new password to login as normal but the old password will not work anymore.

#### Example:
Username: Pedro98
Backup Key: Mustache67

New Password: UEN
Confirm New Password: UEN

### Create Customer Account
(3) On the start screen, there is a "Create Customer Account" button.
The user can enter customer details and login details to create a new customer account.
(1) The user can use the new customer account to login like how an existing customer account works.

#

#### Note
Make sure the last lines in CustomerOrder.txt and CustomerBooking.txt have the same BookingID (primary key) in order to view the
customer invoices with the correct CustomerID (foreign key in CustomerBooking.txt).
Make sure all text files have a line space at the end of the file, ready for the next record to be added.
