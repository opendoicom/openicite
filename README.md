## Home Page
https://github.com/opendoicom/openicite/


## Dependencies
- **requests**



## Useage

### **Installation**
```bash
pip install requests openicite
```

### **Example**

**/api/pubs/{pmid}**

```python
from openicite import Openicite

icite = Openicite()

# get_icite
pmid = 23333
data = icite.get_icite(pmid)
print(data)
```

data

```json
{
    "meta": {
        "pmids": "23456789,27599104"
    },
    "links": {
        "self": "https://icite.od.nih.gov/api/pubs?pmids=23456789%2C27599104"
    },
    "data": [
        {
            "pmid": 23456789,
            "year": 2013,
            "title": "Hospital volume is associated with survival but not multimodality therapy in Medicare patients with advanced head and neck cancer.",
            "authors": "Arun Sharma, Stephen M Schwartz, Eduardo Méndez",
            "journal": "Cancer",
            "is_research_article": "Yes",
            "relative_citation_ratio": 1.78,
            "nih_percentile": 71,
            "human": 1,
            "animal": 0,
            "molecular_cellular": 0,
            "apt": 0.75,
            "is_clinical": "No",
            "citation_count": 46,
            "citations_per_year": 4.181818181818182,
            "expected_citations_per_year": 2.3475706996041663,
            "field_citation_rate": 5.383290487847182,
            "provisional": "No",
            "x_coord": 0,
            "y_coord": 1,
            "cited_by_clin": [
                25488965,
                29180076
            ],
            "cited_by": [ ],
            "references": [ ],
            "doi": "10.1002/cncr.27976",
            "last_modified": "02/25/2024, 09:52:59"
        },
        {
            "pmid": 27599104,
            "year": 2016,
            "title": "Relative Citation Ratio (RCR): A New Metric That Uses Citation Rates to Measure Influence at the Article Level.",
            "authors": "B Ian Hutchins, Xin Yuan, James M Anderson, George M Santangelo",
            "journal": "PLoS Biol",
            "is_research_article": "Yes",
            "relative_citation_ratio": 9.87,
            "nih_percentile": 97.9,
            "human": 1,
            "animal": 0,
            "molecular_cellular": 0,
            "apt": 0.75,
            "is_clinical": "No",
            "citation_count": 222,
            "citations_per_year": 27.75,
            "expected_citations_per_year": 2.8120842223332287,
            "field_citation_rate": 6.375837754422565,
            "provisional": "No",
            "x_coord": 0,
            "y_coord": 1,
            "cited_by_clin": [
                37552823,
                33539992
            ],
            "cited_by": [ ],
            "references": [ ],
            "doi": "10.1371/journal.pbio.1002541",
            "last_modified": "02/25/2024, 09:21:50"
        }
    ]
}
```



**/api/pubs?pmids={pmid1,pmid2...}**

```python
# get_icites
pmid_list = [str(pmid) for pmid in range(2024)]  # 示例: 生成一个超过1000个PMID的列表
field_list = ['pmid', 'year', 'title', 'apt', 'relative_citation_ratio', 'cited_by_clin']
data = icite.get_icites(pmid_list=pmid_list, field_list=field_list)
print(data)
```

data

```json
{
    'meta': 
    {
        'pmids': '31461780,22882545,20050301',
        'fl': 'pmid,year,title,apt,relative_citation_ratio,cited_by_clin'
    },
    'data': [
        {
            'pmid': 22882545,
            'year': 2013,
            'title': 'Killer whale ecotypes: is there a global model?',
            'apt': 0.05,
            'relative_citation_ratio': 1.46,
            'cited_by_clin': None
        },
        {
            'pmid': 31461780,
            'year': 2020,
            'title': 'Enigmatic megafauna: type D killer whale in the Southern Ocean.',
            'apt': 0.05,
            'relative_citation_ratio': 0.16,
            'cited_by_clin': None
        },
        {
            'pmid': 20050301,
            'year': 2009,
            'title': 'Ecological, morphological and genetic divergence of sympatric North Atlantic killer whale populations.',
            'apt': 0.05,
            'relative_citation_ratio': 1.78,
            'cited_by_clin': None
        }
    ]
}
```



