import openai as oa                                                 
oa.api_key = "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"                     

def gpt_request(text_for_gpt):
    retries = 0
    success = False
    while retries <= 5 and success == False:
        try:
            completion = oa.ChatCompletion.create(                              
                model="gpt-3.5-turbo",                                            
                messages=[
                    {"role": "user", "content": "The following text is recorded from a classroom. Take the following text, and make a short resume, summarizing the most important points so that a student could get an idea of what was taught in the classroom. Make sure to format the text nicely, as your response will be put into a DOCS file. Heres the text: " + text_for_gpt}
                ]
            )
            result = completion.choices[0].message.content
            success = True
        except:
            if retries >= 5:
                print("Critical error, ChatGPT API is down, or there is an authentication error with the API key. Stopping program...")
                break
            else:
                retries = retries + 1
                print("Failed to interact with ChatGPT... Retrying for the " + str(retries) + " time...")

    return(result)
