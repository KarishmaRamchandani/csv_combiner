import os
import sys
import pandas as pd
import error_codes

"""
Author - Karishma Ramchandani
csv_combiner.py - Reads multiple csv files and combines them with additional column of file name 
Input - csv file name and path (Pre-requisite : All files should have same columns)
Output - One combined csv file with additional filename column 
"""

CHUNK_SIZE = 10**6
SEPERATOR = ","


class CsvCombiner:

    def validate(self, file_list):
        """
        verifies whether file path and file is valid or not
        input - file_list = the list of all files with file path 
        output - returns bool True if all files and file path are valid 
        """

        for file_path in file_list:
            if not os.path.isfile(file_path):
                raise Exception(error_codes.INVALID_INPUT_PATH)
            elif os.path.getsize(file_path) == 0:
                raise Exception(error_codes.EMPTY_FILE_EXCEPTION)
        return True

    def combine(self, file_list):
        """
        method name - combine - combines file content and creates new column with file name, given file name and path is correct
        input - file_list = the list of all files with file path 
        output - returns 
        """
        if not file_list:
            raise Exception(error_codes.NO_INPUT_ARGUMENTS)

        self.validate(file_list)

        header = True
        for input_file in file_list:

            for chunk in pd.read_csv(input_file, sep=SEPERATOR, chunksize=CHUNK_SIZE):
                chunk["filename"] = os.path.basename(input_file)

                print(chunk.to_csv(index=False, header=header),  end='')
                header = False


def main():
    combiner = CsvCombiner()
    combiner.combine(sys.argv[1:])


if __name__ == "__main__":
    main()
