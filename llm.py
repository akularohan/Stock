from huggingface_hub import InferenceClient
# from llama_index.legacy.llms.huggingface import HuggingFaceInferenceAPI
from llama_index.llms.groq import Groq
from llama_index.llms.huggingface import HuggingFaceLLM
# from llama_index.llms.huggingface import HuggingFaceInferenceAPI
from llama_index.embeddings.huggingface import HuggingFaceInferenceAPIEmbedding
# from llama_index.llms.huggingface import HuggingFaceInferenceAPI
# from llama_index.i import HuggingFaceInferenceAPI
from huggingface_hub import InferenceClient
# from llama_index.llms import 



huggingfacetoken="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"
llamahf="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"
groq_key="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"
groq_model = "llama3-70b-8192"

groq_llm = Groq(model="llama3-70b-8192", api_key=groq_key)

# print(groq_llm)



embed_url ="https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
inference_url="https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"

embedding_model = HuggingFaceInferenceAPIEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2",
                               headers = {"Authorization": "Bearer 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"})

# print(embedding_model)

# inference_model =HuggingFaceInferenceAPI(model_name=inference_url,
#                                   headers={"Authorization": "Bearer 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"})
model = "meta-llama/Meta-Llama-3-8B-Instruct"
inference_model= InferenceClient(model = model,api_key=huggingfacetoken)



# for message in client.chat_completion(
# 	model="meta-llama/Meta-Llama-3-8B-Instruct",
# 	messages=[{"role": "user", "content": "What is the capital of France?"}],
# 	max_tokens=500,
# 	stream=True,
# ):
#     print(message.choices[0].delta.content, end="")

# import requests

# API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
# headers = {"Authorization": f"Bearer {huggingfacetoken}"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": {
# 	"source_sentence": "That is a happy person",
# 	"sentences": [
# 		"That is a happy dog",
# 		"That is a very happy person",
# 		"Today is a sunny day"
# 	]
# },
# })

# print(output)