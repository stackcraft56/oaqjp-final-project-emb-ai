
import json
import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    # Convert the JSON response text into a Python dictionary
    response_dict = json.loads(response.text)

    # Extract the emotion scores from Watson's response
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    # Build the dictionary required by IBM
    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"]
    }

    # Identify the emotion with the highest score
    scores["dominant_emotion"] = max(scores, key=scores.get)

    return scores
