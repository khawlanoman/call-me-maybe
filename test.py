from llm_sdk.llm_sdk import Small_LLM_Model
import numpy as np



def main() -> str:
    model = Small_LLM_Model()
    user_req = "is rabat a country ?"

    allowed = ["YES", "NO", '"']
    allowed_tkn = []
    for v in allowed:
        allowed_tkn.append(model.encode(v).squeeze().tolist())
    
    prompt = f'''Answer on the user request wiht YES or NO
    User Request : {user_req}
    Answer: "
    '''
    prompt_ids = model.encode(prompt).squeeze().tolist()
    resulr = []
    for _ in range(30):
            logits = model.get_logits_from_input_ids(prompt_ids + resulr)
            masked = np.full_like(logits, -np.inf)

            for tid in allowed_tkn:
                masked[tid] = logits[tid]
            correct = np.argmax(masked)
            resulr.append(correct)
            txt = model.decode(resulr)
            if txt in allowed:
                return txt


if __name__ == "__main__":

    print(main())