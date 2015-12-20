# 6.00 Problem Set 5
# RSS Feed Filter
# Dora Jambor, dorajambor@gmail.com
# Collaboration (Discussion): Bobby, Ben
# Time: 5-7 hours
# December, 2014

'''
My solution to a CS50 problem set to retrieve news from Google and Yahoo through feedparsing.
'''

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5
#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def is_word_in(self, text):
        word = self.word.lower()
        text = text.lower() 

        import string
        for c in string.punctuation:
            if c in text:
                text = text.replace(c, ' ')

        separated_text = text.split(' ')

        for string in separated_text:
            if word == string:
                return True
        return False

# Look for word in title
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.get_title()
        return self.is_word_in(text)

# Look for word in subject
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.get_subject()
        return self.is_word_in(text)

# Look for word in summary
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        text = story.get_summary()
        return self.is_word_in(text)

# Composite Triggers

# Produce output by inverting the output of another trigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger
        
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

    
# If both triggers would fire on item
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

    
# Either one trigger or the other one would fire on item
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

# Phrase Trigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    
    def evaluate(self, story):
        title =  story.get_title()
        subject = story.get_subject()
        summary = story.get_summary()
        return self.phrase in title or self.phrase in subject or self.phrase in summary# TODO: PhraseTrigger


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    
    newstories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                newstories.append(story)
    stories = newstories
    return stories

#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []

    def do_every(num_seconds):
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)

        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)

        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)
        
        print "Sleeping..."
        p.root.after(num_seconds * 1000, do_every, num_seconds)
        
    do_every(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    main_thread(p)
    p.start()

