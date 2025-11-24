# Restorantly
# Food Ordering System  ## Introduction  This application is a food ordering system which has two interfaces i.e. Employee and Customer. It can be used via the command line or REST API.

Both users can interact with the system through several options to perform an activity.

The Employee and Customer interface are modeled through classes and the options are mapped to the methods in these classes.

The options available to the Employee are add food category, add food details, add delivery person, assign delivery person to an order, update food order, view food details, view revenue and delete order.

The options available to the Customer are view menu, sign up and log in, create an order, checkout and view order details and status.

## Files

The food ordering system is split into several files i.e. main.py, models.py, core.py, constants.py and server.py.

### main.py

Main contains the controllor object which connects to the DB through bootstrapping. It also handles the user's options via the commande line through which they can perform their activities.

### models.py

Models contains the SQLiteBackend class which holds the engine, session and bootstrap. 

It also contains the Food Category, Food Details, Customer Details, Customer Order Selection, Customer Order Status and Delivery Person classes for the purpose of record keeping. 

It also has the Employee and Customer class that have methods to carry out the processes.

Models also has one function for the session which rollback (in case the commit fails) and close (when the process is complete).  

### core.py

Core contains the controller class which inherites from the SQLiteBackend class and composites from the Employee and Customer classes.

The controller class also includes all the methods from the Employee and Customer classes.

The purpose of the controller class is to mainly connect to the SQLiteBackend class and use the session as well as link the Employee and Customer classes to perform the functions.

### server.py

Server contains the controllor object which connects to the DB through bootstrapping. It is also responsible for creating and running the server.

The employee and customer routes are mapped to their respective functions and the functions call the methods from the Controller class.

The functions in server.py perform a GET, POST, PUT and DELETE requests over HTTP REST and returns results in JSON format.
