# Building A Medium Writer Using Langchain #

In the age of rapid digitalization, content creation has become an essential element of our daily lives. Today, I would like to share with you an exciting Python program that leverages the power of artificial intelligence to create Medium articles.

The script is a powerful use-case of how to utilize Langchain, a library for creating generative language models chains. It makes use of Streamlit, an open-source Python library used for creating custom web-apps, and OpenAI’s GPT model, a transformer-based language model. It uses an API key for authenticating with OpenAI’s services, where the actual language model computations happen.

## Overview ##
The code shared above is a simple implementation of an automatic content generator for Medium articles. The user inputs a subject or a topic, and the code produces a title and a script for a Medium article based on that topic.

## The Code: A Closer Look ##
To start with, the essential libraries and modules are imported. Among these, `OpenAI` from `langchain.llms` is the interface to the language model, `LLMChain` from `langchain.chains` allows to create a sequence of operations with language models, and `ConversationBufferMemory` from `langchain.memory` helps in memory management.

```python
import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
```

The `OPENAI_API_KEY` environment variable is set using the imported `apikey`. This key is used for authenticating the user with OpenAI’s servers.

```python
os.environ['OPENAI_API_KEY'] = apikey
```

Streamlit is then used to create a simple web app interface with a title and a text input field. The user can input their desired topic here.

