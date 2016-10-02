import os,json
from watson_developer_cloud import ToneAnalyzerV3

def analyze_tone(text):
	tone_analyzer = ToneAnalyzerV3(
	   username=os.environ.get('IBM_USERNAME', None),
	   password=os.environ.get('IBM_PASSWORD', None),
	   version='2016-05-19')

	print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))
    # print json.dumps(tone_analyzer.tone(text=text, indent=2))
 
def welcome():
    message = "Welcome to the IBM Watson Tone Analyzer\n"
    print(message + "-" * len(message) + "\n")
    message = "How it works"
    print(message)
    message = "Perhaps a bit too aggressive in your emails? Are your blog posts a little too friendly? Tone Analyzer might be able to help. The service uses linguistic analysis to detect and interpret emotional, social, and writing cues found in text."
    print(message)
    print()
    print("Have fun!\n")
 
def display_results(data):
    data = json.loads(str(data))
    print(data)
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print()
 
def main():
    welcome()
     
    data = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        results = analyze_tone(data)
        if results != False:
            display_results(results)
            exit
        else:
            print("Something went wrong")

main()