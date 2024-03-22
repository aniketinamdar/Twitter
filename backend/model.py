from dotenv import load_dotenv

load_dotenv()

import os
import io
import base64
import google.generativeai as genai


genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def get_analaysis_prompt(tweet):
    analysis_prompt = f"I want you to analyze a tweet.  it should do a sentiment analysis. it includes 3 parts. one is categorizer, identify whether tweet is an example of cyberbullying, hate speech, crime/threat/slogan. second part in sentiment checker is intensity calculator on the scale of 1-10 where 1 is less intense and 10 is more intense. third part is a credible source checker,  if it is a news, whether it is a fake news or true news. also try to identify whether the tweet given is from a bot account or not. give an output where each label is given an answer and in the end a small analysis is given. The tweet is as follow - {tweet}"
    return analysis_prompt

def get_analysis(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])
    return response.text

