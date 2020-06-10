from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
# import libraries
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
# set up training tools
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from feature_engineer import featureGenerator
from evaluator import Evaluator


class classifier:

    def __init__(self, ticker):
        [self.df, self.y] = featureGenerator(ticker).get_features()
        # train test split
        self.X_train, self.X_test, self.y_train, self.y_test = \
            train_test_split(self.df, self.y, test_size=0.3, shuffle=False)

    def train(self, clf):
        scores = cross_val_score(clf, self.X_train, self.y_train, cv=10)
        clf.fit(self.X_train, self.y_train)
        return [clf, scores]

    def predict(self, clf, offset=0):
        return clf.predict(self.X_test[-1 - offset].reshape(-1, self.X_test.shape[1]))[0]

    def predict_all(self, clf):
        return clf.predict(self.X_test)

    def get_report_message(self):
        df = self.df
        y = self.y

        # logistic regression
        clf0, scores = self.train(LogisticRegression())
        logistic_mean = round(scores.mean(), 2)
        logistic_std = round(scores.std(), 2)
        logistic_prediction = self.predict(clf0)

        # support vector machine
        clf1, scores = self.train(svm.SVC(kernel='linear', C=1))
        svm_mean = round(scores.mean(), 2)
        svm_std = round(scores.std(), 2)
        svm_prediction = self.predict(clf1)

        # XG boosting
        clf2, scores = self.train(XGBClassifier(random_state=0))
        xg_mean = round(scores.mean(), 2)
        xg_std = round(scores.std(), 2)
        xg_prediction = self.predict(clf2)

        # random forest
        clf3, scores = self.train(RandomForestClassifier(max_depth=4, random_state=0))
        rf_mean = round(scores.mean(), 2)
        rf_std = round(scores.std(), 2)
        rf_prediction = self.predict(clf3)

        trend = "predicted trend:" + (
            "<strong>RISING</strong>" if logistic_prediction == 1 else "<strong>FALLING</strong>") + "<br>"
        mean_std = "mean score {}, std {}<br>".format(logistic_mean, logistic_std)
        eval_msg = Evaluator(self.y_test, self.predict_all(clf0)).get_eval_message()
        # logistic regression
        msg0 = """
        {}
        {}
        {}
        """.format(trend, mean_std, eval_msg)

        # support vector machine
        trend = "predicted trend:" + ("<strong>RISING</strong>" if svm_prediction == 1 else "<strong>FALLING</strong>") + "<br>"
        mean_std = "mean score {}, std {}<br>".format(svm_mean, svm_std)
        eval_msg = Evaluator(self.y_test, self.predict_all(clf1)).get_eval_message()
        # svm
        msg1 = """
        {}
        {}
        {}
        """.format(trend, mean_std, eval_msg)

        # XG Boost
        trend = "predicted trend:" + ("<strong>RISING</strong>" if xg_prediction == 1 else "<strong>FALLING</strong>") + "<br>"
        mean_std = "mean score {}, std {}<br>".format(xg_mean, xg_std)
        eval_msg = Evaluator(self.y_test, self.predict_all(clf2)).get_eval_message()
        # svm
        msg2 = """
        {}
        {}
        {}
        """.format(trend, mean_std, eval_msg)

        # random forest
        trend = "predicted trend:" + ("<strong>RISING</strong>" if rf_prediction == 1 else "<strong>FALLING</strong>") + "<br>"
        mean_std = "mean score {}, std {}<br>".format(rf_mean, rf_std)
        eval_msg = Evaluator(self.y_test, self.predict_all(clf3)).get_eval_message()
        # svm
        msg3 = """
        {}
        {}
        {}
        """.format(trend, mean_std, eval_msg)

        # overall prediction

        last_week_prediction = (self.predict(clf0, offset=1)
                                + self.predict(clf1, 1)
                                + self.predict(clf2, 1)
                                + self.predict(clf3, 1)) / 4
        last_week_prediction = round(last_week_prediction)

        last_week_actual = self.y_test[-2]

        message = "The average predicted trend given by all 3 classifiers for last week is {}.".format(
            "rising" if last_week_prediction == 1 else "falling"
        )

        message += '<br>'

        message += "The average confidence level for the prediction is {}.".format(
            (logistic_mean + svm_mean + xg_mean + rf_mean) / 4)

        message += "<br>"

        message += "The actual price trend observed for last week's market was: {}".format(
            "rising" if last_week_actual == 1 else "falling"
        )
        return [msg0, msg1, msg2, msg3, message]
