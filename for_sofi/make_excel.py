import pandas as pd


def remove_english(sent: str) -> str:
    if "@en" in str(sent):
        sp = sent.split("@en")
        return sp[0]
    else:
        return sent


if __name__ == "__main__":
    sent = "aaaa"

    file = pd.read_csv('for_sofi/v4.csv', sep='\t')
    file['description'] = file['description'].apply(remove_english)
    # file['prefLabel'] = file['prefLabel'].apply(remove_english)
    # file['altLabel'] = file['altLabel'].apply(remove_english)
    # file['historyNote'] = file['historyNote'].apply(remove_english)

    file.to_excel('for_sofi/noeng_desc.xlsx')
