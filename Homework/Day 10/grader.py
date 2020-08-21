import requests
import pickle
import pandas
import numpy as np

user_id = open('/home/admin_/nimblebox-comput-server/user.txt').read()

def grader_1(accuracy):
    try:
        file = open('check.pkl', 'rb')
        data = pickle.load(file)
        file.close()
        mean_accuracy = np.mean(accuracy)
        grade=0
        if(mean_accuracy >= data):
            grade=100
        data = {
            "username": user_id,
            "question_id": "HW7_1",
            "grade": grade
            }
        requests.post("http://10.140.0.92/upload_result", json=data)
    except:
        return "Answer is not in format as specified in the question"
    return "Homework has been submitted successfully"