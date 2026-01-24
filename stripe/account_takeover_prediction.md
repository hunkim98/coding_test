Account Takeover Prediction System
The Task
You need to design a Machine Learning system to predict the risk of "Account Takeover" (ATO) for a payments platform.

ATO happens when hackers steal login details or use fake identities to break into real user accounts.

Important Things to Note
This problem is very open-ended. The interviewer wants to see how you think. Before you start building a solution, you must ask questions to understand the specific rules and requirements of the scenario.

What to Expect in the Interview
The interview will likely cover these specific topics in detail:

Designing the Model (~20 minutes)
Features: What data will you feed into the model? Think about both numbers and categories:
Account actions: Login time, location, type of device.
Transactions: How much money is moved and how often.
IP address: Details about the network connection.
Preprocessing: How will you prepare the data? This includes fixing missing values, making numbers standard, or turning text categories into numbers.
Model Choice: Which model works best here? How will you measure if it is working?
Risks: What could go wrong? Watch out for Class Imbalance (too few fraud cases), duplicate features, or Overfitting.
Building the System (~15 minutes)
Architecture: What are the main parts of your system?
A module to gather data.
A service to make predictions (either instantly or in batches).
Storage for data and tools for checking system health.
Speed: How do you make sure the system responds quickly, even when many people use it?
Latency: How do you handle delays in getting data?
Updates: How do you update the model while it is running live?
Monitoring: How do you track performance in the real world? You need to check both prediction accuracy and system speed.
Value to the Business (~15 minutes)
Impact: How do you prove the model is helpful? Look for a drop in hacked accounts and an increase in user trust.
False Positives: What are the risks if the model blocks a real user by mistake?
Improvements: How would you change the system later to bring even more value to the company?
Splitting Data for Training (Follow-up)
Class Imbalance: How do you handle training data where there are very few fraud cases compared to normal ones?
Sampling: What strategies will you use? (Examples: Oversampling, SMOTE, Stratified Sampling).
Helpful Links
These links explain how to stop fraud and secure accounts using ML:

Real-Time Fraud Detection ML System Design - Explains system structure, creating features, and real-time serving.
Detecting Account Takeovers with Machine Learning - Looks at user behavior and finding odd patterns.
AWS Fraud Detector - Account Takeover Insights - How AWS detects ATO attempts during login.
Note: These are just examples. In your interview, build a solution that fits the specific questions the interviewer asks.

Real Interview Notes
This question was reported in a Machine Learning Engineer interview at Stripe. It is known for being vague, so you must ask clarifying questions before you design.

Candidates noted that the serving portion (how the model runs in production) was very important. The interviewer also asked follow-up questions about how to split training data when the classes are not balanced. Candidates discussed techniques like Oversampling, SMOTE, and Stratified Sampling.