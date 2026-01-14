from etl import extract, transform, load


def run_pipeline():
    input_path = "data/input/users.csv"
    output_path = "data/output/messages.csv"

    df = extract(input_path)
    df = transform(df)
    load(df, output_path)


if __name__ == "__main__":
    run_pipeline()
    print("ETL com IA executado com sucesso!")
