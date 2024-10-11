# Type of project / description

We have launched a new bus line within the Community of Madrid that connects various neighborhoods with a range of leisure destinations across the city. This service is designed to improve access to popular entertainment venues, parks, and cultural attractions, making it easier for both residents and visitors to experience all that Madrid has to offer. With convenient stops and frequent schedules, our bus line aims to provide a reliable and enjoyable transportation option for those looking to explore the city's vibrant social scene. Passengers will have access to real-time information about bus schedules and routes through multiple channels, including bus stop displays, our website, and the mobile app.

-------- list of the places and in which zones of madrdi are the bus stops, also indicate de routes, order of stops that the bus will follow, for axmplw first in mostole sand then in leganes -----
------ picture of the map showing the places anf stops ------

---- frecuency of the buses, it depens of the places, stops and time of the day-----

# Assumptions of the system

---- zones we cover, and how many stops we have ---------

--- number of people we can transport in a day, 48 people is the capacity os the bus --- The average number of passengers per trip will be sufficient to justify the operation of each bus, as we believe it will effectively accommodate the demand from passengers interested in visiting various leisure destinations.

- Tickets can be purchased online or directly on the bus. This means that ticket reservations can only be made online, as we do not have a bus station where tickets can be bought.

- The buses will transmit information to the control center at regular intervals. This scheduled communication will ensure that the control center maintains a constant flow of real-time data regarding the location and operational status of each bus in the fleet.

- The traffic management system will be capable of identifying and predicting delays caused by traffic in real time. This functionality will enable the control center to make necessary adjustments to routes and schedules, ensuring that service remains efficient and reliable for all passengers. By proactively addressing potential delays, the system can enhance the overall travel experience and minimize disruption to the bus schedule. Additionally, the system will be equipped to modify routes in response to roadworks, public events or demonstrations, allowing for seamless adaptation to changing traffic conditions.

- It is assumed that the 4G network coverage will be sufficient along the entire bus route to enable continuous communication between the bus and the control center, as we will be operating in areas within the Community of Madrid. This reliable coverage will ensure uninterrupted connectivity at all times, which is also essential for processing card payments and mobile transactions.

- The system will be capable of handling adverse weather conditions and that specific protocols will be implemented to ensure the safety of passengers and drivers in these situations.

- Each bus will undergo regularly scheduled preventive maintenance, thereby minimizing the risk of mechanical failures during operation.

# Stakeholders
- End-users (passengers)
- Local government and public transport authorities in Madrid.
- Control Center: responsible for continuously monitoring the bus fleet, making real-time adjustments to schedules, and responding swiftly to any incidents or delay
- Developers: responsible for designing and maintaining the ticketing system, reservation platform (both the mobile app and website), and real-time bus tracking features. They also handle the integration of the onboard communication system with the control center, ensuring seamless GPS tracking, 4G payments, and real-time updates.
- Bus drivers
- GPS, telecommunications, and radio communication providers: responsible for ensuring location tracking, 4G coverage, and secure radio communication between the bus drivers and the control center.
- Payment processing companies ensuring seamless transactions on the bus and online.
- Bus Maintenance and Cleaning Company.
- Leisure Destinations: offering joint promotions or discounts to passengers.

# Summary of requirements
## Functional Requirements
- **FUN-LOC-001** (Geolocation of buses): The system shall continuously monitor and track the real-time location of each bus, displaying this information on the control center dashboard and through online features accessible to passengers.
- **FUN-STATUS-002** (Bus status and faults): The onboard system shall monitor and report the operational status of the bus, including detecting and transmitting faults to the control center for maintenance requests.
- **FUN-DB-003** (Local bus database): Each bus shall maintain a local database to store events such as breakdowns, passenger counts per trip, significant delays and passenger complaints.
- **FUN-OCCUP-004** (Occupancy level): The onboard system shall monitor and report the number of available seats in real-time, updating both the control center and the digital passenger services.
- **FUN-COMM-005** (Driver communication): The system shall allow for two-way communication between the bus driver and the control center.
- **FUN-PANL-006** (Passenger information panel): the onboard passenger information panel shall display real-time updates about the bus route, including upcoming stops, arrival times, delays and route deviations due to events, construction work, traffic...
- **FUN-PANL-007** (Passenger information at bus stops): the information panels at bus stops shall display the estimated wait time for the next bus, the number of available seats and any route deviations.
- **FUN-ONL-008** (Online Passenger Information): The system shall offer passengers real-time updates regarding bus schedules, current locations, and estimated arrival times. Additionally, it shall feature an interactive map displaying all bus stop locations, along with comprehensive details about the destinations served by each stop and the ticket prices for every route
- **FUN-TICK-009** (Onlien Ticket Reservation): The system shall enable passengers to make ticket reservations online, ensuring that all data is synchronized with the central server.
- **FUN-PAY-010** (Payment): Users must have the option to purchase their tickets either directly on the bus or online.
- **FUN-HIST-011** (Historical data): the bus shall periodically send historical data (such as route timings, incidents, and delays) to the control center for performance analysis.
- **FUN-USER-012** (User Profiles and Subscription): The system shall provide an online subscription feature that allows users to create profiles to save their preferences, previous trips, and favorite leisure destinations
- **FUN-ALERT-013** (Real-Time Alerts): The system shall send notifications exclusively to subscribed users regarding transport delays, route changes or special promotions for leisure activities.

