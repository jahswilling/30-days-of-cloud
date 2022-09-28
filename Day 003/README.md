![banner image](./img/heading.png)

Day 002
===

Third day I learned a lot about aws lambda, which allows you to add custom logic to AWS resources like Amazon S3 buckets and Amazon DynamoDB tables, allowing you to easily compute data as it enters or moves through the cloud. Lambda runs your code on a high-availability compute infrastructure and handles all compute resource administration, such as server and operating system maintenance, capacity provisioning and automatic scaling, and logging.

S3 storage a public cloud storage resource available in Amazon Web Services' (AWS) Simple Storage Service (S3), an object storage offering was something cover today. SQS, a fully managed message queuing service, came next, allowing you to decouple and scale microservices, distributed systems, and serverless applications. I then moved on to sns, a fully managed messaging service that supports both application-to-application (A2A) and application-to-person (A2P) communication.

At the end of the day i decided to work on a min serverless application since i had interacted with alot of service on that end. I a conant form that will send form dat through api gateway to lambda where it will be inserted into dynamodb and also sent out via SNS. so far i have created and hosted the static form on s3, created SNS topic and current was working on cloud front.


##Overview of the host S3 site:<br/>
![Network settings](./img/s3_buckects.png)
![Network settings](./img/website.png)

##Overview of the SNs topic:<br/>
![Network settings](./img/sns.png)


## Outstanding Challenges
Cloud front creation blocked by aws
![Network settings](./img/cloundfront.png)
