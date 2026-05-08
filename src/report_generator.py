import pandas as pd


def generate_report(results, output_path):

    df = pd.DataFrame(results)

    df = df.sort_values(by="Score", ascending=False)

    df.to_csv(output_path, index=False)

    return df