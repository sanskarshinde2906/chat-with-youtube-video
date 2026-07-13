from urllib.parse import urlparse, parse_qs


def extract_video_id(youtube_url: str) -> str:
    """
    Extracts the video ID from a YouTube URL.

    Args:
        youtube_url (str): Full YouTube URL.

    Returns:
        str: Video ID.
    """

    parsed_url = urlparse(youtube_url)

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    if parsed_url.hostname in (
        "www.youtube.com",
        "youtube.com",
        "m.youtube.com",
    ):
        query = parse_qs(parsed_url.query)

        if "v" in query:
            return query["v"][0]

    raise ValueError("Invalid YouTube URL")