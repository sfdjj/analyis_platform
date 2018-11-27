# Created by wenchao.jia on 2018/11/27.
# Mail:wenchao.jia@qunar.com

class AnalysisPlatformException(Exception):
    status = 1
    title = '异常'
    __statuses = {status}

    def __init__(self, err='', detail=None, data=None, no_title=False):
        Exception.__init__(self)
        self.err = err
        self.detail = detail
        self.data = data
        self.no_title = no_title

    def __str__(self):
        if self.no_title:
            return self.err
        else:
            return f'[{self.title}]{self.err}'

    def result(self):
        r = {'status': self.status, 'message': str(self)}
        if self.data is not None:
            r['data'] = self.data
        return r

    def __init_subclass__(cls, **kwargs):
        assert cls.status not in cls.__statuses
        cls.__statuses.add(cls.status)


class JsonValidationException(AnalysisPlatformException):
    status, title = 10001, 'json格式错误'
