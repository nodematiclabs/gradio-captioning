import gradio as gr
import torch

from transformers import pipeline
from PIL import Image

captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

def generate_caption(image):
    result = captioner(image)
    return result[0]['generated_text']

demo = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="Image Captioning App",
    description="Upload an image to get an automatically generated caption!"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)