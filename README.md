# 📊 Data Science Job Market Insights

## Overview

Welcome to the Data Science Job Market Insights repository! 🎉 This project dives into the data science job market using data scraped from Indeed.com. We’ve cleaned, analyzed, and visualized the data to uncover insights about job trends, required skills, and salary distributions across the United States.

![Main Dashboard](https://github.com/user-attachments/assets/69b555d0-cb79-4583-a049-5e6fc05fef8b)


## Project Components

### 1. Data Collection 🗃️
- Scraped Data Science job listings from Indeed.com.
- Collected details like job titles, required skills, salaries,education required and locations and more.

### 2. Data Cleaning 🧹
- Processed and cleaned raw data collected by scraping .
- Perfromed Data engineering by extracting and creating new formatted data columns .

### 3. Tableau Dashboards 📊
- Created interactive dashboards in Tableau to visualize insights:
  - Top skills required by top employers
  - Skill distribution across salary ranges
  - Salary distribution analysis
  - Education Level demand 
  - Geographic distribution of on-site job requirements
  - [Dashboard](https://public.tableau.com/views/DataScienceJobVizfromIndeed_com/Dashboard1?:language=en-US&publish=yes&:sid=6F51DA7D92EF4481982A5A7A5FF73F18-0:0&:redirect=auth&:display_count=n&:origin=viz_share_link)
    

## Getting Started 🚀

### Prerequisites

- Python 
- Tableau (for visualization)
- Google Colab / Jupyter Notebook
- Visual Studio Code or any python compiler of choice 
- Required Python libraries: `selenium`, `pandas`, `numpy`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Arian-Rahman/Data-Science-Job-Market-Insights.git
2. Navigate to the project directory:
   ```bash
   cd data-science-job-market-insights
3. Create virtual env (windows)
   ```bash
   python -m venv envDsInsights
4. Activate the new env
   ```bash
   .\envDsInsights\Scripts\activate

5. Install required Python libraries:
   ```bash
   pip install -r requirements.txt

### Usage

1. **Data Scraping**:
   - Run `scrap_v4.01.py` to collect data from Indeed.com .

2. **Data Cleaning**:
   - Run `Final_P01.03_data_cleaning.ipynb` on Colab or Jupyter Notebook for data cleaning.

3. **Data Analysis & Visualization**:
   - Open Tableau and load `Data Science Job Viz from Indeed.com.twbx` to explore the dashboard.
   -Click on the data section and import the data from data folder 
     




   
