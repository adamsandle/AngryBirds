import click
from .auth import login
from .stream import AngryBirdsStreamListener
from .words import load_words
from .analyse import analyse_tweets
import tweepy


@click.group()
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.pass_context
def listen(ctx):
    auth = login()
    api = tweepy.API(auth)
    streamListener = AngryBirdsStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)
    stream.filter(track=load_words())


@main.command()
@click.pass_context
def analyse(ctx):
    analyse_tweets()
