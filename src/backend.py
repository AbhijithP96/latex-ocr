import os
from dotenv import load_dotenv
import base64
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()
llm = ChatNVIDIA(
    model=os.environ["NVIDIA_MODEL"], nvidia_api_key=os.environ["NVIDIA_API_KEY"]
)
# Define the instruction for the LLM
instruction = """Understand the mathematical equation in the provided image and output the corresponding LaTeX code.
                            Here are some guidelines you MUST follow or you will be penalized:
                            - NEVER include any additional text or explanations.
                            - DON'T add dollar signs ($) around the LaTeX code.
                            - DO NOT extract simplified versions of the equations.
                            - NEVER add documentclass, packages or begindocument.
                            - DO NOT explain the symbols used in the equation.
                            - Output only the LaTeX code corresponding to the mathematical equations in the image."""


def run_inference(img_data):
    """
    Method to run inference on the provided image data using NVIDIA AI Models.

    Args:
        img_data: _image data in bytes format

    Returns:
        LLM response containing the LaTeX code.
    """

    b64 = base64.b64encode(img_data).decode("utf-8")  # Convert bytes to base64 string
    data_url = f"data:image/png;base64,{b64}"  # Create data URL

    resp = llm.invoke(
        [
            HumanMessage(
                content=[
                    {"type": "text", "text": instruction},
                    {
                        "type": "image_url",
                        "image_url": {"url": data_url},
                    },
                ]
            )
        ]
    )  # Invoke the LLM with the image and instruction

    return resp.content
