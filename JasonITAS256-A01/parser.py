from bs4 import BeautifulSoup

def parse_jobbank_jobs(soup, max_jobs=15):
    jobs = []

    job_cards = soup.find_all('article', class_='resultJobItem')[:max_jobs]

    for card in job_cards:
        title_tag = card.find("a", class_="resultJobItemTitle")
        company_tag = card.find("div", class_="employerName")
        location_tag = card.find("div", class_="location")

        job = {
            "title": title_tag.get_text(strip=True) if title_tag else"",
            "company": company_tag.get_text(strip=True) if company_tag else"",
            "location": location_tag.get_text(strip=True) if location_tag else"",
            "source": "Job Bank Canada"
        }
        jobs.append(job)
    return jobs 


def parse_indeed_jobs(soup, max_jobs=15):
    jobs = []

    job_cards = soup.find_all("div", class_="job_seen_beacon")[:max_jobs]

    for card in job_cards:
        title_tag = card.find("h2", class_="jobTitle")
        company_tag = card.find("span", class_="companyName")
        location_tag = card.find("div", class_="companyLocation")

        job = {
            "title": title_tag.get_text(strip=True) if title_tag else "",
            "company": company_tag.get_text(strip=True) if company_tag else "",
            "location": location_tag.get_text(strip=True) if location_tag else "",
            "source": "Indeed"
        }

        jobs.append(job)

    return jobs