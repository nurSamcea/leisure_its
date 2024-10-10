# Type of project / description
We have launched a new bus line within the Community of Madrid that connects various neighborhoods with a range of leisure destinations throughout the city. This service is designed to improve access to popular entertainment venues, parks, and cultural attractions, making it easier for both residents and visitors to experience all that Madrid has to offer. With convenient stops and frequent schedules, our bus line aims to provide a reliable and enjoyable transportation option for those looking to explore the city's vibrant social scene. 

-------- list of the places and in which zones of madrdi are the bus stops, also indicate de routes, order of stops that the bus will follow, for axmplw first in mostole sand then in leganes -----
------ picture of the map showing the places anf stops ------

---- frecuency of the buses, it depens of the places, stops and time of the day-----

# Assumptions of the system

---- zones we cover, and how many stops we have ---------

--- number of people we can transport in a day, 48 people is the capacity os the bus --- The average number of passengers per trip will be sufficient to justify the operation of each bus, as we believe it will effectively accommodate the demand from passengers interested in visiting various leisure destinations.

The buses will transmit information to the control center at regular intervals, specifically every 10 minutes. This scheduled communication will ensure that the control center maintains a constant flow of real-time data regarding the location and operational status of each bus in the fleet.

The traffic management system will be capable of identifying and predicting delays caused by traffic in real time. This functionality will enable the control center to make necessary adjustments to routes and schedules, ensuring that service remains efficient and reliable for all passengers. By proactively addressing potential delays, the system can enhance the overall travel experience and minimize disruption to the bus schedule. Additionally, the system will be equipped to modify routes in response to roadworks, public events or demonstrations, allowing for seamless adaptation to changing traffic conditions.

It is assumed that the 4G network coverage will be sufficient along the entire bus route to enable continuous communication between the bus and the control center, as we will be operating in areas within the Community of Madrid. This reliable coverage will ensure uninterrupted connectivity at all times, which is also essential for processing card payments and mobile transactions.

The system will be capable of handling adverse weather conditions and that specific protocols will be implemented to ensure the safety of passengers and drivers in these situations.

Each bus will undergo regularly scheduled preventive maintenance, thereby minimizing the risk of mechanical failures during operation.

# Stakeholders


# summary of requirements
## Functional Requirements
- Multi-Modal Transport Integration: The system must provide options for various transport modes (metro, buses, taxis,
  bike-sharing) to facilitate seamless transitions between them.
- Real-Time Information:Users must receive up-to-date information about transport schedules, availability, and delays
  via a mobile application and website.
- Real-Time Alerts:Send notifications to users about transport delays, route changes, or special promotions for leisure
  activities.
- Data Analytics and Reporting:Implement data analytics tools to track user behavior, popular routes, and leisure
  activity preferences for future planning.
- Interactive Maps:Provide interactive maps with transport routes, leisure attractions, and points of interest to help
  users navigate the city.
- Booking and Payment System:The platform should enable users to book and pay for transport services and entry tickets
  to leisure activities in a single transaction.
- User Profiles and Preferences:Users should be able to create profiles to save preferences, previous trips, and
  favorite leisure destinations
- Emergency Services Integration:Ensure that the system includes features for users to contact emergency services or
  report issues while using transport services.
- Necessary information for the user: bus station, frequency, schedule, stops, etc.

## Non-Functional Requirements
- Language Support:Offer multilingual support for the mobile application and website to cater to international
  visitors.
- Privacy and Data Protection:Ensure that user data is protected through secure data storage, encryption, and compliance
  with data protection regulations.
- Integration with Payment Gateways: Support multiple payment options, including credit cards, mobile wallets, and
  contactless payments, for booking transport services and leisure activities. Since we operate within the Community of Madrid, rather than in rural areas, we will ensure reliable 4G connectivity at all times to facilitate successful payment transactions. Furthermore, passengers will have the convenience of reserving tickets online for a specific time through our user-friendly app or website. This combination of flexible payment methods and online reservations is designed to enhance the overall travel experience for our customers, making it easier and more efficient to enjoy the vibrant leisure offerings in the city.

## Domain Requirements
- Compliance with Local Regulations: All transport services must comply with local transportation laws and safety
  regulations.
- Emergency Response Planning: Develop protocols for responding to emergencies, accidents, and natural disasters within
  the transport system to ensure user safety and service continuity.

## Quality Requirements
- Performance and Scalability:The system should handle high volumes of users, especially during peak tourist seasons,
  without performance degradation.
- Usability:The mobile application and website must have an intuitive user interface, ensuring easy navigation and quick
  access to services.
- Reliability:Transport services should maintain a high level of reliability with minimal downtime, especially during
  operational hours.
- Security:User data must be protected through robust security measures, including encryption for payment processing and
  personal information.
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

# Identification of some relevant quality attributes (Quality Requirements)
- Accessibility Features:Ensure that all transport modes and the booking platform are fully accessible to individuals
  with disabilities.
