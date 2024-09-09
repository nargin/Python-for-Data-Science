import pandas


def load(file: str):
    try:
        csv = pandas.read_csv(file)
        return csv
    except Exception as e:
        print(e)
        return None
