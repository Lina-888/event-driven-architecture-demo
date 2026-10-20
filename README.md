# event-driven-architecture-demo
Event-Driven Architecture demonstration using Python and RabbitMQ
This is a simulation of a e-commerce application where an order service publishes events. The three consumers are Inventory Service, Payment Serive, and Notification Serivce. 
This system uses an broker topology and follows a pub/sub model. 



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


Key Concepts:
- Asynchronous communication: The producer publishes events without waiting for consumers to finish processing them 
- Loose coupling: The producer does not need to know which consumers recive the events 
- Pub/Sub: Multiple consumers may subscribe to the same event 
- Independent event processing: Each consumer process events independently 
- Broker topology: RabbitMQ distributes events without centrally controlling the workflow 