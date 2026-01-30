from serpapi import GoogleSearch
import pandas as pd


def get_data_step_by_step():
    params = {
        "engine": "google_maps",
        "q": "Agences immobilières à Lyon",
        "api_key": "YOUR_API_KEY"
    }

    print("[*] Connecting to Google Maps via API...")

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        if "local_results" in results:
            data = results["local_results"]
            print(f"[+] Success! Found {len(data)} agencies.")

            final_results = []
            for item in data:
                final_results.append({
                    "Name": item.get("title"),
                    "Address": item.get("address"),
                    "Phone": item.get("phone", "N/A"),
                    "Rating": item.get("rating", "N/A"),
                    "Website": item.get("website", "N/A")
                })

            df = pd.DataFrame(final_results)
            df.to_csv("Lyon_Agencies_Portfolio.csv", index=False, encoding='utf-8-sig')
            print("\n[!!!] MABROUK! Check your folder for 'Lyon_Agencies_Official.xlsx'")
        else:
            print("[-] No results found. Double check your query.")

    except Exception as e:
        print(f"[-] An error occurred: {e}")


if __name__ == "__main__":

    get_data_step_by_step()

