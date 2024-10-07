# DND Project

## Overview
The **DND Project** is an AI-driven modular system designed to handle a variety of tasks, self-learn from failures, and improve over time. The system can:
- Manage tasks like stock analysis and prediction.
- Search for solutions online and generate new tools if it encounters a failure.
- Continuously learn and upgrade itself for better performance.

The system is designed in a **modular** fashion, making it easy to extend and scale.

## Key Features
- **Task Management**: Accepts and executes a wide range of tasks using a modular structure.
- **Failure Handling**: Automatically searches the web for solutions when tasks fail and generates new tools/code.
- **Self-Learning**: Learns from failures and upgrades its knowledge base.
- **Stock Prediction**: Can predict stock market trends and visualize data based on previous performance.
- **Modular Design**: Easily extendable system with separate modules for PDF reading, web searching, Chrome interaction, etc.

## Folder Structure
The project is structured as follows:

DND_Project/
│

├── main.py                                  # Core DND logic and workflow management
│

├── Modules/                                 # Contains all modules for task execution and self-learning
│   ├── task_manager.py                      # Manages tasks and assigns them to specific modules
│   ├── failure_handler.py                   # Handles task failures and solution discovery
│   ├── tool_maker.py                        # Generates and updates tools as needed
│   ├── code_upgrader.py                     # Updates system code and generates new tools/files

│   ├── knowledge_base.py                    # Manages storage of learned solutions/tools

│   ├── self_learning.py                     # AI module for self-learning and improvement

│   └── memory_manager.py                    # Manages common memory for storing knowledge (SQL)

│

├── Tools/                                   # Contains specific tools required for various tasks

│   ├── pdf_reader.py                        # Reads and analyzes PDFs

│   ├── websearch.py                         # Searches the web for information, tutorials, etc.

│   ├── chrome.py                            # Controls and interacts with websites via Google Chrome

│   ├── installer.py                         # Manages installation of new tools or packages

│   ├── agent.py                             # Manages multi-agent creation and task distribution

│
├── Stock_Analyzer/                          # Stock market analysis modules for prediction and research

│   ├── Stock_analyzer.py                    # Main module for managing stock analysis workflows

│   ├── select_sector/                       # Sector-based stock analysis

│   │   ├── news_researcher.py               # Collects news and sentiment data for sector analysis

│   │   ├── data_engineer.py                 # Collects historical data and filters companies

│   │   ├── data_scientist.py                # Predicts top stocks with >80% probability

│   │   ├── frontend_developer.py            # Creates stock prediction visualizations

│   │   ├── backend_developer.py             # Manages alert conditions for predictions

│   │   └── quantitative_analyst.py          # Performs risk analysis for the selected stocks

│   │

│   ├── select_company/                      # Company-specific stock analysis

│   │   ├── news_researcher.py               # Gathers company-related news and sentiment

│   │   ├── data_engineer.py                 # Collects historical stock data for the company

│   │   ├── data_scientist.py                # Predicts stock movement for a specific company

│   │   ├── frontend_developer.py            # Visualizes stock predictions for the company

│   │   ├── backend_developer.py             # Manages alert conditions

│   │   └── quantitative_analyst.py          # Conducts risk analysis for the company

│   │

│   ├── overall_next_day/                    # Overall stock prediction for the next day

│   │   ├── news_researcher.py               # Gathers top company news and sentiment

│   │   ├── data_engineer.py                 # Selects top companies based on financial metrics

│   │   ├── data_scientist.py                # Predicts top 5 stocks for the next day

│   │   ├── frontend_developer.py            # Creates visualizations of the stock trends

│   │   ├── backend_developer.py             # Manages alerts for next day stock movement

│   │   └── quantitative_analyst.py          # Performs risk analysis for overall market predictions

│   │

│   ├── ipo/                                 # IPO-specific stock analysis

│   │   ├── news_researcher.py               # Collects news and sentiment about upcoming IPOs

│   │   ├── data_engineer.py                 # Gathers historical IPO data and metrics

│   │   ├── data_scientist.py                # Predicts stock movement after IPO

│   │   ├── frontend_developer.py            # Visualizes IPO-related trends and predictions

│   │   ├── backend_developer.py             # Sets up alerts for IPO stock movements

│   │   └── quantitative_analyst.py          # Performs risk analysis for IPOs

│   │

│   ├── historical/                          # Historical stock data analysis

│   │   ├── data_scientist.py                # Performs feature engineering and ratings based on data

│   │   ├── frontend_developer.py            # Visualizes historical stock performance and predictions

│   │   ├── backend_developer.py             # Manages alert conditions based on historical data

│   │   └── quantitative_analyst.py          # Conducts risk analysis for historical data trends

│

├── Common_Memory/                           # Common memory storage and handling

│   ├── common_memory.sql                    # SQL database for storing shared knowledge

│   ├── memory_handler.py                    # Manages retrieval and storage of knowledge

│

├── Websearch_Support/                       # Supporting modules for web searches

│   ├── search_scraper.py                    # Scrapes web search results (tutorials, code snippets)

│   ├── content_analyzer.py                  # Analyzes the scraped web content

│

├── Self_Modification/                       # Modules for self-modification and system upgrades

│   ├── upgrade_manager.py                   # Manages system versioning and self-upgrades

│   ├── tool_installer.py                    # Installs necessary tools or packages

│

├── Config/                                  # Configuration files for API keys, dependencies, and settings

│   ├── .env                                 # API keys and configurations (OpenAI, web scraping, etc.)

│   ├── config.py                            # Main configuration file for project settings

│

├── input/                                   # Input files (PDFs, data files)

│   ├── pdfs/                                # PDF files for analysis by pdf_reader.py

│   ├── data_files/                          # External datasets for stock analysis

│

├── output/                                  # Output files and logs generated by the system

│   ├── logs/                                # Logs of system activity and task execution

│   ├── reports/                             # Reports generated from stock analysis or other tasks

│

├── requirements.txt                         # Python dependencies required for the project

├── README.md                                # Documentation for the DND project

└── License                                  # License information for the project




## Installation
1. **Clone the Repository**:
```bash
   git clone ##https://github.com/your-username/DND_Project.git
  ```

 ```bash
   cd DND_Project
  ```

2. **Set up a virtual environment (optional but recommended):**

```bash
   python -m venv DND3
```
3. **Activate virtual environment**


* On Linux use 

```bash
   source venv/bin/activate
```
   
* On Windows use 

```bash
   DND4\Scripts\activate
``` 


* On Windows use If you encounter an error regarding execution policies, you can temporarily bypass it by running:
```bash
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```


4.  **Install Dependencies: Ensure you have Python 3.8+ installed. Install the required dependencies by running:**

```bash
    pip install -r requirements.txt
```
5.  **Set Up Environment Variables: Create a .env file in the Config/ folder and add your API keys (e.g., OpenAI):**

```bash
OPENAI_API_KEY=your_openai_api_key
```


6. **Run the DND System: Start the system by running:**

```bash
python main.py
```
**Usage**
The system will ask for a task. Enter a task such as:

"Analyze stock trends for tomorrow."
"Get company financial data."
"Read PDF report and summarize."
If the task fails, the system will search the web for solutions, generate new tools, and attempt the task again.

**Contributing**
If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. We welcome improvements and new ideas!
