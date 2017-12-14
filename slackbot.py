
import time
from slackclient import SlackClient
import os
from youtube import youtube_search
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_NAME = "C7YBL90F3"
webhook = "https://hooks.slack.com/services/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"


def main():
    #create bot
    sc = SlackClient(BOT_TOKEN)
    # Connect to slack using RTM websocket
    if sc.rtm_connect():
        print "Successfully connected"
        sc.rtm_send_message(CHANNEL_NAME, "Slacktubebot connecting!")
        while True:
            for slack_message in sc.rtm_read():
                message = slack_message.get("text")
                user = slack_message.get("user")
                if not message or not user:
                    continue
                message_list = message.split()
                if 'define' in message_list:
                    argument = message_list[1]
                    print argument
                elif 'video' and 'of' in message_list:
                    argument = message_list[2]
                    video = youtube_search(argument)
                    post_data = requests.post(webhook, json={'text': "https://www.youtube.com/watch?v=%s" % (video)})

            print sc.rtm_read()         
            time.sleep(0.5)

if __name__ == '__main__':
    main()