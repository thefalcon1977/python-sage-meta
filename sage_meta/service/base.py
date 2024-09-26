import logging
from typing import List, Optional

import facebook

from sage_meta.models import FacebookPageData, UserData
from sage_meta.service.content import ContentPublishing
from sage_meta.service.handlers import (
    AccountHandler,
    CommentHandler,
    HashtagHandler,
    MediaHandler,
    StoryHandler,
)

logger = logging.getLogger(__name__)


class FacebookClient:
    """
    A client for interacting with the Facebook Graph API.

    This class provides methods to fetch user data and manage various aspects
    of Facebook content and interactions, including accounts, media, comments,
    stories, and hashtags.

    Attributes:
        access_token (str): The access token used for authenticating requests to the Facebook Graph API.
        graph_url (str): The base URL for the Facebook Graph API.
        graph (facebook.GraphAPI): The Graph API client instance.
        user (Optional[UserData]): The user data object containing information about the authenticated user.
        insta_business (Optional): Placeholder for Instagram business account data (to be defined).
        pages (List[FacebookPageData]): A list of Facebook page data objects associated with the user.
        account_handler (AccountHandler): Handler for managing account-related operations.
        media_handler (MediaHandler): Handler for managing media-related operations.
        comment_handler (CommentHandler): Handler for managing comment-related operations.
        story_handler (StoryHandler): Handler for managing story-related operations.
        hashtag_handler (HashtagHandler): Handler for managing hashtag-related operations.
        content_publisher (ContentPublishing): Service for publishing content to Facebook.

    Args:
        access_token (str): The access token for authenticating with the Facebook Graph API.

    Methods:
        get_user_data() -> None:
            Fetches and initializes user data from the Facebook Graph API.
    """

    def __init__(self, access_token: str) -> None:
        """
        Initializes the FacebookClient with the provided access token.

        Args:
            access_token (str): The access token for authenticating with the Facebook Graph API.
        """
        self.access_token = access_token
        self.graph_url = "https://graph.facebook.com/v20.0"
        self.graph = facebook.GraphAPI(
            access_token=access_token, version="3.1")
        self.user: Optional[UserData] = None
        self.insta_business = None
        self.pages: List[FacebookPageData] = []
        self.get_user_data()
        self.account_handler: AccountHandler = AccountHandler(self)
        self.media_handler: MediaHandler = MediaHandler(self)
        self.comment_handler: CommentHandler = CommentHandler(self)
        self.story_handler: StoryHandler = StoryHandler(self)
        self.hashtag_handler: HashtagHandler = HashtagHandler(self)
        self.content_publisher: ContentPublishing = ContentPublishing(self)

    def get_user_data(self) -> None:
        """
        Fetches user data from the Facebook Graph API and initializes the user attribute.

        This method retrieves the user's ID, name, and email, and stores them in a UserData object.
        It also logs the retrieved user data or any errors encountered during the process.

        Raises:
            facebook.GraphAPIError: If there is an error fetching user data from the Graph API.
        """
        logger.debug("Fetching user data.")
        try:
            obj = self.graph.get_object("me", fields="id,name,email")
            additional_data = {
                k: v for k, v in obj.items() if k not in {"id", "name", "email"}
            }
            self.user = UserData(
                id=obj.get("id"),
                name=obj.get("name"),
                email=obj.get("email"),
                additional_data=additional_data,
            )
            logger.info("Retrieved user data: %s", self.user.id)
        except facebook.GraphAPIError as e:
            logger.error("Error fetching user data: %s", e)
            raise
