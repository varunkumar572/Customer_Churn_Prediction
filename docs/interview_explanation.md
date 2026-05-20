# Interview Explanation

## Direct Explanation

I built an end-to-end customer churn prediction pipeline for a telecom business. The system identifies customers who are likely to leave and recommends retention actions before churn happens.

## Detailed Explanation

The pipeline starts by ingesting customer profile, billing, usage, and support data. I designed the flow using a medallion-style architecture. Raw data lands in the bronze layer, cleaned and standardized records move to the silver layer, and churn-related features are created in the gold layer.

Important features include customer tenure, monthly charges, support call count, complaint count, payment delay days, usage drop percentage, contract type, and customer value score. These features help the model understand whether a customer is showing churn behavior.

The ML model is trained using historical churn labels where churned customers are marked as 1 and active customers are marked as 0. After training, the model scores each customer and generates a churn probability.

Finally, the retention engine converts the churn probability into a business action. For example, a high-risk loyal customer may receive a loyalty manager call and a discount, while a medium-risk customer may receive a personalized plan recommendation.

## Strong Interview Line

This project connects data engineering and machine learning by turning raw customer activity data into business-ready churn predictions and automated retention recommendations.
