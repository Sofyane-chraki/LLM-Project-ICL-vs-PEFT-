# Project Contribution

![image](https://github.com/Sofyane-chraki/LLM-Project-ICL-vs-PEFT-/assets/91961463/c32f27fd-0bd7-43a3-9b36-220b9c3b5dc6)


# LLM-Project-ICL-vs-PEFT-
Here's the repository for the LLM project. Its purpose is to train a Large Language Model (LLM) for question-answering about a specific topic. Additionally, we aim to compare two methods of model training and understand the advantages and drawbacks of each.

The project is structured as follows:

from_pdf_to_csv.py: This file is dedicated to modifying and initially creating our dataset. Originally, its purpose was to extract data in the format of questions and answers and create a CSV file from it.
As we progressed with the project, we modified our dataset to better suit our objectives. This involved adapting the format of the dataset to fit our two methodologies and meet the requirements of the model.

Then we have two jupyter notebook file, each one of them is dedicated for one method.

The "PEFT.ipynb" file encapsulates the culmination of our collaborative efforts. It represents a comprehensive integration of various techniques and methodologies aimed at fine-tuning a Mistral-7B model using 4-bit quantization and QLora training. This notebook serves as a detailed guide, providing step-by-step instructions on preprocessing data, configuring the model architecture, defining hyperparameters, and training the model. 
Additionally, it includes sections on saving the trained model, evaluating its performance, and deploying it for inference tasks. 
By making this notebook available in the GitHub repository, stakeholders can access a structured and executable document that not only demonstrates the implementation of advanced machine learning techniques but also fosters further collaboration and learning within the project team and the broader community.

Finaly we have the dataset in the txt format.

The "ICL(RAG).ipynb" file contains our work about the In-Context Learning method. For the ICL, we decided to make a RAG.
Retrieval-Augmented Generation (RAG) is a framework that combines the strengths of both retrieval-based and generative methods for natural language understanding and generation. In a typical RAG setup, you have two main components: a retriever and a generator. Here's how they work together:

Retriever: When a query or prompt is received, the retriever component searches a large corpus of text to find relevant documents or passages. These are often called the "retrieved contexts".

Generator: The generator is a sequence-to-sequence model that takes both the original query and the retrieved contexts as input to generate a response or answer.

The core idea is to use the retriever to augment the generator with external knowledge, effectively combining the ability of retrieval-based models to access large stores of factual information with the nuanced, context-aware generation capabilities of sequence-to-sequence models.

We use alos  Mistral-7B as model and Langchain.
LangChain is a python open-source library that provides all the elements needed to build an NLP application (precisely a Retrieval Augmented Generation) and link its various parts together in simple pipelines called chains.


