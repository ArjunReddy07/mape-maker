import tempfile
import pyutilib.th as unittest
import sys
import os.path
import os
import glob
import pandas as pd
import shutil
import datetime
from datetime import datetime
import shutil
import mape_maker
from mape_maker import __main__ as mapemain
from collections.abc import Iterable
dir_sep = "/"
p = str(mape_maker.__path__)
l = p.find("'")
r = p.find("'", l+1)
mape_maker_path = p[l+1:r]
file_path = mape_maker_path + dir_sep + "samples"

# whether to skip the last two tests
quick_test = False
# whether to run only one example
skip_all_but_one = False
# whether to skip the test which always fails
test_known_failure = False


class TestUM(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # make a temp dir
        self.temp_dir = tempfile.mkdtemp()
        sys.path.insert(1, self.temp_dir)
        # change to the temp directory
        os.chdir(self.temp_dir)
        self.cwd = os.getcwd()
        print("temporary directory:", self.cwd)
        # path to the RTS Load data
        # self.load_data = file_path + dir_sep + ".." + dir_sep + ".." + dir_sep + "mape_maker" + dir_sep + \
        #                  "samples" + dir_sep + "based_rts_gmlc" + dir_sep + "Load_rts_gmlc"+ dir_sep + \
        #                  "processed_file.csv"
        self.load_data = mape_maker_path + dir_sep + "samples" + \
                         dir_sep + "based_rts_gmlc" + dir_sep + "Load_rts_gmlc_based" \
                         + dir_sep + "processed_file.csv"

    def _base_dict(self):
        """
        initialize the parameters
        :return: basedict
        """
        basedict = {"input_file"            : "",
                    "target_mape"           : None,
                    "simulated_timeseries"  : "",
                    "base-process"          : "",
                    "a"                     : None,
                    "output_dir"            : "result",
                    "number_simulations"    : 2,
                    "input_start_dt"        : None,
                    "input_end_dt"          : None,
                    "simulation_start_dt"   : None,
                    "simulation_end_dt"     : None,
                    "title"                 : "",
                    "seed"                  : 1234,
                    "load_pickle"           : False,
                    "curvature"             : False,
                    "time_limit"            : 1,
                    "curvature_target"      : None,
                    "mip_gap"               : None,
                    "solver"                : "gurobi",
                    "latex_output"          : False,
                    "show"                  : True,
                    "verbosity"             : 2,
                    "verbosity_output"      : None
                    }

        return basedict

    def create_temp_dir(self):
        """
        create a sub temporary directory inside the main temporary directory
        to save the output file
        """
        sub_directory = tempfile.mkdtemp(dir=self.temp_dir)
        print("sub temporary directory:", sub_directory)
        return sub_directory

    def test_load_actuals_iid(self):
        print("Running ", str(self.id()).split('.')[2])
        # python -m mape_maker "mape_maker/samples/based_rts_gmlc/Load_rts_gmlc_based/processed_file.csv" -st "actuals" -n 3 -bp "ARMA" -o "load_actuals_iid" -s 1234
        parm_dict                           = self._base_dict()
        parm_dict["input_file"]             = self.load_data
        parm_dict["simulated_timeseries"]   = "actuals"
        parm_dict["number_simulations"]     = 2
        parm_dict["base-process"]           = "ARMA"
        parm_dict["output_dir"]             = "load_actuals_iid"
        parm_list                           = list(parm_dict.values())
        # run the test
        mapemain.main_func(*parm_list)
        # save the output dir to the sub temporary directory
        output_dir_path = self.temp_dir + dir_sep + parm_dict["output_dir"]
        print("output_dir_path = ", output_dir_path)
        print("parm_dict[output_dir]", parm_dict["output_dir"])
        temp_sub_dir = self.create_temp_dir()
        print("Created temp_sub_dir = ", temp_sub_dir)
        shutil.move(output_dir_path, temp_sub_dir)

    @unittest.skipIf(skip_all_but_one,
                     "skipping the second test")
    def test_load_actuals_ARMA_dates(self):
        print("Running ", str(self.id()).split('.')[2])
        # python -m mape_maker "mape_maker/samples/based_rts_gmlc/Load_rts_gmlc_based/processed_file.csv" -st "actuals" -n 2 -bp "ARMA" -is "2020-5-1 1:0:0" -ie "2020-7-30 0:0:0" -sd "2020-6-1 0:0:0" -ed "2020-6-30 23:0:0" -o "load_actuals_ARMA" -s 1234
        parm_dict                           = self._base_dict()
        parm_dict["input_file"]             = self.load_data
        parm_dict["simulated_timeseries"]   = "actuals"
        parm_dict["base-process"]           = "iid"
        parm_dict["input_start_dt"]         = datetime(year=2020, month=5, day=1,   hour=1,   minute=0, second=0)
        parm_dict["input_end_dt"]           = datetime(year=2020, month=7, day=30,  hour=0,   minute=0, second=0)
        parm_dict["simulation_start_dt"]    = datetime(year=2020, month=6, day=10,   hour=0,   minute=0, second=0)
        parm_dict["simulation_end_dt"]      = datetime(year=2020, month=6, day=30,  hour=23,  minute=0, second=0)
        parm_dict["output_dir"]             = "load_actuals_ARMA"
        parm_list                           = list(parm_dict.values())
        # run the test
        mapemain.main_func(*parm_list)
        # save the output dir to the sub temporary directory
        output_dir_path = self.temp_dir + dir_sep + parm_dict["output_dir"]
        shutil.move(output_dir_path, self.create_temp_dir())

    @unittest.skipIf(skip_all_but_one or test_known_failure or quick_test,
                     "skipping the third test")
    def test_load_actuals_ARMA(self):
        print("Running ", str(self.id()).split('.')[2])
        # python -m mape_maker "mape_maker/samples/based_rts_gmlc/Load_rts_gmlc_based/processed_file.csv" -st "forecasts" -n 3 -bp "ARMA" -o "load_actuals_ARMA" -s 1234
        parm_dict                           = self._base_dict()
        parm_dict["input_file"]             = self.load_data
        parm_dict["simulated_timeseries"]   = "forecasts"
        parm_dict["base-process"]           = "ARMA"
        parm_dict["output_dir"]             = "load_actuals_ARMA"
        parm_list                           = list(parm_dict.values())

        # run the test
        mapemain.main_func(*parm_list)
        # save the output dir to the sub temporary directory

        output_dir_path = self.temp_dir + dir_sep + parm_dict["output_dir"]
        shutil.move(output_dir_path, self.create_temp_dir())

    @unittest.skipIf(skip_all_but_one or test_known_failure or quick_test,
                     "skipping the fourth test")
    def test_load_forecasts_iid_dates(self):
        print("Running ", str(self.id()).split('.')[2])
        # python -m mape_maker "mape_maker/samples/based_rts_gmlc/Load_rts_gmlc_based/processed_file.csv" -st "forecasts" -n 2 -bp "iid" -is "2020-5-1 1:0:0" -ie "2020-7-30 0:0:0" -sd "2020-6-1 0:0:0" -ed "2020-6-30 23:0:0" -o "load_forecasts_iid" -s 1234
        parm_dict                           = self._base_dict()
        parm_dict["input_file"]             = self.load_data
        parm_dict["simulated_timeseries"]   = "forecasts"
        parm_dict["number_simulations"]     = 2
        parm_dict["base-process"]           = "iid"
        parm_dict["input_start_dt"]         = datetime(year=2020, month=5, day=1,   hour=1,   minute=0, second=0)
        parm_dict["input_end_dt"]           = datetime(year=2020, month=7, day=30,  hour=0,   minute=0, second=0)
        parm_dict["simulation_start_dt"]    = datetime(year=2020, month=6, day=1,   hour=0,   minute=0, second=0)
        parm_dict["simulation_end_dt"]      = datetime(year=2020, month=6, day=30,  hour=23,  minute=0, second=0)
        parm_dict["output_dir"]             = "load_forecasts_iid"
        parm_list                           = list(parm_dict.values())

        # run the test
        mapemain.main_func(*parm_list)

        # save the output dir to the sub temporary directory
        output_dir_path = self.temp_dir + dir_sep + parm_dict["output_dir"]
        shutil.move(output_dir_path, self.create_temp_dir())


if __name__ == "__main__":
    unittest.main()
