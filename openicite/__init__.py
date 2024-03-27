import requests
import time

class Openicite():
    BASE_URL = "https://icite.od.nih.gov/api"

    def __init__(self):
        """Initialize the client."""        
        self.api_url = f'{self.BASE_URL}/pubs'
        self.MAX_PMIDS_PER_REQUEST = 1000
        self.sleep = 0.05
    
    def get_icite(self, pmid, timeout=500):
        """
        Send a request to the specified URL for a single PMID.
        Example URL: https://icite.od.nih.gov/api/pubs/23456789
        --------------------------------------------------------
        Parameters:
            pmid: PubMed ID for the publication,
            timeout: Timeout for the request, default is 500 seconds.
        Returns:
        A JSON object with publication data if successful, None otherwise.
        """
        single_url = f'{self.api_url}/{pmid}'
        try:
            response = requests.get(single_url, timeout=timeout)
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    
    def get_icites(self, pmid_list=[], field_list=[], timeout=500):
        """
        Fetches publication data in bulk. If pmid_list exceeds 1000, it splits the requests and merges the results.
        Parameters:
            pmid_list: List of PMIDs,
            field_list: List of fields to be fetched,
            timeout: Timeout for the request, default is 500 seconds.
        Returns:
        A JSON object containing merged results of the requests.
        """
        MAX_PMIDS_PER_REQUEST = self.MAX_PMIDS_PER_REQUEST  # Maximum number of PMIDs per request
        responses_data = []  # To store response data from all batches

        # Split pmid_list into sublists of up to 1000 PMIDs each
        for i in range(0, len(pmid_list), MAX_PMIDS_PER_REQUEST):
            time.sleep(self.sleep)
            sub_pmid_list = pmid_list[i:i + MAX_PMIDS_PER_REQUEST]
            payload = {
                'pmids': ','.join(map(str, sub_pmid_list)),
                'fl': ','.join(field_list)
            }

            try:
                response = requests.get(self.api_url, params=payload, timeout=timeout)
                if response.status_code == 200:
                    # Add this batch's results to the list of response data
                    responses_data.extend(response.json().get('data', []))
                else:
                    response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                return None

        # Merge results from all batches and return
        return {
            'meta': {
                'pmids': ','.join(map(str, pmid_list)),
                'fl': ','.join(field_list)
            },
            'data': responses_data
        }


if __name__ == "__main__":
    
    icite = Openicite()

    # get_icite
    pmid = 23333
    data = icite.get_icite(pmid)
    print(data)
    
    # get_icites
    pmid_list = [str(pmid) for pmid in range(2024)]  # 示例: 生成一个超过1000个PMID的列表
    field_list = ['pmid', 'year', 'title', 'apt', 'relative_citation_ratio', 'cited_by_clin']
    data = icite.get_icites(pmid_list=pmid_list, field_list=field_list)
    print(data)