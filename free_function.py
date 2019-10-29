from  SystemRekomendacyjny.challange_function.src.score_submission import score_subm as ss
from  SystemRekomendacyjny.challange_function.src.verify_submission import verify_subm as vs
from SystemRekomendacyjny.challange_function.src.baseline_algorithm import rec_popular as rp

subm_csv = '../data/submission_popular.csv'
gt_csv = '../data/groundTruth.csv'
test_csv = '../data/test.csv'
data_path = '../data/'

def baseline():
    rp.main(data_path)

def verify():
    vs.main(subm_csv, test_csv)


def score():
    ss.main(gt_csv, subm_csv)

if __name__ == '__main__':

   # baseline()
    verify()
    #score()
