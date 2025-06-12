import streamlit as st

from dotenv import load_dotenv
from llm import get_ai_message


st.set_page_config(
    page_title="tax bot",
    page_icon=":guardsman", #이모지 아이콘
    layout="wide",  #레이아웃
    initial_sidebar_state="expanded",   #사이드바 초기상태
)

st.title("Stream 기본예제")
st.caption("소득세에 관련된 모든 것을 답변해드립니다 :)")

load_dotenv()


# pinecone_api_key = os.getenv('PINECONE_API_KEY')
# pc = Pinecone(api_key=pinecone_api_key)
if "message_list" not in st.session_state:
    st.session_state.message_list = []
    
for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# print(f"before == {st.session_state.message_list}")

if user_question := st.chat_input(placeholder="소득세에 관련하여 궁금한 내용을 말씀해주세요"):
    # pass
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다."):
        ai_response = get_ai_message(user_question)
        with st.chat_message("ai"):
            get_ai_message = st.write_stream(ai_response)   #다음 질의하면 답변이 지워져서 변수로 받음. 
        st.session_state.message_list.append({"role": "ai", "content": get_ai_message})
    

# print(f"after == { st.session_state.message_list}")