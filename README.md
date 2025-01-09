# JOING AI: Evaluation & Generation

JOING 플랫폼에서 사용되는 AI 기능은 추천 시스템, 기획안 평가 및 요약, 크리에이터 프로필 평가로 크게 3가지로 나뉜다.
해당 README는 그 중에서도 기획안 평가 및 요약과 크리에이터 평가 기능에 대한 설명을 담고 있다.

<br>

## Contributor

<div align="center">

| ![Wooyong Jeong](https://github.com/jwywoo.png?size=300)|
|:-------------------------:|
| [jwywoo26@egmail.com](mailto:jwywoo26@mail.com) |
| [GitHub](https://github.com/jwywoo) |
| **Wooyong Jeong: Woo**             |
| AI AI Generation            |

</div>

<br>

## Goal

### 공통 목표

- 플랫폼 내의 핵심 기능이 아닌 보조 기능으로써 서비스 내에서의 사용자 활동을 보조하는 기능으로써의 역할을 최우선한다.
- Computing Resource를 최대한 적게 사용하며 동시에 AI 기능들의 남용을 방지는 보조 장치를 구성한다.
- 하지만 성능이 부족하지 아니하며 빠른 처리가 가능하도록 구성한다.

<br>

### 기획안 평가 및 요약

- 상기 목표를 달성하기 위해 기획안을 평가 함에 있어 총 3단계로 나누어 진행한다. 선행 단계의 평가를 통과하지 못한다면 아래의 다음 단계로 넘어가지지 않는다.
  - 1단계: 정량평가 - 보다 정확한 평가와 AI 남용 방지를 위해 주어진 기획안의 일정 토큰수를 기준보다 토큰의 수가 적을 경우 반려한다.
  - 2단계: 내용평가 - 기획안의 논리적인 구조에 대한 평가를 진행한다. 제목과 내용의 상관 관계를 평가하고 논리적으로 연결 되어 있지 않은 경우 반려한다.
  - 3단계: 유해성평가 - 1,2 단계를 통과한 기획안의 내용이 대한민국 방송통신심의위원회 규정에 적합하지 않을시 반려한다.
- 3단계의 기획안 평가를 통과한 기획안의 경우 기획안에서의 키워드를 중심으로 요약을 진행한다.

<br>

### 프로필 평가

- 프로필 평가는 Youtube 채널의 정보를 기반으로 사용하며 채널 정보 요청단계와 정보 검증 단계로 나누어 구성한다.
- 평가과정을 세분화아여 평가의 정확성과 AI 사용 남용을 방지하도록 구성한다.
- 평가에 있어 이미지 데이터와 텍스트 데이터 동시에 활용하여 평가의 정확성을 높인다.

<br>

## Tech Stack

<div>
  <img alt="PYTHON" src="https://img.shields.io/badge/python-3776AB.svg?&style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white" alt="GIT">
  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Google%20colab-F9AB00?style=for-the-badge&logo=Google%20colab&logoColor=white" alt="Google Colab">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitKraken-179287?style=for-the-badge&logo=GitKraken&logoColor=white" alt="GitKraken">
  <img src="https://img.shields.io/badge/Amazon%20EC2-FF9900?style=for-the-badge&logo=Amazon%20EC2&logoColor=white" alt="Amazon EC2">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" alt="Figma">
  <img alt="ChatGPT" src="https://img.shields.io/badge/openai-412991.svg?&style=for-the-badge&logo=openai&logoColor=white"/>
  <img alt="FASTAPI" src="https://img.shields.io/badge/fastapi-009688.svg?&style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube">
  <img alt="Tiktoken" src="https://img.shields.io/badge/Tiktoken-4A90E2.svg?&style=for-the-badge"/>
  <img alt="Pillow" src="https://img.shields.io/badge/Pillow-50E3C2.svg?&style=for-the-badge"/>
  <img alt="HUGGINGFACE" src="https://img.shields.io/badge/huggingface-FFD21E.svg?&style=for-the-badge&logo=huggingface&logoColor=white"/>
  <img alt="LANGCHAIN" src="https://img.shields.io/badge/langchain-1C3C3C.svg?&style=for-the-badge&logo=langchain&logoColor=white"/>
  <img alt="N8N" src="https://img.shields.io/badge/n8n-EA4B71.svg?&style=for-the-badge&logo=n8n&logoColor=white"/>
</div>

<br>

## Service Architecture: Proposal & Channel

![JOING GEN AI Service Architecture](/static/Joing-AI-SA.png)

<br>

## Service Structure

```shell
JOING-GENAI-SERVER/
├── src/
│   ├── channel/
│   │   ├── methods/
│   │   │   ├── evaluation_methods.py
│   │   │   ├── preprocessing_methods.py
│   │   │   └── requests_methods.py
│   │   ├── prompts/
│   │   │   └── evaluation_prompt.py
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── proposal/
│   │   ├── methods/
│   │   │   ├── evaluation_methods.py
│   │   │   └── generation_methods.py
│   │   ├── prompts/
│   │   │   ├── evaluation_prompt.py
│   │   │   └── generation_prompt.py
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   ├── config.py
│   └── main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

<br>

## Service Process

### Proposal Process

#### Proposal Evaluation Process

1. Request from client to server
    - Request DTO: `src/proposal/schemas.py`

      ```python
      class ProposalEvaluationRequestDto(BaseModel):
        title: str
        content: str
        media_type: str
        proposal_score: float
        additional_features: dict
      ```

    - Router: `src/proposal/router.py`

      ```python
      @router.post("/gen/proposal/evaluation")
      def proposal_evaluation_router(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
        return proposal_evaluation(request)
      ```

2. Service: 기획안에 대한 3단계 평가를 진행하고 반려식 해당 단계의 피드백을 생성한다.
    - 평가와 피드백 생성을 위한 프롬프트 및 기획안 준비

      ```python
      def proposal_evaluation(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
        # Proposal from the user
        proposal = request.title + SEP \
          + request.content + SEP \
          + request.media_type + SEP \
          + str(request.proposal_score) + SEP \
          + str(request.additional_features)
        proposal = proposal.replace("\n", "")

        # Prompts
        # for evaluation
        evaluation_prompt = EvaluationPrompt
        content_evaluation_prompt = evaluation_prompt.content_evaluation_prompt.value
        regulation_evaluation_prompt = evaluation_prompt.regulation_evaluation_prompt.value

        # for feedback generation
        generation_prompt = GenerationPrompt
        content_feedback_prompt = generation_prompt.content_feedback_prompt.value
        regulation_feedback_prompt = generation_prompt.regulation_feedback_prompt.value
        summary_generation_prompt = generation_prompt.summary_generation_prompt.value
        ...
      ```

    - 1단계 정량평가: `gpt-4o-mini`기준 롱폼 기준 200 숏폼 기준 100으로 평가
        - `src/proposal/methods/evaluation_methods.py`

          ```python
          # Volume
          # Got to be more than 200 hundreds tokens
          def volume_evaluation(proposal, media_type):
            tokenizer = tiktoken.encoding_for_model("gpt-4o-mini")
            if (media_type=="long_form"):
              return (len(tokenizer.encode(proposal))) < 200
            return (len(tokenizer.encode(proposal))) < 100
          ```

        - `src/proposal/service.py`

          ```python
          def proposal_evaluation(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
            ....
            # Volume Check
            if (volume_evaluation(proposal=proposal, media_type=request.media_type)):
              return ProposalEvaluationResponseDto(
                        evaluation_result=0,
                        feedback=FeedbackDto(
                            feedback_type=0,
                            current_score=0,
                            comment="기획안을 평가할 내용이 부족하여 더 이상의 평가가 불가능합니다.",
                            violations=[]
                            ),
                        summary=SummaryDto(
                            title="",
                            content="",
                            keyword=[]
                            )
                        )
            ....
          ```

    - 2단계 내용평가
      - 기획안 내용 평가 함수: `src/proposal/methods/evaluation_methods.py`

        ```python
        # Content
        # Content score got to be 65 at least
        def content_evaluation(proposal, content_evaluation_prompt):
          llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.4)
          prompt_template = ChatPromptTemplate.from_messages(
            [("system", content_evaluation_prompt), ("user", "{proposal}")]
          )
          chain = prompt_template | llm | StrOutputParser()
          return json.loads(chain.invoke({"proposal": proposal}))
        ```

      - 반려시 피드백 생성 함수: `src/proposal/methods/generation_methods.py`

        ```python
        def content_feedback(proposal, content_feedback_prompt):
          llm = ChatOpenAI(model='gpt-4o-mini', temperature=1)
          prompt_template = ChatPromptTemplate.from_messages(
            [("system", content_feedback_prompt), ("user", PROPOSAL)]
          )
          chain = prompt_template | llm | StrOutputParser()
          return chain.invoke({"proposal": proposal})
        ```

      - 기획안 내용 평가 부분: `src/proposal/service.py`

        ```python
        def proposal_evaluation(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
          ...
          # Content Check
          content_evaluation_result = content_evaluation(
            proposal,
            content_evaluation_prompt
          )

          total_score = float(content_evaluation_result['message']) + float(content_evaluation_result['target']) + float(content_evaluation_result['relevance'])

          evaluated_proposal = "Message: " + content_evaluation_result['message'] + "Target: " + \
                content_evaluation_result['target'] + "Relevance: " + \
                content_evaluation_result['relevance'] + SEP + proposal

          if (total_score <= 65.0):
            generated_feedback = content_feedback(
                content_feedback_prompt=content_feedback_prompt,
                proposal=evaluated_proposal
              )
            return ProposalEvaluationResponseDto(
              evaluation_result=0,
              feedback=FeedbackDto(
                feedback_type=1,
                current_score=total_score,
                comment=generated_feedback,
                violations=[]
              ),
              summary=SummaryDto(
                title="",
                content="",
                current_score=0.0,
                keyword=[]
              )
            )
          ...
        ```

    - 3단계 유해성평가
      - 유해성 평가 함수: `src/proposal/methods/evaluation_methods.py`

        ```python
        # Regulation
        # 방송통신심의위원회 Standards
        def regulation_evaluation(proposal, regulation_evaluation_prompt):
          llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.4)
          prompt_template = ChatPromptTemplate.from_messages(
            [("system", regulation_evaluation_prompt), ("user", "{proposal}")]
          )
          chain = prompt_template | llm | StrOutputParser()
          return json.loads(chain.invoke({"proposal": proposal}))
        ```

      - 반려시 피드백 생성 함수: `src/proposal/methods/generation_methods.py`

        ```python
        def regulation_feedback(proposal, regulation_feedback_prompt):
          llm = ChatOpenAI(model='gpt-4o-mini', temperature=1)
          prompt_template = ChatPromptTemplate.from_messages(
            [("system", regulation_feedback_prompt), ("user", PROPOSAL)]
          )
          chain = prompt_template | llm | StrOutputParser()
          return chain.invoke({"proposal": proposal})
        ```

      - 유행성 평가 부분: `src/proposal/service.py`

        ```python
        def proposal_evaluation(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
          ...
          regulation_evaluation_result = regulation_evaluation(
            proposal=proposal,
            regulation_evaluation_prompt=regulation_evaluation_prompt
          )

          appropriate = bool(regulation_evaluation_result['appropriate'])

          violated_categories = list(regulation_evaluation_result['category'])

          if (not appropriate):
            violated_proposal = "Violated Categories: " + \
                    str(violated_categories) + SEP + proposal

          generated_feedback = regulation_feedback(
            regulation_feedback_prompt=regulation_feedback_prompt,
            proposal=violated_proposal
          )

          return ProposalEvaluationResponseDto(
            evaluation_result=0,
            feedback=FeedbackDto(
                feedback_type=2,
                current_score=total_score,
                comment=generated_feedback,
                violations=violated_categories
            ),
            summary=SummaryDto(
                title="",
                content="",
                current_score=0.0,
                keyword=[]
            )
          )
          ...
        ```

3. 3단계 평가 통과시 요약 생성
    - 기획안 요양 생성 및 반환
      - 기획안 요약 함수: `src/proposal/methods/generation_methods.py`

        ```python
        def summary_generator(proposal, summary_generation_prompt):
          llm = ChatOpenAI(model='gpt-4o-mini', temperature=1)
          prompt_template = ChatPromptTemplate.from_messages(
            [("system", summary_generation_prompt), ("user", PROPOSAL)]
          )
          chain = prompt_template | llm | StrOutputParser()
          return json.loads(chain.invoke({"proposal": proposal}))
        ```

      - 기획안 요약 및 결과 반환: `src/proposal/service.py`

        ```python
        def proposal_evaluation(request: ProposalEvaluationRequestDto) -> ProposalEvaluationResponseDto:
          ...
          # Summary Generator
          generated_summary = summary_generator(
            proposal=proposal,
            summary_generation_prompt=summary_generation_prompt
          )

          return ProposalEvaluationResponseDto(
            evaluation_result=1,
            feedback=FeedbackDto(
                feedback_type=0,
                current_score=0.0,
                comment="",
                violations=[]
            ),
            summary=SummaryDto(
                title=generated_summary['title'],
                content=generated_summary['content'],
                keyword=generated_summary['keyword']
            )
          )
        ```

4. Prompt Templates
    - 양이 많은 관계로 링크로 대체하였습니다.
    - 기획안 평가
      - [`src/proposal/prompts/evaluation_prompt.py`](https://github.com/KTB-6-Joing/joing-genai-server/blob/develop/src/proposal/prompts/evaluation_prompt.py)
    - 피드백, 요약 생성
      - [`src/proposal/prompts/generation_prompt.py`](https://github.com/KTB-6-Joing/joing-genai-server/blob/develop/src/proposal/prompts/generation_prompt.py)

<br>

#### Summary Generation Process

1. Request from client to server
    - Request DTO: `src/proposal/schemas.py`

      ```python
      # Summary
      class SummaryGenerationRequestDto(BaseModel):
        title: str
        content: str
        media_type: str
        proposal_score: float
        additional_features: dict
      ```

    - Router: `src/proposal/router.py`

      ```python
      @router.post("/gen/proposal/summary")
      def summary_generation_router(request: SummaryGenerationRequestDto) -> ProposalEvaluationResponseDto:
        return summary_generation(request)
      ```

2. Service: 평가가 완료된 기획안에 한해서 추천을 위한 요약에 대한 재생성 및 반환
    - 기획안 요양 생성 및 반환
      - 기획안 요약 함수: `src/proposal/methods/generation_methods.py`

        ```python
          def summary_generator(proposal, summary_generation_prompt):
            llm = ChatOpenAI(model='gpt-4o-mini', temperature=1)
            prompt_template = ChatPromptTemplate.from_messages(
              [("system", summary_generation_prompt), ("user", PROPOSAL)]
            )
            chain = prompt_template | llm | StrOutputParser()
            return json.loads(chain.invoke({"proposal": proposal}))
        ```

      - 기획안 요약 생성 처리 함수: `src/proposal/service.py`

        ```python
        def summary_generation(request: SummaryGenerationRequestDto) -> ProposalEvaluationResponseDto:
          # Proposal retrieved from db
          proposal = request.title + SEP \
            + request.content + SEP \
            + request.media_type + SEP \
            + str(request.proposal_score) + SEP \
            + str(request.additional_features)

          # Prompt
          generation_prompt = GenerationPrompt
          summary_generation_prompt = generation_prompt.summary_generation_prompt.value

          # Generator Method
          generated_summary = summary_generator(
            proposal=proposal,
            summary_generation_prompt=summary_generation_prompt
          )

          return ProposalEvaluationResponseDto(
            evaluation_result=1,
            feedback=FeedbackDto(
                feedback_type=0,
                current_score=0.0,
                comment="",
                violations=[]
                ),
            summary=SummaryDto(
              title=generated_summary['title'],
              content=generated_summary['content'],
              keyword=generated_summary['keyword']
              )
            )
        ```

3. Prompt Templates
    - 양이 많은 관계로 링크로 대체하였습니다.
    - 피드백, 요약 생성
      - [`src/proposal/prompts/generation_prompt.py`](https://github.com/KTB-6-Joing/joing-genai-server/blob/develop/src/proposal/prompts/generation_prompt.py)

<br>

### Channel Process

#### Channel Evaluation Process

1. Request from client to server
    - Request DTO: `src/channel/schemas.py` - 채널아이디가 정확히 24자여야한다.

      ```python
      class ChannelEvaluationRequestDto(BaseModel):
        channel_id: str = Field(min=24, max_length=24)
        @field_validator("channel_id")
        def validate_channel_id(cls, value):
          if len(value) != 24:
              raise HTTPException(
                  status_code=422, detail={"code": 'INVALID_CHANNEL_ID_FORMAT', "message": "유효하지 않은 형식의 채널아이디입니다."})
          return value
      ```

    - Router: `src/channel/router.py`

      ```python
      @router.post("/gen/channel/evaluation")
      def channel_evaluation_router(request: ChannelEvaluationRequestDto) -> ChannelEvaluationResponseDto:
        return channel_evaluation(request)
      ```

2. Service: 정확한 평가를 위해 가장 최근에 올라온 영상의 Thumbnail(Image)과 영상 제목 및 설명(Text)을 둘다 활용하여 평가를 진행한다.
    - Data Request: 채널 정보, 최근 영상(4개) 및 추후 회원가입에 필요한 구독자 수와 채널 프로필 이미지 조회
      - `src/channel/service.py`

        ```python
        def channel_evaluation(request: ChannelEvaluationRequestDto) -> ChannelEvaluationResponseDto:
          # Getting Youtube Data API Object
          youtube_data_api = youtube_data_api_request(api_key=settings.YOUTUBE_DATA_API_KEY)

          # Getting Channel Info
          channel_response = youtube_channel_request(youtube_data_api=youtube_data_api, channel_id=request.channel_id)

          # Getting Playlist
          playlist_response = playlist_request(youtube_data_api=youtube_data_api, youtube_channel=channel_response)

          # Getting Channel Image
          channel_image = channel_image_parsing(channel_id=request.channel_id, youtube_data_api=youtube_data_api)

          # Getting Channel Subscriber Counts
          subscribers_count = channel_subscribers_parsing(youtube_data_api=youtube_data_api, channel_id=request.channel_id)

          # Parsing response aka preprocessing
          videos_text_info, thumbnail_urls = response_preprocessing(playlist_response=playlist_response)
        ```

      - `src/channel/methods/requests_methods.py`: 채널 아이디가 조회 되지 않을경우 채널의 영상이 4개 이상 없을 경우 평가 불가

        ```python
        def youtube_data_api_request(api_key):
          youtube_data_api = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
          return youtube_data_api

        def youtube_channel_request(youtube_data_api, channel_id):
          channel_response = youtube_data_api.channels().list(part='contentDetails',id=channel_id).execute()
          if (channel_response['pageInfo']['totalResults'] == 0):
            raise HTTPException(status_code=422, detail={"code": 'INVALID_CHANNEL_ID', "message": "유효하지 않은 채널아이디입니다."})
          return channel_response

        def channel_image_parsing(youtube_data_api, channel_id):
          try:
            channel_response = youtube_data_api.channels().list(part='snippet', id=channel_id).execute()

            # Check if the response contains valid channel data
            if 'items' in channel_response and len(channel_response['items']) > 0:
              thumbnails = channel_response['items'][0]['snippet']['thumbnails']
              return thumbnails['medium']['url']
            else:
              print("Channel not found or no snippet data available.")
              return None
          except Exception as e:
            print(e)
            return None

        def channel_subscribers_parsing(youtube_data_api, channel_id):
          channel_response = youtube_data_api.channels().list(part='statistics',id=channel_id).execute()
          return channel_response["items"][0]["statistics"]["subscriberCount"]

        def playlist_request(youtube_data_api, youtube_channel):
          uploads_playlist_id = youtube_channel["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
          playlist_response = youtube_data_api.playlistItems().list(
              part='snippet',
              playlistId=uploads_playlist_id,
              maxResults=4,
              pageToken=None
            ).execute()

          if (len(playlist_response['items']) < 4):
            raise HTTPException(
              status_code=422, detail={"code": 'NOT_ENOUGH_UPLOADS', "message": "영상의 개수가 충분하지 않아 더이상의 평가가 불가능합니다."})
          return playlist_response

        def image_request(image_urls):
          image_responses = []
          for i in range(len(image_urls)):
              image_responses.append(requests.get(image_urls[i]))
          return image_responses
        ```

    - Image Evaluation
      - Preprocessing: `src/channel/methods/preprocessing_methods.py`: 한번의 요청으로 처리하기 위하여 4장의 Thumbnail을 한장으로 변환

        ```python
        def image_preprocessing(image_response):
          img_in_bytes = []
          for i in range(len(image_response)):
              img_in_bytes.append(Image.open(BytesIO(image_response[i].content)))

          img_width = img_in_bytes[0].size[0]
          img_height = img_in_bytes[0].size[1]

          combined_width = img_width*2
          combined_height = img_height*2

          combined_image = Image.new('RGB', (combined_width, combined_height))

          combined_image.paste(img_in_bytes[0], (0, 0))
          combined_image.paste(img_in_bytes[1], (img_width, 0))
          combined_image.paste(img_in_bytes[2], (0, img_height))
          combined_image.paste(img_in_bytes[3], (img_width, img_height))

          buffer = BytesIO()
          combined_image.save(buffer, format="JPEG")
          buffer.seek(0)
          combined_base64 = base64.b64encode(buffer.read()).decode('utf-8')

          return combined_base64
        ```

      - Evaluation: `src/channel/methods/evaluation_methods.py`

        ```python
        def image_evaluation(base64_image, prompt):
          messages = [
              {
                  "role": "system",
                  "content": prompt
              },
              {
                  "role": "user",
                  "content": [
                      {
                          "type": "text", "text": """This is an image that has 4 recent thumbnail of different videos posted by a Youtuber."""
                      },
                      {
                          "type": "image_url",
                          "image_url":
                              {
                                  "url": f"data:image/jpeg;base64,{base64_image}"
                              },
                      },
                  ],
              }
          ]

          client = OpenAI()
          response = client.chat.completions.create(
              model="gpt-4o-2024-08-06",
              messages=messages,
              max_tokens=300,
          )
          return json.loads(response.choices[0].message.content)
        ```

    - Text Evaluation
      - Preprocessing: `src/channel/methods/preprocessing_methods.py`

        ```python
        def response_preprocessing(playlist_response):
          text_info = []
          thumbnail_urls = []

          for item in playlist_response["items"]:
              snippet = item["snippet"]
              # title
              video_title = snippet["title"]
              # description
              video_desc = snippet['description']
              # thumbnails - urls
              video_thumbnail_url = snippet['thumbnails']['standard']['url']
              text_info.append({
                  "title": video_title,
                  "description": video_desc,
              })
              thumbnail_urls.append(video_thumbnail_url)
          return text_info, thumbnail_urls
        ```

      - Evaluation: `src/channel/methods/evaluation_methods.py`

        ```python
        def text_evaluation(description, prompt):
          llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)
          prompt_template = ChatPromptTemplate.from_messages([("system", prompt), ("user", "{list}")])
          chain = prompt_template | llm | StrOutputParser()
          return json.loads(chain.invoke({"list": description}))
        ```

    - `src/channel/service.py`: 이미지 및 텍스트 전처리,평가 요청 및 결과 반환

      ```python
      def channel_evaluation(request: ChannelEvaluationRequestDto) -> ChannelEvaluationResponseDto:
        ...
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
      ```

<br>

## Results 

### Proposal Evaluation Result

- 1단계: 정량 평가 탈락
  
  ![Volume Evaluation Failed](/static/proposal/volume_evaluation_failed.png)

- 2단계: 내용 평가 탈락

  ![Content Evaluation Failed](/static/proposal/content_evaluation_failed.png)

- 3단계: 유해성 평가 탈락

  ![Regulation Evaluation Failed](/static/proposal/reuglation_evaluation_failed.png)

<br>

### Summary Generation Result

- 기획안 평가 통과 후 요약 생성

  ![Summary Generated](/static/proposal/summary_generated.png)

<br>

### Channel Evaluation Result

- 채널 유행성 평가 통과

  ![Channel Evaluation Passed](/static/channel/channel_evaluation_passed.png)

- 채널 유해성 평가 탈락

  ![Channel Evaluation Failed](/static/channel/channel_evaluation_failed.png)
