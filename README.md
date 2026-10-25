# event-driven-architecture-demo
Event-Driven Architecture demonstration using Python and RabbitMQ
This is a simulation of a e-commerce application where an order service publishes events. The three consumers are Inventory Service, Payment Serive, and Notification Serivce. 
This system uses an broker topology and follows a pub/sub model. 

Technologies used:
- Python: Implements the event producer and consumers
- RabbitMQ: Acts as the event broker and distributes the events
- Pika: Python libary used to communicate with RabbitMQ
- Docker Compose: Starts and manages the RabbitMQ container
- GitHub Codespaces: The cloud-based development envirronment used to run the demonstration

Architecture:
- Event Producer: Publishes events such as OrderPlaced, OrderCanceled, OrderShipped 
- Event Broker (RabbitMQ): Recives published events and distributes them to subscribed services 
- Inventory Service: Simulates the inventory updates 
- Payment Service: Simulates payment processing 
- Notification Service: Simulates sending notifications 

Files:
- docker-compose.yml: Starts RabbitMQ using Docker 
- rabbitmq.py: Establishes connection with RabbitMQ and configures the exchange 
- producer.py: Publishes events to RabbitMQ
- inventory_service.py: Recives OrderPlaced and OrderCancelled events and simulates inventory updates 
- payment_services.py: Recives ORderPlaced events and simulates payment processing 
- notification_services.py: Recives OrderPlaced and OrderShipped events and simulates sending notifications 
- requirements.txt: Lists the python dependecy required to communicate with RabbitMQ 


Installation and Setup:
The project can be executed using GitHub Codespaces 

1. Open the project: Open the GitHub repository and launch the existing Codespace or create a new Codespace
2. Start RabbitMQ: Open a terminal and run: docker compose up -d 
3. Install Python Dependencies: python -m pip install -r requirements.txt
4. Start the Event Consumers: Open three seperate terminals. 
    Terminal 1 - Inventory Service: python inverntory_service.py 
    Terminal 2 - Payment Service: python payment_service.py
    Terminal 3 - Notification Service: python notification_service.py 
Keep all three terminals running to listen for messages/events 
5. Publis Events: Open a fourt terminal for the Event Producer. 
    Example 1 - Place an Order: python producer.py OrderPlaced 08
    Expected results: 
                     Inventory Service: simulates updating the stock 
                     Payment Service: simulates processing the payment 
                     Notification Service: simulates sending an order conformation 
    Example 2 - Cancel an order: python producer.py OrderCancelled 08 
    Expected results: 
                     Only the Inventory Service recives it and simulates restoring stock 
    Example 3 - Create a new Order and Ship an Order: python producer.py OrderPlaced 11 
    and then python producer.py OrderShipped 11 
    Expected results: 
                     Only the Notification Service recives it and simulates sending a shipping notification 

Event Subscribtions:
- Inventory Service: OrderPlaced, OrderCancelled 
- Payment Service: OrderPlaced
- Notification Service: OrderPlaced, OrderShipped 


Key Concepts:
- Asynchronous communication: The producer publishes events without waiting for consumers to finish processing them 
- Loose coupling: The producer does not need to know which consumers recive the events 
- Pub/Sub: Multiple consumers may subscribe to the same event 
- Independent event processing: Each consumer process events independently 
- Broker topology: RabbitMQ distributes events without centrally controlling the workflow 

Note: This is an simulation. Inventory updates, payment processing and notifications are demonstrated thorugh termial output rather than real database operations, payment transactions or emails. 