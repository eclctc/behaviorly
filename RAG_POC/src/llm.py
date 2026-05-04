from llama_cpp import Llama

class LocalLLM:
    def __init__(self, model_path: str = "./models/qwen2.5-0.5b-instruct-q4_k_m.gguf", n_ctx: int = 2048):
        self.model_path = model_path
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_gpu_layers=-1,
            seed=42,
            verbose=False,
        )

    def generate(self, prompt: str, max_tokens: int = 300, temperature: float = 0.0) -> str:
        response = self.llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response["choices"][0]["message"]["content"] # type: ignore
