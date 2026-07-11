from src.predict import predict_sentiment

tweet = "Someone is following me near the bus stand."

result = predict_sentiment(tweet)

print("Tweet:", tweet)
print("Prediction:", result)