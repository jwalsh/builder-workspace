# CloudWatch Metrics, SLOs, SLIs, and SLAs for Code Librarian

## Key Metrics to Track

1. API Gateway
   - Latency
   - 4XX Error Rate
   - 5XX Error Rate
   - IntegrationLatency
   - CacheHitCount and CacheMissCount

2. Lambda Functions
   - Invocations
   - Errors
   - Duration
   - Throttles
   - ConcurrentExecutions

3. DynamoDB
   - ReadThrottleEvents
   - WriteThrottleEvents
   - ConsumedReadCapacityUnits
   - ConsumedWriteCapacityUnits

4. SNS
   - NumberOfMessagesPublished
   - NumberOfNotificationsFailed

5. SQS
   - NumberOfMessagesSent
   - NumberOfMessagesReceived
   - ApproximateAgeOfOldestMessage

6. OpenSearch
   - ClusterStatus.green
   - SearchableDocuments
   - FreeStorageSpace

7. Amazon Bedrock
   - Invocations
   - Latency
   - ThrottledRequests

## Service Level Indicators (SLIs)

SLIs are quantitative measures of the level of service provided. For the Code Librarian, we can define the following SLIs:

1. Availability: Percentage of successful requests (non-5XX responses)
2. Latency: 95th percentile of API response time
3. Error Rate: Percentage of 4XX and 5XX responses
4. Throughput: Number of requests processed per minute
5. Data Freshness: Time since the last successful data update

## Service Level Objectives (SLOs)

SLOs are target values for the SLIs. Here are example SLOs for the Code Librarian:

1. Availability: 99.9% of requests should be successful
2. Latency: 95% of requests should complete within 200ms
3. Error Rate: Less than 0.1% of requests should result in errors
4. Throughput: System should handle at least 1000 requests per minute
5. Data Freshness: Data should be no more than 5 minutes old

## Service Level Agreement (SLA)

The SLA is a formal agreement that includes consequences if the service doesn't meet the specified levels. For the Code Librarian, an example SLA could be:

"We guarantee 99.9% uptime for the Code Librarian service. If we fail to meet this uptime in a given month, we will provide service credits according to the following schedule:
- 99.0% to 99.9%: 10% credit
- 95.0% to 99.0%: 25% credit
- Less than 95.0%: 50% credit"

## CloudWatch Alarms

Based on the SLOs, you should set up CloudWatch Alarms for:

1. API Gateway 5XX error rate > 0.1% over 5 minutes
2. API Gateway Latency > 200ms at 95th percentile over 5 minutes
3. Lambda Error rate > 0.1% over 5 minutes
4. Lambda Duration > 1000ms at 95th percentile over 5 minutes
5. DynamoDB ReadThrottleEvents or WriteThrottleEvents > 0 over 5 minutes
6. SQS ApproximateAgeOfOldestMessage > 5 minutes
7. OpenSearch ClusterStatus != green for 5 minutes

## CloudWatch Dashboard

Create a CloudWatch Dashboard that includes:

1. API Gateway Latency and Error Rates
2. Lambda Invocations, Errors, and Duration
3. DynamoDB Read and Write Capacity Utilization
4. SNS/SQS Message Counts
5. OpenSearch Cluster Status and Free Storage Space
6. Amazon Bedrock Invocations and Latency

This dashboard will provide a quick overview of the system's health and performance.
