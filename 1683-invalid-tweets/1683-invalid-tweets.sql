-- Write your PostgreSQL query statement below
SELECT tweet_id FROM Tweets where LENGTH(Tweets.content) > 15