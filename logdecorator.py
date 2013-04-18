# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import re

class LogDecorator(object):
    def __init__(self, logger, extradict, extraformat):
        self._logger = logger
        self._extradict = extradict
        self._extraformat = extraformat

        if re.search('(%[(][a-zA-Z]+[)][^a-z]|%[(][a-zA-Z]+[)]$)', extraformat):
            raise ValueError('format string contains a %(attribute)'
                             'pattern without a type specifier.')

    def _expanded_message(self, message):
        extradict = dict(self._extradict)
        extradict['message'] = message
        extramessage = self._extraformat % extradict
        return extramessage

    def logger(self):
        return self._logger

    def debug(self, message, *args, **kwargs):
        self._logger.debug(self._expanded_message(message), *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self._logger.info(self._expanded_message(message), *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self._logger.warning(self._expanded_message(message), *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self._logger.error(self._expanded_message(message), *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self._logger.critical(self._expanded_message(message), *args, **kwargs)

    def log(self, lvl, message, *args, **kwargs):
        self._logger.log(lvl, self._expanded_message(message), *args, **kwargs)

    def exception(self, message, *args, **kwargs):
        self._logger.exception(self._expanded_message(message), *args, **kwargs)