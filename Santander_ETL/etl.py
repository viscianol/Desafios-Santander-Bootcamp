import pandas as pd
import os

USE_OPENAI = False


def extract(csv_path):
    return pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")


def generate_message_with_ai(nome: str) -> str:
    if not USE_OPENAI:
        return f"Olá {nome}, temos uma oferta personalizada esperando por você!"

    try:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": f"Crie uma mensagem curta e amigável de marketing para o cliente {nome}."
                }
            ],
            temperature=0.7
        )

        return response.choices[0].message["content"]

    except Exception as e:
        return f"Olá {nome}, temos uma oferta especial esperando por você!"


def transform(df):
    df["mensagem"] = df["nome"].apply(generate_message_with_ai)
    return df


def load(df, output_path):
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
