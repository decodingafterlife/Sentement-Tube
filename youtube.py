from googleapiclient.discovery import build
import json
import pandas as pd
import re

class Youtube:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_youtube_api_service(self):
        """
        Builds a service object for interacting with the YouTube Data API.

        Returns:
        googleapiclient.discovery.Resource:
            A service object that allows interaction with the YouTube Data API.
        """
        youtube_api_service = build('youtube', 'v3', developerKey=self.api_key)
        return youtube_api_service



    def get_video_id(self, youtube_url):
        """
        Extracts the YouTube video ID from a given YouTube video URL.

        Args:
        - youtube_url (str): The URL of the YouTube video.

        Returns:
        str or None:
            If a valid video ID is found, returns the extracted video ID.
            If no video ID is found, returns None.
        """
        # Define the regular expression pattern to match the video ID
        pattern = re.compile(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})')

        # Use the pattern to find the video ID in the URL
        match = pattern.search(youtube_url)

        if match:
            video_id = match.group(1)
            return video_id
        else:
            return None



    def search_videos(self, api_service,keyword, max_results = 5):
        """
        Searches for videos on YouTube using the provided API service and a specified keyword.

        Args:
        - api_service (googleapiclient.discovery.Resource): The YouTube Data API service object created using the 'build' function.
        - keyword (str): The search keyword to look for in YouTube videos.
        - max_results (int, optional): The maximum number of video results to retrieve. Default is 10.

        Returns:
        - List[str]: A list of video IDs corresponding to the search results.
        """
        search_response = api_service.search().list(
            q = keyword,
            part = 'id',
            type = 'video',
            maxResults = max_results,
            eventType = 'completed'
        ).execute()

        video_ids = [item['id']['videoId'] for item in search_response['items']]
        return video_ids

    def get_video_details(self, api_service, video_id):
        """
        Retrieves details of a specific YouTube video using the provided API service and video ID.

        Args:
        - api_service (googleapiclient.discovery.Resource): The YouTube Data API service object created using the 'build' function.
        - video_id (str): The ID of the YouTube video for which details are to be retrieved.

        Returns:
        dict or None:
            If details are found, returns a dictionary containing the video's snippet information.
            If no details are found, returns None.
        """
        video_response = api_service.videos().list(
            part='snippet',
            id=video_id
        ).execute()

        if 'items' in video_response and video_response['items']:
            return video_response['items'][0]['snippet']
        else:
            return None

    def get_data(self,video_id, max_results=100):
        """
        Retrieves user comments and related information from a YouTube video using the YouTube Data API.

        Args:
        - video_id (str): The YouTube video ID for which comments are to be retrieved.
        - max_results (int, optional): The maximum number of comments to fetch. Default is 100.

        Returns:
        - pandas.DataFrame or Exception:
            If successful, returns a DataFrame containing comment details such as text, replies, user names, and dates.
            If an error occurs during the API request, returns None.
        """
        # Initialize the API request
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        request = youtube.commentThreads().list(
            part="snippet, replies",
            videoId=video_id,
            textFormat="plainText",
            maxResults=max_results
        )

        # Lists to store comments, replies, user names, and dates
        comments = []
        replies_list = []
        user_names = []
        dates = []

        # Fetching the comments
        while len(comments) < max_results and request:
            try:
                # Execute the API request
                response = request.execute()

                # Iterate through the response items
                for item in response['items']:
                    # Extract the comment details
                    comment_snippet = item['snippet']['topLevelComment']['snippet']
                    if (len(comment_snippet['textDisplay']) > 128):
                        continue
                    comments.append(comment_snippet['textDisplay'])
                    user_names.append(comment_snippet['authorDisplayName'])
                    dates.append(comment_snippet['publishedAt'])

                    # Extract replies if available
                    reply_count = item['snippet']['totalReplyCount']
                    if reply_count > 0:
                        replies = [reply['snippet']['textDisplay'] for reply in item['replies']['comments']]
                    else:
                        replies = []
                    replies_list.append(replies)

                    # Check if there are more pages of comments
                    request = youtube.commentThreads().list_next(request, response)

            except Exception as e:
                return None

        # Create a DataFrame for collected data
        df = pd.DataFrame({"Comment": comments, "Replies": replies_list, "User Name": user_names, "Date": dates})

        return df

    def save_data(self, df):
        """
        Saves a DataFrame containing YouTube video comments and related information to a CSV file.

        Args:
        - df (pandas.DataFrame): The DataFrame containing comment details such as text, replies, user names, and dates.

        Returns:
        None
        """
        # Save the DataFrame to a CSV file
        df.to_csv("comments.csv", index=False, encoding='utf-8')

    def get_comments(self, df):
        """
        Extracts and returns a list of comments from a DataFrame containing YouTube video comments.

        Args:
        - df (pandas.DataFrame): The DataFrame containing comment details such as text, replies, user names, and dates.

        Returns:
        List[str]: A list of comments extracted from the DataFrame.
        """
        comments = df["Comment"].tolist()
        return comments





        



    