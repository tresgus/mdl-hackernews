# %% [markdown]
# # Exploring Hacker News Posts
# 
# ## Introduction
# Hacker News is a website where users submit stories which recieve votes and comments. Hacker News is used by a lot of people interested in technology, and posts can receive thousands of interactions. Two of the most popular posts start with `Ask HN` or `Show HN`. `Ask HN` posts ask the community a specific question. `Show HN` posts show the community a project or something similar that is interesting.
# This project is exploring the Hacker News posts. We will investigate the following questions:
# * Do `Ask HN` or `Show HN` receive more comments on average?
# * Do posts created at a certain time receive more comments on average?
# 
# This project will include data cleaning, data analysis, and data visualization. The data is a sampled dataset of 20,000 posts from a Hacker News dataset. The larger dataset is available on [Kaggle](https://www.kaggle.com/hacker-news/hacker-news-posts).
# %%
import pandas as pd

hn = pd.read_csv("Data/hacker_news.csv")
hn.head()

# %% [markdown]
# ## Data Cleaning
# ### Removing Headers from a List of Lists
# Since we have imported the pandas dataset, we don't need to directly remove the headers from the data. This is because pandas automatically reads the .csv file with the first row as the header.

# %% [markdown]
# ### Extracting `Ask HN` and `Show HN` Posts
# We will now extract the `Ask HN` and `Show HN` posts from the dataset. We will use the `str.startswith()` method to filter the posts that start with `Ask HN` and `Show HN`. We will also convert the titles to lowercase to ensure that we are not missing any posts due to case sensitivity.

# %% 
ask_posts = []
show_posts = []
other_posts = []

for index, row in hn.iterrows():
    title = row["title"].lower()
    if title.startswith("ask hn"):
        ask_posts.append(row)
    elif title.startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

# %% [markdown]
# ## Calculating the Average Number of Comments for `Ask HN` and `Show HN` Posts

# %%
total_ask_comments = 0
for post in ask_posts:
    row = int(post["num_comments"])
    total_ask_comments += row
avg_ask_comments = total_ask_comments / len(ask_posts)
print("Average comments for Ask HN posts:", avg_ask_comments)

total_show_comments = 0
for post in show_posts:
    row = int(post["num_comments"])
    total_show_comments += row
avg_show_comments = total_show_comments / len(show_posts)
print("Average comments for Show HN posts:", avg_show_comments)

# %% [markdown]
# Taking a look at the averages of `Show HN` and `Ask HN` posts, we can see more comment engagements for `Ask HN` than `Show HN`. `Ask HN` posts have an average 14 comments per post. In comparison, `Show HN` posts have 10 comments per post on average.
#
# Taking a step back, it is understandable why `Ask HN` posts have more comments. `Ask HN` posts are asking questions for a problem or hurdle they're experiencing. The Hacker News community is responding to that question. `Show HN` posts are showing something interesting, and the community is not as likely to comment on that post.
# %% [markdown]
# ## Finding the Amount of `Ask HN` Posts and Comments by Hour Created
# Now understanding `Ask HN` posts have more comments on average, we will now focus on that channel's engagement to gauge _when_ posting is likely going to attract more comments.
# To do this, we will follow the following steps:
# * Calculate the number of ask posts created in each hour of the day, along with the number of comments recieved.
# * Calculate the average number of comments ask posts receive by hour created.
# %%
import datetime as dt

# %% [markdown]
# ### Calculating the Number of Ask Posts and Comments by Hour Created

# %% 
result_list = []
for post in ask_posts:
    created_at = post["created_at"]
    num_comments = int(post["num_comments"])
    result_list.append([created_at, num_comments])

counts_by_hour = {}
comments_by_hour = {}

for item in result_list:
    time =dt.datetime.strptime(item[0], "%m/%d/%Y %H:%M")
    hour = time.strftime("%H")
    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = item[1]
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += item[1]

print(counts_by_hour)
print(comments_by_hour)
# %% [markdown]
# ### Calculating the Average Number of Comments for `Ask HN` Posts by Hour

# %% 
avg_by_hour = []
for hour in comments_by_hour:
    comments = comments_by_hour[hour]
    posts = counts_by_hour[hour]
    avg_by_hour.append([hour, comments/posts])

print(avg_by_hour)
# %%
swap_avg_by_hour = []
for avg in avg_by_hour:
    first_element = avg[1]
    second_element = avg[0]
    swap_avg_by_hour.append([first_element, second_element])

print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse = True)
print("Top 5 Hours for Ask Posts Comments")
for avg in sorted_swap[0:5]:
    hour = dt.datetime.strptime(avg[1], "%H")
    hour = hour.strftime("%H:%M")
    print(f"{hour}: {avg[0]:.2f} average comments per post")

# %% [markdown]
# Above we can look at the top 5 hours with the highest average comment rate. We can see the top 5 hours most likely to recieve comments are 3 p.m. with 38.59, 2 a.m. with 23.81, 8 p.m. with 21.52, 4 p.m. with 16.8, and 9 p.m. with 16.01 average comments per post.
# 
# All of these times are in EST. An interesting theme with these posts is that more of them take place in the afternoon, with 4 out of the top 5 entries taking place after noon, and only one is in the morning. This might correspond with user availability in the afternoon after their 9-5 job and work break. More specifically, the morning entry is in the early morning. This might be because more people abroad, like in India, are responding to posts. It could also be because a lot of people can see the post in the middle of the day when they check Hacker News.

# %% [markdown]
# ## Conclusion
# After our data cleaning and analysis, we have found the answers to our initial questions. We found out `Ask HN` posts have more comments than `Show HN`, having an average of 14.04 comments per post to 10.32 average comments per post. We also found out when users are more likely to get responses to their questions, showing that afternoon posts receive the most community attention.
# %%
