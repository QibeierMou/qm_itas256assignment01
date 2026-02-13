import json
import os

PROVINCES = {
    "ontario": "ON",
    "british columbia": "BC",
    "quebec": "QC",
    "alberta": "AB",
    "manitoba": "MB",
    "saskatchewan": "SK",
    "nova scotia": "NS",
    "new brunswick": "NB",
    "prince edward island": "PE",
    "newfoundland and labrador": "NL",
    "northwest territories": "NT",
    "nunavut": "NU",
    "yukon": "YT",
}


def normalize_location(location):
    if not location:
        return ""
    
    location = location.strip()
    
    if "," in location:
        city, province = location.split(",")
        city = city.strip().title()
        province = province.strip().lower()
        
        if province in PROVINCES:
            province = PROVINCES[province]
        else:
            province = province.upper()
        
        return f"{city}, {province}"
    
    return location.title()


def normalize_job(job):
    for key in job:
        if isinstance(job[key], str):
            job[key] = " ".join(job[key].split())
            
            if key in ["title", "company"]:
                job[key] = job[key].title()
            
            if key == "location":
                job[key] = normalize_location(job[key])
    
    return job


def make_job_key(job):
    title = job.get("title", "").lower().strip()
    company = job.get("company", "").lower().strip()
    return f"{title}|{company}"


def remove_duplicates(jobs):
    seen = {}
    
    for job in jobs:
        key = make_job_key(job)
        
        if key not in seen:
            seen[key] = job
        else:
            old_count = len([v for v in seen[key].values() if v])
            new_count = len([v for v in job.values() if v])
            
            if new_count > old_count:
                seen[key] = job
    
    return list(seen.values())


def process_jobs(jobbank_jobs, indeed_jobs):
    all_jobs = []
    for job in jobbank_jobs:
        all_jobs.append(normalize_job(job))
    for job in indeed_jobs:
        all_jobs.append(normalize_job(job))
    
    unique_jobs = remove_duplicates(all_jobs)
    
    sorted_jobs = sorted(unique_jobs, key=lambda x: x.get("company", "").lower())
    
    return sorted_jobs


def export_to_json(jobs, output_path="output/canadian_it_jobs.json"):
    if not os.path.exists("output"):
        os.makedirs("output")
    
    with open(output_path, "w") as f:
        json.dump(jobs, f, indent=2)
    
    print(f"Saved {len(jobs)} jobs to {output_path}")