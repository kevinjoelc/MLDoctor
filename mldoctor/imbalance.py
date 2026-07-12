def check_imbalance(df,target):

    counts=df[target].value_counts()

    percent=(counts/len(df)*100).round(2)

    return {

        "count":counts.to_dict(),

        "percentage":percent.to_dict()

    }