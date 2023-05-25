# Our OpenAI API Key: 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

import openai as oa                                                 
oa.api_key = "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"                     

def gpt_request(text_for_gpt):
    try:
        completion = oa.ChatCompletion.create(                              
            model="gpt-3.5-turbo",                                            
            messages=[
                {"role": "user", "content": "The following text is recorded from a classroom. Take the following text, and make a short resume, summarizing the most important points so that a student could get an idea of what was taught in the classroom: " + text_for_gpt}
            ]
        )
        result = completion.choices[0].message.content
    except:
        print("Failed to interact with ChatGPT...")
    
    return(result)