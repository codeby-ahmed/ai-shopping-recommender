from phi.agent import Agent
from phi.model.huggingface import HuggingFaceChat

import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()



def recommend(product, color, special_feature, budget):
    """
    Generates product recommendations using a local LLM.
    """
    model = HuggingFaceChat(
        model_name="EleutherAI/gpt-neo-2.7B",
        api_key=os.environ["API_KEY"]  # make sure this line is indented exactly 4 spaces from 'model ='
    )
    agent = Agent(
        name="Shopping recommendations",
        model=model,
        instructions=[
            "You are a product recommender agent specializing in finding products that match user preferences.",
            "Prioritize products that match at least 80% of the user's requirements.",
            "Search only from trusted e-commerce websites such as Daraz and Alibaba other reputable platforms.",
            "Ensure every recommended product is currently in stock and available for purchase.",
            "For each product, clearly provide: product name, price, brand, key features, and availability status.",
            "Always include a valid, direct product URL for every recommendation.",
            "Format the response in a clean, structured list and show only the top 5 results.",
        ],
        tools=[],  # No external tools requiring API keys
        markdown=True
    )
    
    # Build the prompt
    prompt = f"Please find the {product} with {color} color and {special_feature} and {budget} budget."
    
    # Run agent and get recommendations
    output = agent.run(prompt)
    
    return output.content


def main():
    # HTML header
    html_temp = """
    <div style="background-color:yellow;padding:8px">
    <h2 style="color:gray;text-align:center;">Shopping Recommendations by AI Agent</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)    
    
    # App logo
    st.image("app_logo.png", width=300)
   
    # Inputs
    product = st.text_input("**Product**", "")
    color = st.text_input("**Color**", "")
    special_feature = st.text_input("**Specific requirements**", "")
    budget = st.text_input("**Budget**", "")
    
    # Button style
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #DD3300;
        color:#eeffee;
    }
    </style>""", unsafe_allow_html=True)

    # Recommend button
    if st.button("Recommend"):
        try:
            results = recommend(product, color, special_feature, budget)
            st.success(results)
        except Exception as e:
            st.error(f"Error generating recommendations: {e}")
    

if __name__ == '__main__':
    main()
