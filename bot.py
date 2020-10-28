import praw
import random
import datetime
import time

# WORKING
# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    bidens = ['Biden', 'Joe Biden', 'Joe', 'The Former VP']
    biden = random.choice(bidens)    

    acts = ['Settle for', 'Vote for', 'Elect', 'Choose']
    act = random.choice(acts)    

    jobs = ['President', 'President of the US', 'US President', 'President of the United States']
    job = random.choice(jobs)    

    dates = ['2020', 'November', 'the election', 'November 2020']
    date = random.choice(dates)    

    times = ['at this point', 'by now', 'come November', 'this election']
    time = random.choice(times)

    text = act + ' ' + biden + '. You just have to, ' + time + '. Vote for ' + biden+' for '+ job + ' in '+ date +'!'
    return text

def generate_comment_1():
    bidens = ['Biden', 'Joe Biden', 'Joe', 'The Former VP']
    biden = random.choice(bidens)    

    acts = ['leaving', 'fleeing', 'exiting', 'abandoning']
    act = random.choice(acts)    

    adverbs = ['necessarily', 'really', 'urgently', 'quickly']
    adverb = random.choice(adverbs)    

    dates = ['year', 'November', 'election', 'November 2020']
    date = random.choice(dates)    

    places = ['America', 'this country', 'the US', 'the United States']
    place = random.choice(places)

    text = "Elect " + biden + " or join me in " + act + ' ' + place + " this November. If Biden wins this " + date + ", you won't " + adverb + " need to flee in fear."
    return text

def generate_comment_2():
    bidens = ['Biden', 'Joe Biden', 'Joe', 'The Former VP']
    biden = random.choice(bidens)       

    trumps = ['Trump', 'Donald Trump', 'Donald', '45']
    trump = random.choice(trumps)    

    dates = ['year', 'November', 'election', 'November 2020']
    date = random.choice(dates)    

    places = ['America', 'this country', 'the US', 'the United States']
    place = random.choice(places)

    jobs = ['President', 'President of the US', 'US President', 'President of the United States']
    job = random.choice(jobs)  

    text = biden + ' should be elected ' + job + ' because ' + place + ' cannot survive another four years of ' + trump + '. Make sure you vote for Biden this ' + date + '.'
    return text

def generate_comment_3():
    pences = ['Pence', 'Mike Pence', 'His VP', 'His Vice President']
    pence = random.choice(pences)       

    trumps = ['Trump', 'Donald Trump', 'Donald', '45']
    trump = random.choice(trumps)    

    dates = ['year', 'November', 'election', 'November 2020']
    date = random.choice(dates)    

    jobs = ['President', 'President of the US', 'US President', 'President of the United States']
    job = random.choice(jobs)  

    acts = ['vote', 'vote for', 'elect', 'choose']
    act = random.choice(acts)  

    text = "Don't " + act + " " + trump + " for " + job + " this " + date + ". " + pence + " literally attracts flies."
    return text

def generate_comment_4():
    trumps = ['Trump', 'Donald Trump', 'Donald', '45']
    trump = random.choice(trumps)    

    dates = ['this year', 'in 2020', 'in the past 12 months', 'during the pandemic']
    date = random.choice(dates)    

    jobs = ['President', 'President of the US', 'US President', 'President of the United States']
    job = random.choice(jobs)  

    peoples = ['people', 'Americans', 'American people', 'persons']
    people = random.choice(peoples) 

    times = ['in 2016', 'last election', 'four years ago', 'against Hillary Clinton']
    time = random.choice(times) 

    text = trump + ' should not be reelected ' + job + ' because more ' + people + ' have filed for unemployment ' + date + ' than voted for him ' + time + '. As an aside, the electoral college is a failure.'
    return text

def generate_comment_5():
    trumps = ['Trump', 'Donald Trump', 'Donald', '45']
    trump = random.choice(trumps)    

    dates = ['this year', 'in 2020', 'in the past 12 months', 'during the pandemic']
    date = random.choice(dates)    

    covids = ['COVID-19', 'the Coronavirus', 'the pandemic', 'this virus']
    covid = random.choice(covids)  

    acts = ['Vote', 'Work to get', 'Elect', 'Choose to get']
    act = random.choice(acts)

    places = ['The White House', 'The Oval Office', 'The Presidency', 'Washington D.C.']
    place = random.choice(places)

    text = act + ' ' + trump + ' out of ' + place + ' ' + date + '. He cannot be president for another term after the way he handled ' + covid + '.'
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    comments = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5] 
    text = random.choice(comments)()
    return text

