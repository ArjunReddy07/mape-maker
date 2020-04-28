import tempfile
import pyutilib.th as unittest
import sys
import os.path
import os
import shutil
import datetime
from datetime import datetime
import mape_maker
from mape_maker import __main__ as mapemain
dir_sep = "/"
p = str(mape_maker.__path__)
l = p.find("'")
r = p.find("'", l+1)
mape_maker_path = p[l+1:r]
file_path = mape_maker_path + dir_sep + "samples"
test_with_error = True

class TestUM(unittest.TestCase):

    def _basic_dict(self):
        basedict = {"input_file": "",
                    "second_file": None,
                    "target_mape": None,
                    "simulated_timeseries": "actuals",
                    "base-process": "iid",
                    "a": 4,
                    "output_dir": None,
                    "number_simulations": 1,
                    "input_start_dt": None,
                    "input_end_dt": None,
                    "simulation_start_dt": None,
                    "simulation_end_dt": None,
                    "title": None,
                    "seed": None,
                    "load_pickle": False,
                    "curvature": None,
                    "time_limit": 3600,
                    "curvature_target": None,
                    "mip_gap": 0.3,
                    "solver": "gurobi",
                    "latex_output": False,
                    "show": True,
                    "verbosity": 2,
                    "verbosity_output": None
                    }
        return basedict

    def test_first(self):
        """
        here is the command :
        python -m mape_maker "mape_maker/samples/2012-2013_BPA_forecasts_actuals.csv" -sf "mape_maker/samples/wind_total_forecast_actual_070113_063015.csv" -s 1234 -n 5 -o "BPA_Wind_1" -is "2012-6-3 00:00:00" -ie "2014-1-1 00:00:00" -sd "2015-6-23 00:00:00" -ed "2015-6-30 00:00:00"
        :return:
        """
        parm_dict = self._basic_dict()
        parm_dict["input_file"] = file_path + dir_sep + "2012-2013_BPA_forecasts_actuals.csv"
        parm_dict["second_file"] = file_path + dir_sep + "wind_total_forecast_actual_070113_063015.csv"
        parm_dict["number_simulations"] = 5
        parm_dict["base-process"] = "iid"
        parm_dict["output_dir"] = "BPA_Wind_1"
        parm_dict["seed"] = 1234
        parm_dict["input_start_dt"] = datetime(year=2012, month=6, day=3, hour=0, minute=0, second=0)
        parm_dict["input_end_dt"] = datetime(year=2014, month=1, day=1, hour=0, minute=0, second=0)
        parm_dict["simulation_start_dt"] = datetime(year=2015, month=6, day=29, hour=0, minute=0, second=0)
        parm_dict["simulation_end_dt"] = datetime(year=2015, month=6, day=30, hour=0, minute=0, second=0)
        parm_list = list(parm_dict.values())
        mapemain.main_func(*parm_list)
        shutil.move("mmFinalFig.png", parm_dict["output_dir"] + dir_sep + "mmFinalFig.png")


    def test_second(self):
        """
        here is the command :
        python -m mape_maker "mape_maker/samples/CAISO_wind_operational_data.csv" -s 1234 -n 5 -bp "iid" -o "Wind_Operation1" -is "2013-7-1 00:00:00" -ie "2015-6-30 23:00:00" -sd "2015-6-29 23:00:00" -ed "2015-6-30 23:00:00"
        :return:
        """
        parm_dict = self._basic_dict()
        parm_dict["input_file"] = file_path + dir_sep + "2012-2013_BPA_forecasts_actuals.csv"
        parm_dict["second_file"] = file_path + dir_sep + "wind_total_forecast_actual_070113_063015.csv"
        parm_dict["simulated_timeseries"] = "actuals"
        parm_dict["number_simulations"] = 5
        parm_dict["base-process"] = "iid"
        parm_dict["output_dir"] = "BPA_Wind_2"
        parm_dict["seed"] = 1234
        parm_dict["input_start_dt"] = datetime(year=2012, month=6, day=3, hour=0, minute=0, second=0)
        parm_dict["input_end_dt"] = datetime(year=2013, month=8, day=3, hour=0, minute=0, second=0)
        parm_dict["simulation_start_dt"] = datetime(year=2015, month=6, day=23, hour=0, minute=0, second=0)
        parm_dict["simulation_end_dt"] = datetime(year=2015, month=6, day=30, hour=0, minute=0, second=0)
        parm_list = list(parm_dict.values())
        mapemain.main_func(*parm_list)
        shutil.move("mmFinalFig.png", parm_dict["output_dir"] + dir_sep + "mmFinalFig.png")


    def test_third(self):
        """
        here is the command :
        python -m mape_maker "mape_maker/samples/CAISO_wind_operational_data.csv" -s 1234 -n 5 -bp "iid" -o "Wind_Operation1" -is "2013-7-1 00:00:00" -ie "2015-6-30 23:00:00" -sd "2015-6-29 23:00:00" -ed "2015-6-30 23:00:00"
        :return:
        """
        parm_dict = self._basic_dict()
        parm_dict["input_file"] = file_path + dir_sep + "2012-2013_BPA_forecasts_actuals.csv"
        parm_dict["second_file"] = file_path + dir_sep + "wind_total_forecast_actual_070113_063015.csv"
        parm_dict["number_simulations"] = 5
        parm_dict["output_dir"] = "BPA_Wind_3"
        parm_dict["seed"] = 1234
        parm_dict["input_start_dt"] = datetime(year=2012, month=8, day=1, hour=0, minute=0, second=0)
        parm_dict["input_end_dt"] = datetime(year=2013, month=6, day=30, hour=0, minute=0, second=0)
        parm_dict["simulation_start_dt"] = datetime(year=2013, month=8, day=1, hour=0, minute=0, second=0)
        parm_dict["simulation_end_dt"] = datetime(year=2014, month=6, day=30, hour=23, minute=0, second=0)
        parm_list = list(parm_dict.values())
        mapemain.main_func(*parm_list)
        shutil.move("mmFinalFig.png", parm_dict["output_dir"] + dir_sep + "mmFinalFig.png")


    def test_forth(self):
        """
        here is the command :
        python -m mape_maker "mape_maker/samples/CAISO_wind_operational_data.csv" -s 1234 -n 5 -bp "iid" -o "Wind_Operation1" -is "2013-7-1 00:00:00" -ie "2015-6-30 23:00:00" -sd "2015-6-29 23:00:00" -ed "2015-6-30 23:00:00"
        :return:
        """
        parm_dict = self._basic_dict()
        parm_dict["input_file"] = file_path + dir_sep + "wind_total_forecast_actual_070113_063015.csv"
        parm_dict["second_file"] = file_path + dir_sep + "rts_gmlc" + dir_sep + "WIND_forecasts_actuals.csv"
        parm_dict["number_simulations"] = 5
        parm_dict["output_dir"] = "Wind_RTS_4"
        parm_dict["seed"] = 1234
        parm_dict["input_start_dt"] = datetime(year=2013, month=8, day=1, hour=0, minute=0, second=0)
        parm_dict["input_end_dt"] = datetime(year=2014, month=6, day=30, hour=23, minute=0, second=0)
        parm_dict["simulation_start_dt"] = datetime(year=2020, month=2, day=1, hour=0, minute=0, second=0)
        parm_dict["simulation_end_dt"] = datetime(year=2020, month=12, day=31, hour=0, minute=0, second=0)
        parm_list = list(parm_dict.values())
        mapemain.main_func(*parm_list)
        shutil.move("mmFinalFig.png", parm_dict["output_dir"] + dir_sep + "mmFinalFig.png")

if __name__ == "__main__":
    unittest.main()