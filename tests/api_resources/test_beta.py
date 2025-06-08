# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from acctest import Acctest, AsyncAcctest
from tests.utils import assert_matches_type
from acctest.types import BetaCreateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion(self, client: Acctest) -> None:
        beta = client.beta.create_completion(
            echo=False,
            frequency_penalty=0,
            logprobs=0,
            max_tokens=1024,
            model="deepseek-chat",
            presence_penalty=0,
            prompt="Once upon a time, ",
            stop=None,
            stream=False,
            stream_options=None,
            suffix=None,
            temperature=1,
            top_p=1,
        )
        assert_matches_type(BetaCreateCompletionResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_completion(self, client: Acctest) -> None:
        response = client.beta.with_raw_response.create_completion(
            echo=False,
            frequency_penalty=0,
            logprobs=0,
            max_tokens=1024,
            model="deepseek-chat",
            presence_penalty=0,
            prompt="Once upon a time, ",
            stop=None,
            stream=False,
            stream_options=None,
            suffix=None,
            temperature=1,
            top_p=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(BetaCreateCompletionResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_completion(self, client: Acctest) -> None:
        with client.beta.with_streaming_response.create_completion(
            echo=False,
            frequency_penalty=0,
            logprobs=0,
            max_tokens=1024,
            model="deepseek-chat",
            presence_penalty=0,
            prompt="Once upon a time, ",
            stop=None,
            stream=False,
            stream_options=None,
            suffix=None,
            temperature=1,
            top_p=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(BetaCreateCompletionResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncAcctest) -> None:
        beta = await async_client.beta.create_completion(
            echo=False,
            frequency_penalty=0,
            logprobs=0,
            max_tokens=1024,
            model="deepseek-chat",
            presence_penalty=0,
            prompt="Once upon a time, ",
            stop=None,
            stream=False,
            stream_options=None,
            suffix=None,
            temperature=1,
            top_p=1,
        )
        assert_matches_type(BetaCreateCompletionResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncAcctest) -> None:
        response = await async_client.beta.with_raw_response.create_completion(
            echo=False,
            frequency_penalty=0,
            logprobs=0,
            max_tokens=1024,
            model="deepseek-chat",
            presence_penalty=0,
            prompt="Once upon a time, ",
            stop=None,
            stream=False,
            stream_options=None,
            suffix=None,
            temperature=1,
            top_p=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(BetaCreateCompletionResponse, beta, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncAcctest) -> None:
        async with async_client.beta.with_streaming_response.create_completion(
            echo=False,
            frequency_penalty=0,
            logprobs=0,
            max_tokens=1024,
            model="deepseek-chat",
            presence_penalty=0,
            prompt="Once upon a time, ",
            stop=None,
            stream=False,
            stream_options=None,
            suffix=None,
            temperature=1,
            top_p=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(BetaCreateCompletionResponse, beta, path=["response"])

        assert cast(Any, response.is_closed) is True
