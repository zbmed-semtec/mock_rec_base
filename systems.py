import json
import random
import logging
import jsonlines

logging.basicConfig(level=logging.INFO)

class Recommender(object):

    def __init__(self):
        self.idx = None

    def index(self):
        self.idx = []
        with jsonlines.open('./data/relish_text.jsonl') as reader:
            for obj in reader:
                self.idx.append(obj.get('pmid'))

    def recommend_publications(self, item_id, page, rpp):
        # filename = '../data/relish_recoms.jsonl'

        # recommendations = []

        # # Read the JSONL file
        # with open(filename, 'r') as file:
        #     for line in file:
        #         record = json.loads(line)
        #         # Check if the record matches the target PMID
        #         if record['pmid'] == item_id:
        #             recommendations.append(record)

        # # sorted_recommendations = sorted(recommendations, key=lambda x: (x['target_pmid']))

        # itemlist = [record['target_pmid'] for record in recommendations[:rpp]]
        # print(itemlist)
        # itemlist = recommendations[:rpp]
        # itemlist = random.choices(self.idx, k=rpp)
        itemlist = random.choices(self.idx, k=rpp)
        return {
            'page': page,
            'rpp': rpp,
            'item_id': item_id,
            'itemlist': itemlist,
            'num_found': len(itemlist)
        }