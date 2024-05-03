# StudyBuddy: AI-Powered Learning Platform

## Introduction

**StudyBuddy** is an innovative solution designed to address the challenges faced by learners, educators, and professionals in their pursuit of knowledge acquisition, particularly overcoming limitations in accessing and extracting valuable insights from specific data sources. It harnesses cutting-edge AI to revolutionize how people study by extracting knowledge efficiently from specified data sources like PDFs or URLs, empowering users with valuable insights.


## Installation

To install StudyBuddy, follow these steps:

1. Clone the repository from GitHub.
```
git clone https://github.com/fyxx10/SBuddy.git
```

2. Create a virtual environment.
```
python3 -m venv name_of_virtual_environment
```

3. Activate the virtual environment.
```
source name_of_virtual_environment/bin/activate
```

4. Install the required dependencies.
```
pip install -r requirements.txt
```

5. Create new .env file.
```
cd path/to/your/project
touch .env
```

6. Add openai key to the .env file.
```
OPENAI_API_KEY=your_api_key
```

7. Create new .gitignore file.
```
cd path/to/your/project
touch .gitignore
```

8. Add both virtual environment folder and .env file.
```
.env
name_of_virtual_environment/
```

9. Run the STUDYBUDDY application
```
streamlit run src/HOME.py
```

10. The app will run on port 8501
```
http://localhost:8501
```

## Usage

To use StudyBuddy:

1. Run **STUDYBUDDY** locally on **localhost:8501** or on a deployed web-based version.
2. Upload PDFs or Enter a URL to interact with the intelligent study assistant.
3. Receive instant and accurate answers to your study queries.

## Features

StudyBuddy offers the following key features:

- **Ask Questions**: Get instant answers to your queries.
- **Summarize and Simplify**: Simplify complex materials for easier understanding.
- **Translation**: Break language barriers and access content in your preferred language.
- **Search Without Keywords**: Explore documents and web content effortlessly.
- **Generate Questions**: Enhance study sessions with automatic question generation.

## Use Cases

StudyBuddy is designed to assist you in various study-related tasks, including:

- **Books**: Dive into books and extract key information quickly.
- **Textbooks**: Simplify complex textbook content for better comprehension.
- **Lecture Notes**: Summarize and organize lecture notes for efficient revision.
- **Research Papers**: Extract key findings and insights from research papers.
- **Articles**: Summarize articles and extract important information.
- **Financial Documents**: Analyze financial documents and extract relevant data.
- **Legal Documents**: Summarize legal documents and extract key points.
- **Instruction Manuals**: Simplify complex instructions and procedures.
- **Resumes**: Analyze resumes and extract key qualifications and skills.

### Note:
StudyBuddy can perform efficiently with any PDF containing text content, as well as with any website URL containing text content. Whether it's extracting key information from documents or summarizing web articles, StudyBuddy is your reliable study companion!

## Limitations

While StudyBuddy offers powerful features for collaborative learning, it currently has some limitations:

- **PDF parsing constraints:** StudyBuddy's PDF parsing functionality may encounter difficulties with encrypted PDFs.

- **Limited File Type Support:** StudyBuddy currently only supports PDF files for knowledge extraction. Other popular file types such as docx, txt, and md are not supported.
  
- **Data Source Citation:** StudyBuddy does not automatically cite the source of data extracted from uploaded files or URLs.
  
- **Buggy Multipage Execution:** Occasionally, StudyBuddy may encounter issues with multipage execution, requiring the cache to be cleared before switching pages to ensure proper functionality.
  
- **Transient Vector Database:** The vector database used by StudyBuddy currently does not persist, resulting in uploaded files and chat history not being saved between sessions. Uploaded files and URL chat history persist temporarily in the cache but are deleted upon app reload.
  
- **Limited Chat Session Features:** Currently, StudyBuddy does not offer the option to create a new chat session or view the history of different chat sessions. All chat history is stored temporarily and may be lost upon app reload.

We are continuously working to address these limitations and improve the StudyBuddy experience for our users.


## License

StudyBuddy is licensed under the MIT License.


## Acknowledgements

We would like to acknowledge the following:

- OpenAI for providing the powerful models used in StudyBuddy.
- Streamlit for enabling easy deployment of web applications.
- Langchain for the framework making this project possible.
- Special thanks to team members from CodeCraftCrew for contributing:
  - Felix Nunoo
  - Etornam Klu
  - Jojo Saka

## Contact Information

For questions or support, please reach out to either:
- [felixnunoo9@gmail.com](felixnunoo9@gmail.com)
- [03etornam@gmail.com](03etornam@gmail.com)
- [sakajojo8@gmail.com](sakajojo8@gmail.com)

Visit STUDYBUDDY app: [chatbuddy.streamlit.app](https://chatbuddy.streamlit.app)


