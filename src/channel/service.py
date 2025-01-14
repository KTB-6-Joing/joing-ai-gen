from config import settings

from channel.schemas import ChannelEvaluationRequestDto, ChannelEvaluationResponseDto
from channel.methods.requests_methods import youtube_data_api_request, youtube_channel_request, playlist_request, image_request, channel_image_parsing, channel_subscribers_parsing
from channel.methods.preprocessing_methods import response_preprocessing, image_preprocessing
from channel.methods.evaluation_methods import text_evaluation, image_evaluation
from channel.prompts.evaluation_prompt import EvaluationPrompt


def channel_evaluation(request: ChannelEvaluationRequestDto) -> ChannelEvaluationResponseDto:
    # Getting Youtube Data API Object
    youtube_data_api = youtube_data_api_request(
        api_key=settings.YOUTUBE_DATA_API_KEY)

    # Getting Channel Info
    channel_response = youtube_channel_request(
        youtube_data_api=youtube_data_api,
        channel_id=request.channel_id)

    # Getting Playlist
    playlist_response = playlist_request(
        youtube_data_api=youtube_data_api,
        youtube_channel=channel_response)

    # Getting Channel Image
    channel_image = channel_image_parsing(
        channel_id=request.channel_id, 
        youtube_data_api=youtube_data_api)
    
    # Getting Channel Subscriber Counts
    subscribers_count = channel_subscribers_parsing(
        youtube_data_api=youtube_data_api,
        channel_id=request.channel_id)

    # Parsing response aka preprocessing
    videos_text_info, thumbnail_urls = response_preprocessing(
        playlist_response=playlist_response)

    evaluation_prompt = EvaluationPrompt

    # Image Evaluation
    # Image request & preprocessing
    image_response = image_request(thumbnail_urls)
    combined_image = image_preprocessing(image_response)

    image_evaluation_prompt = evaluation_prompt.image_evaluation_prompt.value
    try:
        image_evaluation_result = image_evaluation(
            combined_image, image_evaluation_prompt)
        if (not image_evaluation_result['appropriate'] and len(image_evaluation_result['reason']) != 0):
            return ChannelEvaluationResponseDto(
                evaluation_status=False,
                channel_image=None,
                subscribers=None,
                reason=image_evaluation_result['reason']
            )
    except Exception as e:
        print(e)

    # Text Evaluation
    text_evaluation_prompt = evaluation_prompt.text_evaluation_prompt.value
    text_evaluation_result = text_evaluation(
        description=videos_text_info, prompt=text_evaluation_prompt)
    return ChannelEvaluationResponseDto(
        evaluation_status=text_evaluation_result['appropriate'],
        channel_image=channel_image,
        subscribers=subscribers_count,
        reason=text_evaluation_result['reason']
    )
