# Our OpenAI API Key: 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

import openai as oa                                                 # Import the OpenAI Library
oa.api_key = "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"  # Set our OpenAI API key

gpt_request = "This text is what we ask ChatGPT"                    # Content needs to be fetched from the speech to text algorithm. Can be a text file, or whatever else, as long as its plain text.

completion = oa.ChatCompletion.create(                              # Creating an instance of the ChatCompletion class
  model="gpt-3.5-turbo",                                            # Using the GPT 3.5 model
  messages=[
    {"role": "user", "content": gpt_request}                        # Feeding ChatGPT the request
  ]
)

result = completion.choices[0].message.content                      # Storing our result from ChatGPT in a variable.

print(result)