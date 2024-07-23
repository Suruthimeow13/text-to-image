from openai import OpenAI
import streamlit as st
from apikey import API_KEY

client = OpenAI(api_key=API_KEY)

def generate_images(img_description, no_of_img):
    images=[]
    for i in range(no_of_img):
        img_response=client.images.generate(
            model="dall-e-2",
            prompt=img_description,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url=img_response.data[0].url
        images.append(image_url)
    return image_url
st.set_page_config(page_title="Image Generator", page_icon=":camera:", layout="wide")

st.title("DALL-E-3 Image Generation")

st.subheader("Powered by DALL-E")
img_description = st.text_input("Enter a description for the image:")
no_of_img = st.number_input("select the number of images you want to generate", min_value=1, max_value=5, value=1)

if st.button("Generate Images"):
    generate_image=generate_images(img_description, no_of_img)
    st.image(generate_image)