# LaTeX Equation From Images
This Streamlit application allows users to upload images containing mathematical equations and converts them into LaTeX code using NVIDIA's AI endpoints.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AbhijithP96/latex-ocr.git
    ```
2. Navigate to the project directory:
    ```bash
    cd latex-ocr
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up environment variables for NVIDIA API:
   - Create a `.env` file in the root directory.
   - Add the following lines to the `.env` file:
     ```
     NVIDIA_API_KEY=your_nvidia_api_key
     NVIDIA_MODEL=meta/llama-3.2-11b-vision-instruct
     ```    
5. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open your web browser and navigate to `http://localhost:8501`.
2. Upload an image containing a mathematical equation.
3. Click the "Generate LaTeX Code" button to generate the LaTeX code.