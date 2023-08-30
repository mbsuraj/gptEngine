from src.gpt_engine.gpt_engine import GPTEngineModel

main_task = "Transform the given document to emphasize"
prompt = "Data Science Skills"
mm = GPTEngineModel(main_task=main_task, input_prompt=prompt)