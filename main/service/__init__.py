# Created by wenchao.jia on 2018/11/20.
# Mail:wenchao.jia@qunar.com

class BaseService(SessionSupporter):
    def __init__(self, session: Session):
        if isinstance(session, BaseService):
            session = session.session
        super().__init__(session)
        self.logger = logging.getLogger(self.logger_name)