## Refs

### Request parameters

- `pmids`: only return publications with the given PubMed IDs. Separate multiple IDs with commas to request up to 1000 at a time. If this parameter is provided, all other parameters are ignored.
- `fl`: only return publications with the given fields. Separate multiple fields with commas (no space). Field names are very specific and listed in Response example below. No fl param will return all fields.



### Data keys

- **pmid**: PubMed Identifier, an article ID as assigned in PubMed by the National Library of Medicine
- **doi**: Digital Object Identifier, if available
- **year**: Year the article was published
- **title**: Title of the article
- **authors**: List of author names
- **journal**: Journal name (ISO abbreviation)
- **cited_by**: PMIDs of articles that have cited this one.
- **references**: PMIDs of articles in this article's reference list.
- **is_research_article**: Flag indicating whether the Publication Type tags for this article are consistent with that of a primary research article
- **relative_citation_ratio**: Relative Citation Ratio (RCR)--OPA's metric of scientific influence. Field-adjusted, time-adjusted and benchmarked against NIH-funded papers. The median RCR for NIH funded papers in any field is 1.0. An RCR of 2.0 means a paper is receiving twice as many citations per year than the median NIH funded paper in its field and year, while an RCR of 0.5 means that it is receiving half as many citations per year. Calculation details are documented in Hutchins et al., PLoS Biol. 2016;14(9):e1002541.
- **provisional**: RCRs for papers published in the previous two years are flagged as "provisional", to reflect that citation metrics for newer articles are not necessarily as stable as they are for older articles. Provisional RCRs are provided for papers published previous year, if they have received with 5 citations or more, despite being, in many cases, less than a year old. All papers published the year before the previous year receive provisional RCRs. The current year is considered to be the NIH Fiscal Year which starts in October. For example, in July 2019 (NIH Fiscal Year 2019), papers from 2018 receive provisional RCRs if they have 5 citations or more, and all papers from 2017 receive provisional RCRs. In October 2019, at the start of NIH Fiscal Year 2020, papers from 2019 receive provisional RCRs if they have 5 citations or more and all papers from 2018 receive provisional RCRs.
- **citation_count**: Number of unique articles that have cited this one
- **citations_per_year**: Citations per year that this article has received since its publication. If this appeared as a preprint and a published article, the year from the published version is used as the primary publication date. This is the numerator for the Relative Citation Ratio.
- **field_citation_rate**: Measure of the intrinsic citation rate of this paper's field, estimated using its co-citation network.
- **expected_citations_per_year**: Citations per year that NIH-funded articles, with the same Field Citation Rate and published in the same year as this paper, receive. This is the denominator for the Relative Citation Ratio.
- **nih_percentile**: Percentile rank of this paper's RCR compared to all NIH publications. For example, 95% indicates that this paper's RCR is higher than 95% of all NIH funded publications.
- human: Fraction of MeSH terms that are in the Human category (out of this article's MeSH terms that fall into the Human, Animal, or Molecular/Cellular Biology categories)
- animal: Fraction of MeSH terms that are in the Animal category (out of this article's MeSH terms that fall into the Human, Animal, or Molecular/Cellular Biology categories)
- molecular_cellular: Fraction of MeSH terms that are in the Molecular/Cellular Biology category (out of this article's MeSH terms that fall into the Human, Animal, or Molecular/Cellular Biology categories)
- x_coord: X coordinate of the article on the Triangle of Biomedicine

- y_coord: Y Coordinate of the article on the Triangle of Biomedicine
- is_clinical: Flag indicating that this paper meets the definition of a clinical article.
- cited_by_clin: PMIDs of clinical articles that this article has been cited by.
- apt: Approximate Potential to Translate is a machine learning-based estimate of the likelihood that this publication will be cited in later clinical trials or guidelines. Calculation details are documented in Hutchins et al., PLoS Biol. 2019;17(10):e3000416.

> [iCite | API | NIH Office of Portfolio Analysis](https://icite.od.nih.gov/api)
>
> [iCite Database Snapshots (NIH Open Citation Collection) (figshare.com)](https://nih.figshare.com/collections/iCite_Database_Snapshots_NIH_Open_Citation_Collection_/4586573)



