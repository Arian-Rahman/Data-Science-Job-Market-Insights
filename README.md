# 📊 Data Science Job Market Insights

## Overview

Welcome to the Data Science Job Market Insights repository! 🎉 This project dives into the data science job market using data scraped from Indeed.com. We’ve cleaned, analyzed, and visualized the data to uncover insights about job trends, required skills, and salary distributions across the United States.

## Project Components

### 1. Data Collection 🗃️
- Scraped job listings from Indeed.com.
- Collected details like job titles, required skills, salaries, and locations.

### 2. Data Cleaning 🧹
- Processed and cleaned raw data to ensure accuracy.
- Addressed missing values and standardized formats.

### 3. Data Analysis & Visualization 📈
- **Top Skills**: Identified the most in-demand skills for data science positions.
- **Skills by Salary Range**: Analyzed skill requirements across different salary ranges.
- **Salary Distribution**: Visualized how salaries are distributed for data science roles.
- **Job Location Trends**: Mapped the U.S. states with the highest number of on-site job listings.

### 4. Tableau Dashboards 📊
- Created interactive dashboards in Tableau to visualize insights:
  - Top skills required by employers
  - Skill distribution across salary ranges
  - Salary distribution analysis
  - Geographic distribution of on-site job requirements

## Getting Started 🚀

### Prerequisites

- Python (for data scraping and cleaning)
- Tableau (for visualization)
- Required Python libraries: `requests`, `beautifulsoup4`, `pandas`, `numpy`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-science-job-market-insights.git
2. Navigate to the project directory:
   ```bash
   cd data-science-job-market-insights
3. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
### Usage

1. **Data Scraping**:
   - Run `scrape_jobs.py` to collect data from Indeed.

2. **Data Cleaning**:
   - Execute `clean_data.py` to preprocess the data.

3. **Data Analysis & Visualization**:
   - Open Tableau and load `data_science_jobs_analysis.twb` to explore the dashboards.
     
## Files 📂

- `scrape_jobs.py`: Script for scraping data from Indeed.
- `clean_data.py`: Script for cleaning the scraped data.
- `data_science_jobs_analysis.twb`: Tableau workbook with visualizations.
- `requirements.txt`: Python libraries required for the project.


   
