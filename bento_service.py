from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput
from bentoml.frameworks.transformers import TransformersModelArtifact

# @env(pip_packages=["transformers==4.26.1", "torch==1.12.1+cu113"])
@env(infer_pip_packages=True)
@artifacts([TransformersModelArtifact("mt5Model")])
class TransformerService(BentoService):
    @api(input=JsonInput(), batch=False)
    def predict(self, parsed_json):
        src_text = parsed_json.get("text")

        model = self.artifacts.mt5Model.get("model")
        tokenizer = self.artifacts.mt5Model.get("tokenizer")

        input_ids = tokenizer.encode(src_text, return_tensors="pt", add_special_tokens=True)
        generated_ids = model.generate(input_ids=input_ids, num_beams=1, num_return_sequences=1)
        output = tokenizer.decode(generated_ids[0])

        return output
