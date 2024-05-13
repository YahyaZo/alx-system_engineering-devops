import requests

def number_of_subscribers(subreddit):
  """Queries the Reddit API for the number of subscribers of a subreddit.

  Args:
      subreddit: The name of the subreddit (without the 'r/').

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {"User-Agent": "MyCoolScript (by /u/your_username)"}  # Replace with your username

  try:
    response = requests.get(url, headers=headers, allow_redirects=False)
    response.raise_for_status()  # Raise exception for non-200 status codes
    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
  except requests.exceptions.RequestException:
    return 0  # Return 0 on any error

# Example usage (assuming 0-main.py is in the same directory)
if __name__ == "__main__":
  import sys

  if len(sys.argv) < 2:
    print("Please pass an argument for the subreddit to search.")
  else:
    print("{:d}".format(number_of_subscribers(sys.argv[1])))
