#!/usr/bin/env python
import json
import logging
import sys
from ctypes import *
from datetime import date
from timeit import default_timer as timer


def main():
    today = date.today().isoformat()
    log_filename = "{}_rpn_api.log".format(today)
    logging.basicConfig(filename=log_filename, filemode="a", level=logging.DEBUG, format='%(asctime)s: [%(levelname)s] %(message)s')
    logging.info("New request!")

    # Load file
    with open(sys.argv[1]) as rpn_json_file:
        rpn_json_load = json.load(rpn_json_file)
    logging.info("Received input: %s" , rpn_json_load)

    # Split by new line and ignore first input (not needed)
    input_rpn_list = rpn_json_load["input_rpn"].splitlines()[1:]

    # Load RPN library
    lib_rpn = cdll.LoadLibrary("./librpn.so")

    # Define class GoString to map:
    # C type struct { const char *p; GoInt n; }
    class GoString(Structure):
        _fields_ = [("p", c_char_p), ("n", c_longlong)]

    # Describe and call start_job()
    lib_rpn.start_job.argtypes = [GoString]
    lib_rpn.start_job.restype = c_double

    # Prepare dictionary for results
    rpn_results = {}

    for index, input_rpn in enumerate(input_rpn_list):
        go_input_rpn = GoString(input_rpn, len(input_rpn))

        logging.info("Calculating: %s" , input_rpn)
        rpn_start = timer()
        rpn_result = lib_rpn.start_job(go_input_rpn)
        rpn_end = timer()
        rpn_time = rpn_end - rpn_start
        logging.info("Result and time: [%f, %f]" , rpn_result, rpn_time)

        rpn_results[index] = {"input": input_rpn,"result": rpn_result, "time": rpn_time}

    # Return to Ruby
    print json.dumps(rpn_results)


if __name__ == "__main__":
    main()
