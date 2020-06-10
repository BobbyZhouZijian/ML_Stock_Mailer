from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score


class Evaluator:
    def __init__(self, y_test, y_pred):
        self.y_test = y_test
        self.y_pred = y_pred

    def get_cm_revel(self):
        cm = confusion_matrix(self.y_test, self.y_pred)
        return cm[0][0], cm[0][1], cm[1][0], cm[1][1]

    def get_accuracy(self):
        tp, fp, fn, tn = self.get_cm_revel()
        res = (tp + tn) / (tp + fp + fn + tn)
        return round(res, 2)

    def get_precision(self):
        tp, fp, fn, tn = self.get_cm_revel()
        res = tp / (tp + fp)
        return round(res, 2)

    def get_recall(self):
        tp, fp, fn, tn = self.get_cm_revel()
        res = tp / (tp + fn)
        return round(res, 2)

    def get_f1(self):
        tp, fp, fn, tn = self.get_cm_revel()
        res = (2 * tp) / (2 * tp + fp + fn)
        return round(res, 2)

    def get_auc(self):
        res = roc_auc_score(self.y_test, self.y_pred)
        return round(res, 2)

    def get_eval_message(self):
        cm = self.get_cm_revel()
        message = "EVALUATION OF MODEL:<br>"
        message += """
                    True       False<br>
        Positive    {}          {}<br>
        Negative    {}          {}<br>        
""".format(cm[0], cm[1], cm[2], cm[3])

        message += "Precision rate: {}.<br>".format(self.get_precision())
        message += "Accuracy rate: {}.<br>".format(self.get_accuracy())
        message += "Recall rate: {}.<br>".format(self.get_recall())
        message += "F1 rate: {}.<br>".format(self.get_f1())
        message += "AUC: {}.<br>".format(self.get_auc())
        return message
