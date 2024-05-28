import tweepy
import time
import boto3

class TweetStreamListener(tweepy.StreamingClient):
#     def __init__(self, bearer_token, wait_on_rate_limit = True):
#         tweepy.StreamingClient.__init__(self, bearer_token = bearer_token,
#                                         wait_on_rate_limit = True)
    
    def on_response(self, response):
        include = response.includes
        tweet = response.data
        msg_lst = [
            str(tweet.id),
            str(include["users"][0].name),
            str(include["users"][0].username),
            str(tweet).replace("\n", " ").replace("\r", " "),
            str(include["users"][0].public_metrics["followers_count"]),
            str(include["users"][0].location),
            str(tweet.created_at),
            "\n"
        ]
        message = "\t".join(msg_lst)
        print(message)
        firehose_client.put_record(DeliveryStreamName=delivery_stream_name,
                                   Record = {'Data':message})
    def on_error(self, errors):
        print(f"Error: {errors}")
    

if __name__ == '__main__':
    session = boto3.Session()
    firehose_client = session.client('firehose', region_name = 'us-east-1')
    
    delivery_stream_name = 'test'
    
    bearer_token = ''
    
    while True:
        try:
            print("Twitter Streaming")
            
            listener = TweetStreamListener(bearer_token, wait_on_rate_limit = True)
            
            previous_rules = listener.get_rules().data
            if previous_rules:
                listener.delete_rules(previous_rules)
                
            rule = 'Trump lang:en'
            tag = 'Trump, English'
            listener.add_rules(tweepy.StreamRule(rule, tag = tag))
            
            expansions = ['author_id']
            user_fields = ["name", "username", "location", "public_metrics"]
            tweet_fields = ["id", 'author_id', "created_at"]
            
            listener.filter(expansions = expansions,
                            user_fields = user_fields, 
                            tweet_fields = tweet_fields)
            
        except Exception as e:
            print(e)
            listener.disconnect()
            print('Disconnected...')
            time.sleep(5)
            continue
            