from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Category:
    """
    Represents a category for Facebook pages or Instagram accounts.

    Attributes:
        id (str): Unique identifier for the category.
        name (str): Name of the category.
    """
    id: str
    name: str


@dataclass
class Insight:
    """
    Represents an insight related to an Instagram account or media.

    Attributes:
        id (str): Unique identifier for the insight.
        name (str): Name of the insight.
        period (str): The time period for which the insight is relevant.
        values (List[Dict[str, str]]): A list of key-value pairs representing the insight values.
        title (Optional[str]): Optional title for the insight.
        description (Optional[str]): Optional description providing more details about the insight.
    """
    id: str
    name: str
    period: str
    values: List[Dict[str, str]] = field(default_factory=list)
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)


@dataclass
class AccountInsight:
    """
    Represents an account-level insight for an Instagram account.

    Attributes:
        id (str): Unique identifier for the account insight.
        name (str): Name of the account insight.
        period (str): The time period for which the account insight is relevant.
        values (List[Dict[str, str]]): A list of key-value pairs representing the account insight values.
        title (Optional[str]): Optional title for the account insight.
        description (Optional[str]): Optional description providing more details about the account insight.
    """
    id: str
    name: str
    period: str
    values: List[Dict[str, str]] = field(default_factory=list)
    title: Optional[str] = field(default="")
    description: Optional[str] = field(default="")


@dataclass
class Comment:
    """
    Represents a comment on a post or media.

    Attributes:
        id (str): Unique identifier for the comment.
        text (Optional[str]): The text content of the comment.
        username (Optional[str]): The username of the commenter.
        like_count (Optional[int]): The number of likes the comment has received.
        timestamp (Optional[str]): The time at which the comment was made.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the comment.
    """
    id: str
    text: Optional[str] = field(default=None)
    username: Optional[str] = field(default=None)
    like_count: Optional[int] = field(default=None)
    timestamp: Optional[str] = field(default=None)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class Story:
    """
    Represents a story from an Instagram account.

    Attributes:
        id (str): Unique identifier for the story.
        media_type (Optional[str]): The type of media (e.g., image, video).
        media_url (Optional[str]): The URL of the media associated with the story.
        timestamp (Optional[str]): The time at which the story was posted.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the story.
    """
    id: str
    media_type: Optional[str] = field(default=None)
    media_url: Optional[str] = field(default=None)
    timestamp: Optional[str] = field(default=None)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class Media:
    """
    Represents media posted on an Instagram account.

    Attributes:
        id (str): Unique identifier for the media.
        caption (Optional[str]): The caption associated with the media.
        media_type (Optional[str]): The type of media (e.g., image, video).
        media_url (List[str]): A list of URLs for the media.
        timestamp (Optional[str]): The time at which the media was posted.
        like_count (Optional[int]): The number of likes the media has received.
        comments_count (Optional[int]): The number of comments on the media.
        comments (List[Comment]): A list of comments associated with the media.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the media.
    """
    id: str
    caption: Optional[str] = field(default=None)
    media_type: Optional[str] = field(default=None)
    media_url: List[str] = field(default_factory=list)
    timestamp: Optional[str] = field(default=None)
    like_count: Optional[int] = field(default=None)
    comments_count: Optional[int] = field(default=None)
    comments: List[Comment] = field(default_factory=list)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class InstagramAccount:
    """
    Represents an Instagram account.

    Attributes:
        id (str): Unique identifier for the Instagram account.
        username (str): Username of the Instagram account.
        follows_count (int): The number of accounts the user follows.
        followers_count (int): The number of followers the account has.
        media_count (int): The total number of media posted by the account.
        profile_picture_url (Optional[str]): URL of the account's profile picture.
        website (Optional[str]): URL of the account's website.
        biography (Optional[str]): The biography of the account.
        media (List[Media]): A list of media posted by the account.
        insights (List[Insight]): A list of insights associated with the account.
        stories (List[Story]): A list of stories posted by the account.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the account.
    """
    id: str
    username: str
    follows_count: int
    followers_count: int
    media_count: int
    profile_picture_url: Optional[str] = field(default=None)
    website: Optional[str] = field(default=None)
    biography: Optional[str] = field(default=None)
    media: List[Media] = field(default_factory=list)
    insights: List[Insight] = field(default_factory=list)
    stories: List[Story] = field(default_factory=list)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class FacebookPageData:
    """
    Represents data related to a Facebook page.

    Attributes:
        id (str): Unique identifier for the Facebook page.
        name (str): Name of the Facebook page.
        category (str): Category of the Facebook page.
        access_token (str): Access token for API operations.
        category_list (List[Category]): A list of categories associated with the page.
        tasks (List[str]): A list of tasks associated with the page.
        instagram_business_account (Optional[InstagramAccount]): The associated Instagram business account, if any.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the Facebook page.
    """
    id: str
    name: str
    category: str
    access_token: str
    category_list: List[Category] = field(default_factory=list)
    tasks: List[str] = field(default_factory=list)
    instagram_business_account: Optional[InstagramAccount] = field(
        default=None)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class UserData:
    """
    Represents user data for a Facebook user.

    Attributes:
        id (str): Unique identifier for the user.
        name (str): Name of the user.
        email (Optional[str]): Email address of the user.
        pages (List[FacebookPageData]): A list of Facebook pages managed by the user.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the user.
    """
    id: str
    name: str
    email: Optional[str] = field(default=None)
    pages: List[FacebookPageData] = field(default_factory=list)
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class PostMention:
    """
    Represents a mention of a post in a comment or another post.

    Attributes:
        id (str): Unique identifier for the post mention.
        media_type (str): The type of media (e.g., image, video).
        media_url (str): The URL of the media associated with the mention.
        caption (str): The caption of the post being mentioned.
        comments_count (int): The number of comments on the mentioned post.
        like_count (int): The number of likes on the mentioned post.
        timestamp (str): The time at which the post was made.
        username (str): The username of the post owner.
        owner (str): The owner of the post being mentioned.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the mention.
    """
    id: str
    media_type: str
    media_url: str
    caption: str
    comments_count: int
    like_count: int
    timestamp: str
    username: str
    owner: str
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class CommentMention:
    """
    Represents a mention of a comment in a post or another comment.

    Attributes:
        id (str): Unique identifier for the comment mention.
        text (str): The text content of the mentioned comment.
        like_count (int): The number of likes the mentioned comment has received.
        timestamp (str): The time at which the comment was made.
        username (str): The username of the commenter.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the mention.
    """
    id: str
    text: str
    like_count: int
    timestamp: str
    username: str
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)


@dataclass
class ReplyMention:
    """
    Represents a mention of a reply to a comment.

    Attributes:
        id (str): Unique identifier for the reply mention.
        message (str): The text content of the reply.
        timestamp (str): The time at which the reply was made.
        additional_data (Dict[str, Optional[str]]): A dictionary for any additional data related to the mention.
    """
    id: str
    message: str
    timestamp: str
    additional_data: Dict[str, Optional[str]] = field(default_factory=dict)
