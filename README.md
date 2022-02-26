# bodleian

The bodleian is an awesome library. Check it out and check out some books. This project seeks to create a library containing every yaml. It will be used in a yaml search feature. 

# What??
When you create a resource, such as a pod, we want to recommend other resources that you can create. In it's first iteration: create a pod, then be presented with yaml that is similar to the pod you've created.  The novel insight here is treating yaml as a language. In the same way we can use Natural Language Processing to "learn" english, we should be able to use it to learn the language of K8S.  

# How??
Input a yaml, output similar yaml. 
 - input comes from when the user provisions a resource. this will serve as the input yaml
 - reccomend. The system will use a cosine distance similarity measurement. We will embed individual yaml files as Word2Vec or Doc2Vec vectors. (let's see which works betterr). Once we've trained our word embeddings, we can use a cosine similarity measurement to find yamls that are very similar to the current pod you just provisioned. 
 - We will construct our dataset of yamls by scraping all public yamls from github. We could also potentially use a more targeted dataset consisting of every yaml used in a particular application. 

# Why..
This could assist with low-code/no-code plug and play system provisioning.

# Who!
You!

# Where!!
Here!!

# When!!
In the background, as a side project throughout Q1 2022. That's the target for a POC

!! USE PYTHON3 
