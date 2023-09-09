import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate

st.set_page_config(page_title ="🦜🔗 Blog Outline Generator App")
st.title('🦜🔗 Blog Outline Generator App')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(topic):
  llm = OpenAI(model_name='text-davinci-003', openai_api_key=openai_api_key)
  # Prompt
  template = '''
  To achieve a concise and precise outline, please generate an outline for a blog about {topic}. Kindly follow the structure below in markdown format:

  ## Introduction
  A brief description of the topic.

  ## Main Topic 1 (or Subtopic Title 1)
  Brief description.
  ### Subtopic (if relevant)
  Brief description.

  ## Main Topic 2 (or Subtopic Title 2)
  Brief description.
  ### Subtopic (if relevant)
  Brief description.

  (Continue as needed for additional main topics and subtopics)

  ## FAQ
  Contains 3-5 common questions people often ask about {topic}.

  ## Conclusion
  A brief summary.

  ## Footnotes
  Short references or additional remarks (if necessary).

  Note: Focus solely on providing an outline. Avoid delving deep into each point.
  '''

  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form('myform'):
  topic_text = st.text_input('Enter keyword:', '')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(topic_text)
