# Author: Mohammed Haashir Butt
# Project Main File


pred_model = HealthcareProj('abc.xlsx') # create object and load data
pred_model.create_train_test_split()
pred_model.create_model()
pred_model.fit_model()
pred_model.infer()
pred_model.calc_error()
pred_model.create_plots()
pred_model.print_results()