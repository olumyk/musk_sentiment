import tweepy
import json
import boto3
import time

def get_user_info(id):
    client = tweepy.Client(bearer_token)
    user = client.get_user(id=id, user_fields=['name','username','location','public_metrics'])
    return user

class TweetStreamListener(tweepy.StreamingClient):
    # on success
    def on_tweet(self, tweet):
        msg_lst = [str(tweet.id),
        str(get_user_info(tweet.author_id).data.name),
        str(get_user_info(tweet.author_id).data.username),
        str(tweet).replace('\n',' ').replace('\r',' '),
        str(get_user_info(tweet.author_id).data.public_metrics['followers_count']),
        str(get_user_info(tweet.author_id).data.location),
        str(tweet.created_at)]
        message = '\t'.join(msg_lst)
        print(message)
        firehose_client.put_record(
            DeliveryStreamName = delivery_stream_name,
            Record = {
                'Data': message
            })

    def on_error(self, status):
        print (status)


if __name__ == '__main__':
    # create kinesis client connection
    session = boto3.Session()
    firehose_client = session.client('firehose', region_name='us-east-1')

    # Set kinesis data stream name
    delivery_stream_name = 'test' # name given to aws kinesis firehose during creation

    # Set twitter credentials
   
    bearer_token = '<Your Own Bearer Token>'

    while True:
        try:
            print('Twitter streaming...')

            listener = TweetStreamListener(bearer_token)
            listener.add_rules(tweepy.StreamRule('Trump'))
            listener.filter(tweet_fields=['author_id','created_at'])
            
        except Exception as e:
            print(e)
            print('Disconnected...')
            time.sleep(5)
            continue
