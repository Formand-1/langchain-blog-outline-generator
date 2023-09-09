import streamlit as st
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="🦜🔗 Blog Outline Generator App")
st.title('🦜🔗 Blog Outline Generator App')

# Adding some white space after the header
st.write("\n\n")

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(topic):
    with st.spinner('Generating outline...'):
        try:
            llm = OpenAI(model_name='gpt-3.5-turbo-0613', openai_api_key=openai_api_key)
            prompt_query = f'''
            You are an exceptionally talented writer. Given the topic "{topic}", generate an outline that includes specific main points and FAQs. Do not generate content for the Introduction, Conclusion, or Footnotes/References; instead, provide a brief guideline on what they should cover.
            
            User: Please generate a structured outline for a blog about {topic}. Your response should be in markdown format and follow the structure below:

            ### Outline for {topic}
            1. **Introduction**: A section that sets the tone for the rest of the article. It should provide a brief overview of what the article will cover, capture the readers' attention, and motivate them to continue reading.
            2. **Main Points**: 
                - **Point 1**: Brief description.
                    - Subpoint (if relevant): Brief description.
                - **Point 2**: Brief description.
                    - Subpoint (if relevant): Brief description.
                - (Continue as needed for additional points)
            3. **FAQ**: Contains 3-5 common questions people often ask about {topic}.
            4. **Conclusion**: A section that wraps up the main points of the article, reinforces its main message, and provides a takeaway for the readers. Here, the writer should also offer their personal takeaway and opinion on the topic.
            5. **Footnotes/References**: Used to cite sources, provide additional information, or clarify points made in the article. It helps in building credibility and providing readers with the opportunity to explore topics in more depth.

            Remember, this is just an outline. Keep each point concise and avoid delving deep.
            '''
            
            response = llm(prompt_query)
            
            # Check if the response is a string (since that's what we seem to be receiving)
            if isinstance(response, str):                
                # Render the content as markdown
                st.markdown(response)
                
                # Create a temporary file with the content
                with open('temp_outline.txt', 'w') as f:
                    f.write(response)

                # Let the user download the file
                with open('temp_outline.txt', 'rb') as f:
                    st.download_button('Download Outline', f, file_name='outline.txt', mime='text/plain')

                # Optionally, remove the temporary file
                os.remove('temp_outline.txt')
            else:
                st.error("Unexpected response format from the model.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")



with st.form('myform'):
    topic_text = st.text_input('Enter keyword or topic:', '')
    st.write("\n")  # Adding white space before the submit button
    submitted = st.form_submit_button('Submit')
    st.write("\n")  # Adding white space after the submit button
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(topic_text)
