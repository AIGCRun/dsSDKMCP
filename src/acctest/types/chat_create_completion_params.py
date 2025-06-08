# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateCompletionParams", "Message", "ResponseFormat"]


class ChatCreateCompletionParams(TypedDict, total=False):
    frequency_penalty: Required[int]

    logprobs: Required[bool]

    max_tokens: Required[int]

    messages: Required[Iterable[Message]]

    model: Required[str]

    presence_penalty: Required[int]

    response_format: Required[ResponseFormat]

    stop: Required[None]

    stream: Required[bool]

    stream_options: Required[None]

    temperature: Required[int]

    tool_choice: Required[str]

    tools: Required[None]

    top_logprobs: Required[None]

    top_p: Required[int]


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


class ResponseFormat(TypedDict, total=False):
    type: Required[str]
