# Chat

Types:

```python
from acctest.types import ChatCreateCompletionResponse
```

Methods:

- <code title="post /chat/completions">client.chat.<a href="./src/acctest/resources/chat.py">create_completion</a>(\*\*<a href="src/acctest/types/chat_create_completion_params.py">params</a>) -> <a href="./src/acctest/types/chat_create_completion_response.py">ChatCreateCompletionResponse</a></code>

# Beta

Types:

```python
from acctest.types import BetaCreateCompletionResponse
```

Methods:

- <code title="post /beta/completions">client.beta.<a href="./src/acctest/resources/beta.py">create_completion</a>(\*\*<a href="src/acctest/types/beta_create_completion_params.py">params</a>) -> <a href="./src/acctest/types/beta_create_completion_response.py">BetaCreateCompletionResponse</a></code>

# Models

Types:

```python
from acctest.types import ModelListResponse
```

Methods:

- <code title="get /models">client.models.<a href="./src/acctest/resources/models.py">list</a>() -> <a href="./src/acctest/types/model_list_response.py">ModelListResponse</a></code>

# User

Types:

```python
from acctest.types import UserRetrieveBalanceResponse
```

Methods:

- <code title="get /user/balance">client.user.<a href="./src/acctest/resources/user.py">retrieve_balance</a>() -> <a href="./src/acctest/types/user_retrieve_balance_response.py">UserRetrieveBalanceResponse</a></code>