# comment these lines out for now
# for i in range(10):
#         print(generate_comment())

# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
# reddit_debate_url = 'https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/'
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
submission = reddit.submission(url=reddit_debate_url)

# print('Total comments =',len(submission.comments)) 

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

start_time = datetime.datetime.now()

# WORKING
# CHANGE TO WHILE BEFORE RUNNING FOR SUBMISSION
while True:
# or use a for loop
# if True: 
# for i in range(5): # have to run more than once for Task 5 to work

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

        # if start_time - datetime.datetime.now() is > or equal to 30:
        #     break
        #use datetime now to check if 30 minutes has passed

    # WORKING
    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=25) # set limit = None to get all level comments, set = 1 while debugging/writing
    # for limit None, goes through entire comment tree
    # for limit = 1, will go that level deep
    all_comments = []
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    
    all_comments = submission.comments.list()
    print('len(all_comments)=',len(all_comments))
    # print(type(all_comments))

    # WORKING
    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    my_comments = []
    for comment in all_comments:
        if comment.author == 'sophie-cs40':
            my_comments.append(comment)
        else:
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))
    print('len(my_comments)=',len(my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments)
    
        # post a top level comment
        # print(generate_comment())
        # submission.reply(generate_comment())

    # WORKING 
        # FIXME (task 2)
    if has_not_commented == len(all_comments):
        try:
            submission.reply(generate_comment())
        except praw.exceptions.RedditAPIException: 
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')
        # print(generate_comment())
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
 
    # WORKING
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over has_not_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        # replied works like a switch, go through each reply one by one 

    else:
        comments_without_replies = []
        for comment in not_my_comments:
            replied = True
            for comment.reply in not_my_comments: 
                if comment.author == 'sophie-cs40':
                     replied = True
                     break 
                if comment.author != 'sophie-cs40':
                    replied = False 
            if replied:
                continue
            else:
                comments_without_replies.append(comment)         
        
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))
        
    # WORKING
        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        try:
            try:
                # sorted_comments_without_replies = sorted(comments_without_replies key=comment.score) -- figure this part out
                comment = reddit.comment(id=random.choice(comments_without_replies))
                print('comment_id =', random.choice(comments_without_replies))
                comment.reply(generate_comment())
            except praw.exceptions.RedditAPIException:
                pass
        except praw.exceptions.RedditAPIException: #AssertionError
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')

        # print(generate_comment())
        # continue is for while or for loops -- would skip task 5 
        # pass does nothing, better to use when not sure
    
        # print(type(comments_without_replies))

        # use random.choice() with list 
        # also use submission.reply(generate_comment())

        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    # ALMOST WORKING - EXTRA CREDIT: UPVOTE COMMENT
    upvoted = False
    for comment in all_comments:
        if 'biden' in comment.body.lower() and upvoted == False:
            comment.upvote()
            upvoted = True
            # print('upvote comment')
    # can check if i've already upvoted and if so skip

    # ALMOST WORKING - EXTRA CREDIT: UPVOTE SUBMISSION
    upvoted = True
    downvoted = True
    # for submission in reddit.subreddit("csci040").top("month"):
    for submission in reddit.subreddit("csci040temp").top("month"):
        if 'biden' in submission.title.lower() and upvoted == True:
            submission.upvote()
            upvoted = False
        # elif 'trump' in submission.title.lower() and downvoted == True:
        #     submission.downvote()
        #     downvoted = False
            # print('upvote submission')

        # elif 'trump' in submission.title.lower():
        #     submission.downvote()

    # WORKING 
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions

    # random.random() returns random object float number between 0 and 1 

    # print(type(all_comments))
    
    result = random.random()
    all_submissions = []
    if result >= 0.5:
        print('original submission')
        # submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/?')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/')
        submission.reply(generate_comment())
    if result < 0.5:
        print('top subreddit submission')
        # print(type(all_submissions))
        # for submission in reddit.subreddit("csci040").top("month"):
        for submission in reddit.subreddit("csci040temp").top("day"):
            # print(submission.title)
            all_submissions.append(submission)
            # print(submission.title)
        # print(len(all_submissions))
        submission_choice = random.choice(all_submissions)
        submission = reddit.submission(id=submission_choice)
        print('submission_id =',submission_choice)
        print(submission_choice.title)
        # print(type(submission_choice))        
        # submission.reply(generate_comment())
        # print(generate_comment())
