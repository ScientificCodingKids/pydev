#https://api.slack.com/methods/bots.info

from slackclient import SlackClient

def bot_fn_1():
    slack_token = ''
    sc = SlackClient(slack_token)

    sc.api_call('chat.postEphemeral', )