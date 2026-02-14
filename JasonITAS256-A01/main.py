from parser import parse_jobbank_jobs, parse_indeed_jobs
from scraper import scrape_site
from processor import process_jobs, export_to_json


def main():
    jobbank_url = "https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=IT&locationstring=Canada"
    indeed_url = "https://ca.indeed.com/jobs?q=IT&l=Canada"

    jobbank_jobs = scrape_site(jobbank_url, parse_jobbank_jobs, "Job Bank Canada")
    indeed_jobs = scrape_site(indeed_url, parse_indeed_jobs, "Indeed")

    processed_jobs = process_jobs(jobbank_jobs, indeed_jobs)

    export_to_json(processed_jobs)

    print(f"\nTotal jobs collected: {len(processed_jobs)}")
    print("This is for educational purposes only.")
    print("This is a assigment for ITAS256 at Vancouver Island University.")
    print("Student: Jason Mou")


if __name__ == "__main__":
    main()