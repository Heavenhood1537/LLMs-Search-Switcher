# 🧠 LLMs Search Switcher

A powerful local LLM-based search interface that allows you to switch between different locally running language models while performing web searches. This tool combines the capabilities of multiple open-source LLMs with real-time web search functionality via Google Programmable Search Engine.

## ✨ Features

- 🖥️ Local LLM Integration via Ollama
- 🔄 Support for multiple models:
  - Gemma 3
  - OpenHermes
  - Llama 3.1
  - Mistral
  - CodeLlama
- 🌐 Real-time web search integration
- 🎯 Model switcher for easy LLM selection
- 💻 Streamlit-based user-friendly interface

## ⚙️ Prerequisites

Before using this tool, ensure you have:

1. [Ollama](https://ollama.ai) installed locally
2. A valid **Google API Key** and **Custom Search Engine ID**
3. Python 3.8 or higher

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Heavenhood1537/LLMs-Search-Switcher.git
   cd LLMs-Search-Switcher
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Google API credentials:
   ```
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_CSE_ID=your_cse_id_here
   ```

## 🎮 Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Select your preferred LLM from the dropdown menu

4. Start searching and chatting!

## 🔐 Important Notes

- This app does **not include any Google API keys**. You must provide your own.
- All LLM processing is done locally through Ollama
- Web search results are fetched in real-time using Google's API

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Users are responsible for complying with all applicable laws and terms of service when using this software.
