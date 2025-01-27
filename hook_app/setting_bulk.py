from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

es.indices.create(
	index='dictionary',
	body={
		"settings":{
			"index":{
				"analysis":{
					"analyzer":{
						"my_analyzer":{
							"type":"custom",
							"tokenizer":"nori_tokenizer"
						}
					}
				}
			}
		},
		"mappings":{
			"ratings_train":{
				"properties":{
					"id":{
						"type":"long"
					},
					"title":{
						"type":"text",
						"analyzer":"my_analyzer"
					},
					"content":{
						"type":"text",
						"analyzer":"my_analyzer"
					}
				}
			}
		}
	}
)

with open("train_docs.json",encoding='utf-8') as json_file:
	json_data = json.loads(json_file.read())

bdoy=""

for i in json_data:
	body = body + json.dumps({"index": {"_index": "dictionary", "_type": "dictionary_datas"}}) + '\n'
    body = body + json.dumps(i, ensure_ascii=False) + '\n'

es.bulk(body)