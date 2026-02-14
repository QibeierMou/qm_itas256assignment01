from bs4 import BeautifulSoup

def parse_jobbank_jobs(soup, max_jobs=15):

    jobs = []

    cards = soup.find_all("a", class_="resultJobItem")

    for card in cards[:max_jobs]:

        title_tag = card.find("span", class_="noctitle")
        title = title_tag.text.strip() if title_tag else ""

        company_tag = card.find("li", class_="business")
        company = company_tag.text.strip() if company_tag else ""

        location_tag = card.find("li", class_="location")
        location = location_tag.text.strip() if location_tag else ""

        job = {
            "title": title,
            "company": company,
            "location": location,
            "source": "Job Bank"
        }

        jobs.append(job)

    print("Job Bank jobs found:", len(jobs))
    return jobs


def parse_indeed_jobs(soup, max_jobs=15):
    jobs = []

    job_cards = soup.find_all("td", class_="resultContent")

    for card in job_cards[:max_jobs]:
        title_tag = card.find("h2", class_="jobTitle")
        title = title_tag.get_text(strip=True) if title_tag else ""

        company_tag = card.find("div", class_="company-Name")
        company = company_tag.get_text(strip=True) if company_tag else ""
        location_tag = card.find("div", class_="text-Location")
        location = location_tag.get_text(strip=True) if location_tag else ""

        job = {
            "title": title,
            "company": company,
            "location": location,
            "source": "Indeed"
        }

        jobs.append(job)

    print("Indeed jobs found:", len(jobs))
    return jobs