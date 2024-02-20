import query_hugging_face
import query_openai


def call_lm(openai=False, **kwargs):
    if openai:
        # return query_openai.query_openai_lm(**kwargs)
        pass
    else:
        return query_hugging_face.query_hf_lm(**kwargs)
