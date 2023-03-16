# bentoml-transformers-tutorial

1. Installation 

   - BentoML requires **Python 3.7** or above.
   - `pip install -r requirements.txt`
   - Install **torch** for your version


 2. Creating a Service

    1. `python3 bento_packer.py`

    2. `bentoml list`
![image](https://user-images.githubusercontent.com/50271311/225471723-2c18d44e-a941-4ffd-bb97-7a94377d2583.png)

    3. run : `bentoml serve TransformerService:latest`
![image](https://user-images.githubusercontent.com/50271311/225473570-4f85baa0-c361-4a53-b494-e8c9cc9843d0.png)

    4. Go to http://localhost:5000 and check the connection

    5. Send prediction request to the service: 
![image](https://user-images.githubusercontent.com/50271311/225473824-556d7bce-2015-43e9-84d6-a16edd1ec6ab.png)
![image](https://user-images.githubusercontent.com/50271311/225473851-c90d890a-e53e-4a0f-a26c-dac0b2e97be1.png)
    
    6. Using Python3 

       ```
       import requests
       res = requests.post("http://127.0.0.1:5000/predict", json={"text": "transformer"})
       print(res.text)
       
       ## "<pad> 트랜스포머</s>"
       ```


3. Running the Yatai server : `bentoml yatai-service-start`

    Go to http://localhost:3000 and check the connection
    ![image](https://user-images.githubusercontent.com/50271311/225474320-3e60ce6e-aaa5-4110-9efa-13184bc319b2.png)


4. Generate Docker Image
   - `bentoml containerize TransformerService:latest `
   - For Mac With Apple Silicon
     `bentoml containerize --platform=linux/amd64 iris_classifier:latest`

<br>


## Running load tests using Locust

Run : `locust -f locust.py`

Go to http://localhost:8089 and check the connection

- **Number of users** : maximum number of users
- **Spawn rate** : User creations per second
- **Host** : Target address

![image](https://user-images.githubusercontent.com/50271311/225476700-b109c825-a10c-409a-a45d-a2f7e4c7aa97.png)
![image](https://user-images.githubusercontent.com/50271311/225476711-2e103bfb-a2c9-49a6-91c3-c4f6c099490f.png)

<br>


### Reference
- https://zuminternet.github.io/BentoML/
- https://velog.io/@perfitt/BentoML-%EC%82%BD%EC%A7%88%EA%B8%B0
- https://velog.io/@gtpgg1013/MLOps-BentoML-1
- https://etloveguitar.tistory.com/145

    
