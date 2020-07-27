# Chapter:sp20-516-251,Shihui Jiang

## Google Cloud Natural Language 


### Instroduction 

Natural language processing(NPL) is the combination of machine learning and
linguistics. It has become one of the most popular tool and has been used in
all areas of our life[sp-20-251-NPLGoogleCloud].  Natural language uses machine learning to reveal the
structure and meaning of text.You can extract information about people
places, and events, and better understand social media sentiment and customer
conversations. Natural language enables your to analyze text and also
integrate it with your document storage on Cloud Storage.

![](images/natural_language_method.jpg){#fig:Google-Cloud-Natural-Language-Method}

### Services

Google cloud natural language includes two product: AutoML Natural Language and 
Natural language APL. Each product comprises different services to support 
different purpose. 


AutoML Natural Language: Integrated REST API, Custom entity extraction, custom 
content classification, customer models, powered by Google's AutoML models,
spatial structure understanding and Large dataset support.
Natural language API: Integrated REST API, syntax analysis, entity analysis, 
sentiment analysis, content classification, Multi-language


### Natural Language API 


This chapter will focus on Google Natural Language API. 

Natual Language API is an easy to use interface to a set of powerful NLP
 models which have been pre-trained by google to perform various task. 


### Set up and requirements: 

1. Create project on google cloud platform console 
2. Enable the Cloud Natural Language API 
3. Activate Cloud Shell 
4. Create an API Key 

### Natural Language Method 

1. Syntax Analysis: Extract tokens and sentences
2. Sentiment Analysis: Understand the overall sentiment expressed in a block of text
3. Entity Analysis: Identify entities such as person,location,events,products,etc
4. Entity Sentiment Analysis: predicts the sentiment expressed about individual
entity in the text
5. Text Classification:structure textual data 

Following Example shows how to use `analyzeEntities` to extract 
information from a text. 

>Indiana University Bloomington is a public research university in Bloomington
, Indiana.It is the flagship institution of the Indiana University system and
, with over 40,000 students, its largest university

Request 

~~~
curl "https://language.googleapis.com/v1/documents:analyzeEntities?key=${API_Key}" -s -X POST -H "Content-Type:application/json" --data-binary @entityanalysisexample.json
~~~

Response

~~~
{
  "entities": [
    {
      "name": "Indiana University Bloomington",
      "type": "ORGANIZATION",
      "metadata": {
        "mid": "/m/01qrb2",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Indiana_University_Bloomington"
      },
      "salience": 1,
      "mentions": [
        {
          "text": {
            "content": "Indiana University Bloomington",
            "beginOffset": 0
          },
          "type": "PROPER"
        },
        {
          "text": {
            "content": "research university",
            "beginOffset": 43
          },
          "type": "COMMON"
        }
      ]
    }
  ],
  "language": "en"
}

~~~



### Cost of Google Natual Language API 

![](images/natural_language_service_cost.jpg){#fig:Google-Cloud-Natural-Language-API-Service-Cost}





