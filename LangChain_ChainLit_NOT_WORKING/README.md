# Llama2-Conflict Resolution-Chatbot
This is a Conflict Resolution bot built using Llama2 and Sentence Transformers. The bot is powered by Langchain and Chainlit. The bot runs on a CPU/GPU machine with a minimum of 16GB of RAM.

### How to run in the terminal?
```bash
pyenv virtualenv 3.12.9 langchain
pyenv local langchain
pip install -r requirements.txt
```

```bash
python ingest.py
chainlit run model.py -w
```
```bash
!pip install accelerate==0.21.0 transformers==4.31.0 tokenizers==0.13.3
!pip install bitsandbytes==0.40.0 einops==0.6.1
!pip install xformers==0.0.22.post7
!pip install langchain==0.1.4
!pip install faiss-gpu==1.7.1.post3
!pip install sentence_transformers
```
