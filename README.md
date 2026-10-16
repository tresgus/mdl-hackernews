# Exploring Hacker News Posts

An analysis of 20,100 posts from [Hacker News](https://news.ycombinator.com/), focusing on two post types:

- **Ask HN**: posts that ask the community a question
- **Show HN**: posts that show the community a project or something interesting

## Questions

1. Do `Ask HN` or `Show HN` posts receive more comments on average?
2. Do posts created at a certain time receive more comments on average?

## Key Findings

**Ask HN posts get more comments.** They average about 14 comments per post, compared with about 10 for Show HN posts.

| Post type | Posts | Avg. comments per post |
|-----------|------:|-----------------------:|
| Ask HN    | 1,744 | 14.04 |
| Show HN   | 1,162 | 10.32 |

**Posting time matters.** These are the top 5 hours (Eastern Time) for average comments on Ask HN posts:

| Hour  | Avg. comments per post |
|-------|-----------------------:|
| 15:00 | 38.59 |
| 02:00 | 23.81 |
| 20:00 | 21.52 |
| 16:00 | 16.80 |
| 21:00 | 16.01 |

Four of the five hours are in the afternoon or evening, which may line up with when people are free after work. The early-morning 2:00 entry may reflect readers in other time zones.

## Data

`Data/hacker_news.csv` is a sample of 20,100 posts drawn from the larger [Hacker News Posts dataset on Kaggle](https://www.kaggle.com/hacker-news/hacker-news-posts). Columns:

| Column | Description |
|--------|-------------|
| `id` | Post ID |
| `title` | Post title |
| `url` | Linked URL |
| `num_points` | Upvotes minus downvotes |
| `num_comments` | Number of comments |
| `author` | Username of the poster |
| `created_at` | Date and time the post was created (Eastern Time) |

## Project Structure

```
mdl-hackernews/
├── Data/
│   └── hacker_news.csv
├── mdl-hackernews.py   # the analysis, written as notebook cells
└── README.md
```

`mdl-hackernews.py` is a regular Python script that uses `# %%` cell markers, so it can be run cell by cell in VS Code or converted into a Jupyter notebook.

## Running the Project

Install the requirements:

```
pip install pandas ipykernel jupytext
```

Then use one of these options:

- **Run the whole script:** `python mdl-hackernews.py`
- **Run it cell by cell:** open the file in VS Code with the Python and Jupyter extensions installed, then click **Run Cell** above any `# %%`.
- **Convert it to a notebook:** `jupytext --to notebook mdl-hackernews.py` creates `mdl-hackernews.ipynb`.

## Tools

- Python 3
- pandas
- `datetime` (standard library)
