import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
import time
import pandas as pd

job_data = []  # List to store job titles
jobs = []
job_header_dict = {}


def main():
    base_url = "https://www.indeed.com/jobs?q=data+science&l=Remote&start="
    for i in range (10,420,10):
        try:
            driver = webdriver.Firefox()
            url = base_url+str(i)
            driver.get(url)
           
            # Wait for job results to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "mosaic-jobResults"))
            )
    
            # Find job result elements
            job_results = driver.find_elements(By.CSS_SELECTOR, 'td.resultContent')
    
            for result in job_results:
                WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.jobsearch-InfoHeaderContainer'))
            )
                job_header = driver.find_element(By.CSS_SELECTOR, 'div.jobsearch-InfoHeaderContainer').text
    
                job_title = result.find_element(By.CSS_SELECTOR, 'h2.jobTitle span[title]').get_attribute('title')
                company_name = result.find_element(By.CSS_SELECTOR, 'span[data-testid="company-name"]').text
                job_links = result.find_elements(By.CSS_SELECTOR, 'h2.jobTitle > a')
    
                for index, job_link in enumerate(job_links):
                    print(f"Clicking on job {index + 1} ")
                    # Create a new skills list for each job
                    job_skills = []
                    education_list = []
                    try:
                        driver.execute_script("arguments[0].click();", job_link)
                        time.sleep(3)  # Wait for the job details to load
    
                        # Check for the skills section and process one skill at a time
                        skills_section = driver.find_element(By.CSS_SELECTOR, "fieldset.js-match-insights-provider-3xemkb")
    
                        # Continue checking and interacting with the skill prompts until no more appear
                        while True:
                            try:
                                # Extract the current skill name
                                skill_element = skills_section.find_element(By.TAG_NAME, "b")
                                skill_name = skill_element.text
                                print(f"Skill found: {skill_name}")
    
                                # Append the skill to the current job's skills list
                                job_skills.append(skill_name)
    
                                # Click "No" to reveal the next skill
                                no_button = skills_section.find_element(By.XPATH, ".//following::button[span[text()='No']]")
                                driver.execute_script("arguments[0].click();", no_button)
    
                            except NoSuchElementException:
                                print("No more skills found for this job.")
                                break
                            except StaleElementReferenceException:
                                print("Stale element reference. Retrying...")
                                break
                        while True :
                            try:
                                education_section = driver.find_element(By.CSS_SELECTOR, "fieldset.js-match-insights-provider-3xemkb")
                                education_element = education_section.find_element(By.TAG_NAME,"b")
                                ed_name = education_element.text
                                print(f"Educational Req found: {ed_name}")
                                education_list.append(ed_name)
                                
                                no_button = skills_section.find_element(By.XPATH, ".//following::button[span[text()='No']]")
                                driver.execute_script("arguments[0].click();", no_button)
    
                            except NoSuchElementException:
                                print("No more skills found for this job.")
                                break
                            except StaleElementReferenceException:
                                print("Stale element reference. Retrying...")
                                break                       
                            
                    except NoSuchElementException as e:
                        print(f"Error: {e}")
    
                    finally:
                        # Append job details and skills to the jobs list
                        # job_header
                        job_header_cleaned = job_header.replace('\n', '@@') 
                        jobs.append({
                            'job_header': job_header_cleaned, 
                            'skills': ', '.join(job_skills),
                            'education_level': ', '.join(education_list)
                        })

    
        finally:
            with open(f'jobs_data.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['job_header', 'skills', 'education_level'])
                writer.writeheader()
                writer.writerows(jobs)
            driver.quit()

if __name__ == "__main__":
    main()
