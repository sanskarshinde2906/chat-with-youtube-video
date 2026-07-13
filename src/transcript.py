from youtube_transcript_api import YouTubeTranscriptApi



def get_available_languages(video_id: str) -> list[str]:
    """
    Return all available language codes.
    """

    api = YouTubeTranscriptApi()

    transcript_list = api.list(video_id)

    languages = []

    for transcript in transcript_list:

        languages.append(transcript.language_code)

    return languages


def get_transcript(video_id: str) -> str:
    """
    Fetch transcript using the first available language.
    """

    try:

        api = YouTubeTranscriptApi()

        languages = get_available_languages(video_id)

        transcript = api.fetch(
            video_id,
            languages=[languages[0]]
        )

        transcript_text = " ".join(
            snippet.text
            for snippet in transcript.snippets
        )

        return transcript_text

    except Exception as e:

        raise Exception(f"Transcript not available : {e}")