## Non-Functional Requirements
- **NFUNC-PAY-014** (Secure Online Payments): Online payments made via card will be processed securely and without additional costs, provided that the cards are compatible with the Spanish payment system. Passengers will have the option to pay in cash or by card, including contactless payments, while on the bus.
- **NFUNC-INFO-015** (Passenger Information Access): Passengers will have access to online information through both a dedicated mobile app and the official website, ensuring they have the latest updates and details at their fingertips.
- **NFUNC-SUBS-016** (Subscription Notifications): Subscriptions will be managed via email, where users will receive all relevant notifications and confirmations regarding their service preferences.
- **NFUNC-BILAN-017** (Bilingual Support): Both the mobile app and the website will be available in two languages, offering content in Spanish and English to accommodate a diverse user base.
- **NFUNC-COMM-018** (Driver-Control Center Communication): Communication between the bus driver and the control center regarding the start and end of routes, as well as any incidents, will primarily take place via radio. If there are any issues with radio communication, alternative messages can be sent to ensure effective communication
- **NFUNC-DATA-019** (Real-Time Data Transmission): The onboard system of the bus will periodically and automatically send the information collected during the journey every five minutes via a 4G connection. This information will include data on the bus's location, the number of passengers and the mechanical status. Similarly, the control center will be able to send commands or modifications to the bus using the same communication channel, ensuring continuous and effective interaction between both systems.

## Operation domain Requirements
- Compliance with Local Regulations: All transport services must comply with local transportation laws and safety
  regulations.
- Emergency Response Planning: Develop protocols for responding to emergencies, accidents, and natural disasters within
  the transport system to ensure user safety and service continuity.

## Quality requirements
- la aplia ion esra diseñan de forma sencilla e intuitiva para que todo el muendo puedo usarla sin problemas

# Analyze the impact of quality attributes
- Accessibility Features:Ensure that all transport modes and the booking platform are fully accessible to individuals
  with disabilities.
- Performance and Scalability:The system should handle high volumes of users, especially during peak tourist seasons,
  without performance degradation.
- Usability:The mobile application and website must have an intuitive user interface, ensuring easy navigation and quick
  access to services.
- Reliability:Transport services should maintain a high level of reliability with minimal downtime, especially during
  operational hours.
- Security:User data must be protected through robust security measures, including encryption for payment processing and
  personal information. proteccion de datos en las subcricione sy canales de comuniaion segueros entre el centro de control y el autobus
- Maintainability: The system should be designed for easy updates and maintenance to incorporate user feedback and new
  features.
- Data Accuracy: Ensure that all information related to transport schedules, availability, and leisure activities is
  accurate and updated regularly.
- Compliance: The system must comply with data protection laws, privacy regulations, and accessibility standards to
  ensure user trust and legal compliance. Implement privacy features such as data anonymization, consent management, and
  user control over personal information to protect user privacy and comply with data protection regulations.
- Performance Optimization: Optimize system performance through caching, load balancing, and other techniques to ensure
  fast response times and efficient resource utilization.
- Accessibility Compliance: Ensure that the system meets accessibility standards such as WCAG to provide equal access to
  users with disabilities.
- Security Compliance: Implement security best practices such as encryption, authentication, and authorization to
  protect user data and prevent unauthorized access.
- Sensor Integration: Integrate with sensors and IoT devices to collect real-time data on traffic conditions, weather
  patterns, and user behavior to optimize transport services and improve user experience.

# Use case diagram

# Class diagram
Identification of classes, relationship between them and multiplicity
