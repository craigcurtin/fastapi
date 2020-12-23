import pandas as pd
import logging
import itertools
from enum import Enum
import os.path

_ReportOutput = {
    1: ['csv', 'CSV'],
    2: ['xls', 'XLS'],
    3: ['pdf', 'PDF'],
    4: ['txt', 'TXT'],
}
ReportOutput = Enum(
    value='ReportOutput',
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _ReportOutput.items()
    )
)


class CreateReport(object):
    """CreateReport performs the following
            1. Collect Data, (gather the data ... DB2, Postgres, ...)
            2. Shape Data, (create output in desired format)
            3. Delivery Data, (aka push to S3 bucket)
    """

    def __init__(self, data_source, report_target, report_out, report_id):

        # verify input data_source ...
        assert True == os.path.isfile(data_source)
        self.data_source = data_source

        self.report_target = report_target
        self.report_out = report_out
        self.report_id = report_id
        msg = 'Source: {}, Format: {}, Id:{}'.format(self.data_source,
                                                     self.report_out,
                                                     self.report_id)
        logging.debug(msg)

    def run(self):
        """ run and shape the data ..."""

        # assume we are reading csv, pipe_delimit
        df = pd.read_csv(self.data_source, sep='|', index_col=False)
        logging.debug('Read: {} to df, {} records'.format(self.data_source, len(df)))

        if ReportOutput.XLS == self.report_out:
            xls_writer = pd.ExcelWriter(self.report_target, engine='xlsxwriter')
            df.to_excel(xls_writer, sheet_name='PS Fancy Sheet Name 1',
                        na_rep='',
                        float_format=None,
                        columns=None,
                        header=True, verbose=True)

            # Close the Excel writer and output the Excel file.
            xls_writer.save()

        else:
            if ReportOutput.CSV == self.report_out:
                # modify file extention to identify as .zip file
                self.report_target = '{}.zip'.format(self.report_target[:-4])
                compression_opts = dict(method='zip', archive_name=self.report_target)
                df.to_csv(self.report_target, index=False, compression=compression_opts)
            else:
                if ReportOutput.PDF == self.report_out:
                    pass
                else:
                    if ReportOutput.TXT == self.report_out:
                        pass
                    else:
                        assert True, 'Report Output has invalid type {}'.format(self.report_out)

        logging.debug('Write: {} from pandas'.format(self.report_target))

        # verify/validate that we wrote the report_target data
        assert True == os.path.isfile(self.report_target)

        # release Dataframe memory ...
        df = None
