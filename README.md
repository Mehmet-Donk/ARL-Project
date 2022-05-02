# What is ARL(Association Rule Learning)?

Association rule learning is a rule-based machine learning method for discovering interesting relations between variables in large databases. It is intended to identify strong rules discovered in databases using some measures of interestingness.An example of Association Rule Learning is usually given as a market basket application. This process analyzes the purchasing habits of customers by finding associations between products in their purchases.


# Business Problem

One of Turkey's largest online service platforms brings together service providers and service providers.
It provides easy access to services such as cleaning, modification and transportation with a few touches on your computer or smart phone. By using the data set containing the service users and the services and categories that these users have received.
It is desired to establish a product recommendation system with Association Rule Learning.

# Data Set Story

The data set consists of the services customers receive and the categories of these services.

It contains the date and time information of each service received.

 UserId: Customer number
 
 ServiceId: Anonymized services belonging to each category. (Example: Upholstery washing service under the cleaning category)
 
 A ServiceId can be found under different categories and refers to different services under different categories.
 
 (Example: Service with CategoryId 7 and ServiceId 4 is honeycomb cleaning, while service with CategoryId 2 and ServiceId 4 is furniture assembly)
 
 CategoryId: Anonymized categories. (Example: Cleaning, transportation, renovation category)
 
 CreateDate: The date the service was purchased
