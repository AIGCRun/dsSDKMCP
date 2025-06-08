# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from acctest import Acctest, AsyncAcctest
from tests.utils import assert_matches_type
from acctest.types import ChatCreateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion(self, client: Acctest) -> None:
        chat = client.chat.create_completion(
            frequency_penalty=0,
            logprobs=False,
            max_tokens=2048,
            messages=[
                {
                    "content": "You are a helpful assistant",
                    "role": "system",
                },
                {
                    "content": "Hi",
                    "role": "user",
                },
            ],
            model="deepseek-chat",
            presence_penalty=0,
            response_format={"type": "text"},
            stop=None,
            stream=False,
            stream_options=None,
            temperature=1,
            tool_choice="none",
            tools=None,
            top_logprobs=None,
            top_p=1,
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_completion(self, client: Acctest) -> None:
        response = client.chat.with_raw_response.create_completion(
            frequency_penalty=0,
            logprobs=False,
            max_tokens=2048,
            messages=[
                {
                    "content": "You are a helpful assistant",
                    "role": "system",
                },
                {
                    "content": "Hi",
                    "role": "user",
                },
            ],
            model="deepseek-chat",
            presence_penalty=0,
            response_format={"type": "text"},
            stop=None,
            stream=False,
            stream_options=None,
            temperature=1,
            tool_choice="none",
            tools=None,
            top_logprobs=None,
            top_p=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_completion(self, client: Acctest) -> None:
        with client.chat.with_streaming_response.create_completion(
            frequency_penalty=0,
            logprobs=False,
            max_tokens=2048,
            messages=[
                {
                    "content": "You are a helpful assistant",
                    "role": "system",
                },
                {
                    "content": "Hi",
                    "role": "user",
                },
            ],
            model="deepseek-chat",
            presence_penalty=0,
            response_format={"type": "text"},
            stop=None,
            stream=False,
            stream_options=None,
            temperature=1,
            tool_choice="none",
            tools=None,
            top_logprobs=None,
            top_p=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncAcctest) -> None:
        chat = await async_client.chat.create_completion(
            frequency_penalty=0,
            logprobs=False,
            max_tokens=2048,
            messages=[
                {
                    "content": "You are a helpful assistant",
                    "role": "system",
                },
                {
                    "content": "Hi",
                    "role": "user",
                },
            ],
            model="deepseek-chat",
            presence_penalty=0,
            response_format={"type": "text"},
            stop=None,
            stream=False,
            stream_options=None,
            temperature=1,
            tool_choice="none",
            tools=None,
            top_logprobs=None,
            top_p=1,
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncAcctest) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            frequency_penalty=0,
            logprobs=False,
            max_tokens=2048,
            messages=[
                {
                    "content": "You are a helpful assistant",
                    "role": "system",
                },
                {
                    "content": "Hi",
                    "role": "user",
                },
            ],
            model="deepseek-chat",
            presence_penalty=0,
            response_format={"type": "text"},
            stop=None,
            stream=False,
            stream_options=None,
            temperature=1,
            tool_choice="none",
            tools=None,
            top_logprobs=None,
            top_p=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncAcctest) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            frequency_penalty=0,
            logprobs=False,
            max_tokens=2048,
            messages=[
                {
                    "content": "You are a helpful assistant",
                    "role": "system",
                },
                {
                    "content": "Hi",
                    "role": "user",
                },
            ],
            model="deepseek-chat",
            presence_penalty=0,
            response_format={"type": "text"},
            stop=None,
            stream=False,
            stream_options=None,
            temperature=1,
            tool_choice="none",
            tools=None,
            top_logprobs=None,
            top_p=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
