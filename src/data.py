import pandas as pd


column_names = ["word_freq_make", "word_freq_address", "word_freq_all", "word_freq_3d", "word_freq_our",
                 "word_freq_over", "word_freq_remove", "word_freq_internet", "word_freq_order", "word_freq_mail",
                 "word_freq_receive", "word_freq_will", "word_freq_people", "word_freq_report",
                 "word_freq_addresses", "word_freq_free", "word_freq_business", "word_freq_email", "word_freq_you",
                 "word_freq_credit", "word_freq_your", "word_freq_font", "word_freq_000", "word_freq_money",
                 "word_freq_hp", "word_freq_hpl", "word_freq_george", "word_freq_650", "word_freq_lab",
                 "word_freq_labs", "word_freq_telnet", "word_freq_857", "word_freq_data", "word_freq_415",
                 "word_freq_85", "word_freq_technology", "word_freq_1999", "word_freq_parts", "word_freq_pm",
                 "word_freq_direct", "word_freq_cs", "word_freq_meeting", "word_freq_original", "word_freq_project",
                 "word_freq_re", "word_freq_edu", "word_freq_table", "word_freq_conference", "char_freq_;",
                 "char_freq_(", "char_freq_[", "char_freq_!", "char_freq_$", "char_freq_  #",
                 "capital_run_length_average", "capital_run_length_longest", "capital_run_length_total", "Is Spam"]


def read_spambase_data(filepath):
    """
    Read the spambase data file at the given filepath and return a dataframe
    :param filepath: filepath of the spambase data file
    :return: Pandas dataframe, where the index is the class of the row (1 = spam, 0 = not spam)
    """

    # The id column is always the last in the list of columns
    id_col_index = len(column_names) - 1

    return pd.read_csv(filepath, names=column_names, index_col=id_col_index)
