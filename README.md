# LLM Creation?

<!-- ## Commands Need to be Excuted

```pwsh
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
``` -->

## ipynb sequences

* 00 -> Basics</br>
CPU vs. GPU: Explain the difference between using CPU and GPU for computations in machine learning tasks. Discuss the advantages and limitations of each hardware type and when to choose one over the other.
</br>hecking CUDA Availability: Guide users on how to check if CUDA (Compute Unified Device Architecture) is available on their system. CUDA is a parallel computing platform and application programming interface (API) model created by NVIDIA.

* 01 -> Introduction to Vector Databases</br>
Use Cases: Illustrate common use cases where vector databases are beneficial, such as semantic search, recommendation systems, similarity matching, and clustering.

* 02 -> Creating Vectors/Embeddings with Different Frameworks</br>
This section focuses on practical techniques for generating embeddings using popular frameworks such as Gensim and SentenceTransformers. It may include:
</br>Gensim: Explain how to create word embeddings using Gensim, a Python library for topic modeling and document similarity analysis. Cover techniques such as Word2Vec, Doc2Vec, and FastText for generating embeddings from text data.
</br>SentenceTransformers: Introduce SentenceTransformers, a Python library for generating sentence embeddings using pre-trained transformer models (e.g., BERT, RoBERTa). Demonstrate how to use SentenceTransformers to encode sentences into high-dimensional vectors for downstream tasks.

* 03 -> Working with Transformers</br>
This section focuses on the world of transformers, a groundbreaking architecture in natural language processing (NLP), and its applications in performing various NLP tasks such as sentiment analysis, text classification, machine translation, and more.</br>Introduction to pipelines, tokenizers and it's archetecture....
