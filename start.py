import praw

# Optional: IF you want to use your own script, for whatever reason. Here's the steps.
# https://www.reddit.com/prefs/apps/
# 1. Create another app...
# 2. Name it
# 3. Select SCRIPT from dropdown
# 4. Redirect URL doesn't matter, but is required any address should work.
# 5. Copy the text under "personal use script", that's your client_id - replace the one in here with that.
# 6. Copy the text from "secret" - that's your client_secret, replace the one here with that.
# 7. Replace the user_agent part that says "redditHistoryDeleter" with your name, and your username.

client_id = 'OFQUawR0Xfxc-A'
client_secret = 'alLLwpPK4XTXh8cHIFgHxeCtDW0'
user_agent = '<console:redditHistoryDeleter:0.0.1 (by /u/WebDevLikeNoOther)>'

username = 'SomeUsername'  # REPLACE THIS WITH YOUR USERNAME
password = 'someOtherUsername'  # REPLACE THIS WITH YOUR PASSWORD

reddit = praw.Reddit(
    client_id=client_id, client_secret=client_secret, user_agent=user_agent,
    username=username, password=password)

# This is in UTC, so you have to use a converter to get the correct date.
# Use https://www.epochconverter.com/ to select the date you want to delete before.
# Example: delete_before_this_date = 1559694276
# Will delete all posts/comments that happened before
# Tuesday, June 4, 2019 8:24:36 PM
delete_before_this_date = 1528677401

def main():
    comments = reddit.redditor(username).comments.new(limit=None)
    submissions = reddit.redditor(username).submissions.new(limit=None)

    for comment in comments:
        if comment.created_utc < delete_before_this_date:
            reddit.comment(comment.id).delete()

    for sub in submissions:
        if sub.created_utc < delete_before_this_date:
            reddit.submission(sub.id).delete()

    print("Finished cleaning up your Reddit history!")


if __name__ == '__main__':
    main()

