import logging
import json
import azure.functions as func

from .huggingface import HuggingFace

hf = HuggingFace('nlptown/bert-base-multilingual-uncased-sentiment')

# Main entry point 
def entry_point(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    sentence = req.params.get('sentence')
    
    if sentence:
        out = hf.analyze(sentence)
        return func.HttpResponse(json.dumps(out),mimetype="application/json")
    else:
        return func.HttpResponse(json.dumps({
                "error": "This HTTP triggered function executed successfully. Pass a sentence in the query string for a personalized response."
            }),
            status_code=400
        )
