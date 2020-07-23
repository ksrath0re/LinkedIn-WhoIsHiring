from bs4 import BeautifulSoup
import glob
import pandas as pd

hiring_profiles = {}
related_profiles = {}

for file in glob.glob('Files/*'):
    with open(file, 'rb') as fp: # Pass an encoded byte string 'rb' to avoid UnicodeDecodeError
        soup = BeautifulSoup(fp, 'html.parser')
        for li in soup.find_all("li", "pv-browsemap-section__member-container pv-browsemap-section__member-container-line ember-view"):
            for a in li.find_all("a"):
                # print(a.get("href"))
                profile_link = a.get("href")
            for div in li.find_all("div", "pv-browsemap-section__member-detail"):
                for span in div.find_all("span", "name"):
                    # print(span.string)
                    profile_name = span.string
                for p in div.find_all("p", "pv-browsemap-section__member-headline t-14 t-black t-normal"):
                    # print(p.div.string)
                    profile_heading = p.div.string

            if "hiring" in profile_heading.lower() or "hiring" in profile_name.lower():
                hiring_profiles[profile_name] = {}
                hiring_profiles[profile_name]['Profile Link '] = profile_link
                hiring_profiles[profile_name]['Heading '] = profile_heading.strip()
            else:
                related_profiles[profile_name] = {}
                related_profiles[profile_name]['Profile Link '] = profile_link
                related_profiles[profile_name]['Heading '] = profile_heading.strip()

df_hiring = pd.DataFrame.from_dict(hiring_profiles, orient='index') # convert dict to dataframe
df_hiring.to_csv('Hiring profiles.csv')

df_related = pd.DataFrame.from_dict(related_profiles, orient='index') # convert dict to dataframe
df_related.to_csv('Related profiles.csv')