# -*- coding: utf-8 -*-
import xlrd


def get_data(path, table_name):
    file = xlrd.open_workbook(path)
    table = file.sheet_by_name(table_name)
    nrows = table.nrows
    # print nrows
    datas = []
    for i in range(1, nrows):
        label_people = table.row(i)[2].value
        label_method = table.row(i)[3].value
        datas.append((label_people, label_method))
    return datas


if __name__ == "__main__":
    datas = get_data('E:/test/Maps - Navigation & Transit.xlsx', 'Sheet1')
    TP = 0.0
    FP = 0.0
    FN = 0.0
    NN = 0.0
    for label_by_people, label_by_method in datas:
        if label_by_method == 'N':
            if label_by_people == 'N':
                NN = NN + 1
            if label_by_people == 'R':
                FN = FN + 1
        if label_by_method == 'R':
            if label_by_people == 'N':
                FP = FP + 1
            if label_by_people == 'R':
                TP = TP + 1
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F = (2 * precision * recall) / (precision + recall)
    print 'Precision:'
    print precision
    print 'Recall:'
    print recall
    print 'F-measure:'
    print F