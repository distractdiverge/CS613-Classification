import argparse
import pandas as pd
import matplotlib.pyplot as plt
import svm
import naive_bayes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CS 613 - HW 3 Assignment")
    parser.add_argument("--naive-bayes", action="store_true", dest="do_naive_bayes",
                        help="Execute the 'Naive Bayes Classification' problem")
    parser.add_argument("--svm", action="store_true", dest="do_svm",
                        help="Execute the 'Multi-Class Support Vector Machines' problem")

    parser.add_argument("--style", action="store", dest="style", default="ggplot",
                        help="Set the matplotlib render style (default: ggplot)")
    parser.add_argument("--data", action="store", dest="data_filepath", type=str,
                        help="Set the filepath of the data csv file.")

    args = parser.parse_args()

    if not args.do_naive_bayes and not args.do_svm:
        parser.print_help()
        exit(-1)

    if args.do_naive_bayes and not args.data_filepath:
        args.data_filepath = "./spambase.data"

    if args.do_svm and not args.data_filepath:
        args.data_filepath = "./CTG.csv"

    plt.style.use(args.style)

    print "Reading Data from '{0}'".format(args.data_filepath)
    raw_data = pd.read_csv(args.data_filepath, index_col=0)

    if args.do_naive_bayes:
        print "Executing Naive-Bayes Classification"
        naive_bayes.execute(raw_data)
        print ""

    if args.do_svm:
        print "Executing Gradient Descent"
        svm.execute(raw_data)